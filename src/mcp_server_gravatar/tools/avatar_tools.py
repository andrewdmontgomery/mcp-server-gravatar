import httpx
import json
from typing import Any
from fastmcp import FastMCP, Image


class AvatarTools:
    def __init__(self, client):
        """
        Initialize with a Gravatar API client.
        """
        self.client = client

    async def get_avatar_by_id(self, avatar_identifier: str) -> bytes:
        """
        Fetch an avatar as raw data using its avatar_identifier hash
        """
        if not avatar_identifier:
            raise ValueError("avatar_identifier must not be empty")
        async with httpx.AsyncClient(verify=False) as client_http:
            avatar_url = "https://gravatar.com/avatar/{avatar_identifier}"
            response = await client_http.get(avatar_url)
            response.raise_for_status()
            return response.content

    async def get_avatar_by_id_as_image(self, avatar_identifier: str) -> Image:
        """
        Fetch an avatar image using its avatar_identifier hash
        """
        avatar = await self.get_avatar_by_id(avatar_identifier)
        return Image(avatar)

    async def get_avatar_by_email(self, email: str) -> bytes:
        """
        Fetch an avatar as raw data using its email address
        """
        avatar_identifier = self.client.hash_email(email)
        avatar = await self.get_avatar_by_id(avatar_identifier)
        return avatar

    async def get_avatar_by_email_as_image(self, email: str) -> Image:
        """
        Fetch an avatar image using its email address
        """
        avatar = await self.get_avatar_by_email(email)
        return Image(avatar)

    async def get_avatars(self, selected_email_hash: str | None = None) -> list[dict[str, Any]]:
        """
        List all avatars for the authenticated user in JSON-friendly format.

        Args:
            selected_email_hash: Optional SHA256 hash of an email to mark that avatar as selected.

        Returns:
            list[dict[str, Any]]: A list of avatar metadata dictionaries.
        """
        if selected_email_hash is not None:
            avatars = self.client.get_avatars(
                selected_email_hash=selected_email_hash)
        else:
            avatars = self.client.get_avatars()
        result = []
        for avatar in avatars:
            if hasattr(avatar, "model_dump"):
                # Pydantic v2 JSON-compatible dump (converts datetime to strings)
                result.append(avatar.model_dump(
                    mode="json", by_alias=True, exclude_unset=True))
            elif hasattr(avatar, "to_dict"):
                result.append(avatar.to_dict())
            else:
                result.append(avatar)
        return result

    async def get_avatars_as_images(self, selected_email_hash: str | None = None) -> list[Image]:
        """
        Fetch and return the images for all avatars.
        """
        avatars = await self.get_avatars(selected_email_hash=selected_email_hash)
        images: list[Image] = []
        # TODO: Use a proper CA for SSL certificate validation
        async with httpx.AsyncClient(verify=False) as client_http:
            for avatar in avatars:
                url = avatar.get("image_url")
                if not url:
                    continue
                response = await client_http.get(url)
                response.raise_for_status()
                images.append(Image(data=response.content))
        return images

    async def get_avatars_as_bytes(self, selected_email_hash: str | None = None) -> list[bytes]:
        """
        Fetch and return the raw image bytes for all avatars.
        """
        avatars = await self.get_avatars(selected_email_hash=selected_email_hash)
        images: list[bytes] = []
        # TODO: Use a proper CA for SSL certificate validation
        async with httpx.AsyncClient(verify=False) as client_http:
            for avatar in avatars:
                url = avatar.get("image_url")
                if not url:
                    continue
                response = await client_http.get(url)
                response.raise_for_status()
                images.append(response.content)
        return images

    async def get_selected_avatar_as_image(self, email: str | None = None) -> list[Image]:
        """
        Fetch and return images for the selected avatar.

        Args:
            email: User's email address to determine which avatar is selected.

        Returns:
            list[Image]: A single-element list containing the selected avatar image.
        """
        avatars_as_bytes = self.get_selected_avatar_as_bytes(email=email)
        avatars = map(lambda bytes: Image(data=bytes), avatars_as_bytes)
        return avatars

    async def get_selected_avatar_as_bytes(self, email: str | None = None) -> list[bytes]:
        """
        Fetch and return the raw image bytes for the selected avatar.

        Args:
            email: User's email address to determine which avatar is selected.

        Returns:
            list[bytes]: A single-element list containing the selected avatar image bytes.
        """
        # Reuse the metadata tool to get avatar URLs
        selected_hash = self.client.hash_email(email)
        avatars = await self.get_avatars(selected_email_hash=selected_hash)
        images: list[bytes] = []
        # TODO: Use a proper CA for SSL certificate validation
        async with httpx.AsyncClient(verify=False) as client_http:
            for avatar in avatars:
                if not avatar.get("selected"):
                    continue
                url = avatar.get("image_url")
                if not url:
                    continue
                response = await client_http.get(url)
                response.raise_for_status()
                images.append(response.content)
                break
        return images

    def register_tools(self, mcp: FastMCP):
        @mcp.tool()
        async def get_avatar_by_id_as_image(hash: str) -> Image:
            """
            Fetch the avatar for a given id as an image.
            """
            avatar = await self.get_avatar_by_id_as_image(hash)
            return avatar

        @mcp.tool()
        async def get_avatars(selected_email_hash: str | None = None) -> list[dict[str, Any]]:
            """
            Fetch all avatars.
            """
            avatars = await self.get_avatars(selected_email_hash)
            return avatars

        @mcp.tool()
        async def get_avatars_as_images(selected_email_hash: str | None = None) -> list[Image]:
            """
            Fetch all avatars as images.
            """
            avatars = await self.get_avatars_as_images(selected_email_hash)
            return avatars

        @mcp.tool()
        async def get_selected_avatar_as_image(email: str | None = None) -> list[Image]:
            """
            Fetch the selected avatar as an image.
            """
            return await self.get_selected_avatar_as_image(email)

    def register_resources(self, mcp: FastMCP):
        @mcp.resource(
            uri="avatar://avatar_identifier/{avatar_identifier}",
            name="Get avatar for id",
            description="Returns an avatar for a given id",
            mime_type="image/png"
        )
        async def get_avatar_by_id(avatar_identifier: str) -> bytes:
            avatar = await self.get_avatar_by_id(avatar_identifier=avatar_identifier)
            return avatar

        @mcp.resource(
            uri="avatar://email/{email}",
            name="Get avatar for email",
            description="Returns an avatar for a given email address",
            mime_type="image/png"
        )
        async def get_avatar_by_email(email: str) -> bytes:
            avatar = await self.get_avatar_by_email(email)
            return avatar

        @mcp.resource(
            uri="avatars://me",
            name="Get all avatars",
            description="Returns the avatars object as json for the authenticated user",
            mime_type="application/json"
        )
        async def get_avatars() -> str:
            avatars = await self.get_avatars()
            return json.dumps(avatars)

        @mcp.resource(
            uri="avatars://me/images/{index}",
            name="Get avatars at index",
            description="Returns an avatar of the authenticated user as an image with a given index",
            mime_type="image/png"
        )
        async def get_avatar_at_index(index: int) -> bytes:

            avatars = await self.get_avatars()
            # Guard against invalid index
            if index < 0 or index >= len(avatars):
                raise IndexError(
                    f"Avatar index {index} is out of range (0 to {len(avatars)-1})")

            url = avatars[index]["image_url"]
            # TODO: handle SSL verification
            data = (await httpx.AsyncClient(verify=False).get(url)).content
            return data
