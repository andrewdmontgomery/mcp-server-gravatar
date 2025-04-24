import httpx
from typing import Any
from mcp.server.fastmcp import FastMCP, Image


class AvatarTools:
    def __init__(self, client):
        """
        Initialize with a Gravatar API client.
        """
        self.client = client

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
        Fetch and return the raw image bytes for all avatars.
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

    async def get_selected_avatar_as_image(self, email: str | None = None) -> list[Image]:
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
        images: list[Image] = []
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
                images.append(Image(data=response.content))
                break
        return images

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="get_avatars",
            description="Fetch all avatars"
        )
        async def get_avatars(selected_email_hash: str | None = None) -> list[dict[str, Any]]:
            return await self.get_avatars(selected_email_hash)

        @mcp.tool(
            name="get_avatars_as_images",
            description="Fetch all avatars as images"
        )
        async def get_avatars_as_images(selected_email_hash: str | None = None) -> list[Image]:
            return await self.get_avatars_as_images(selected_email_hash)

        @mcp.tool(
            name="get_selected_avatar_as_image",
            description="Fetch the selected avatar as an image"
        )
        async def get_selected_avatar_as_image(email: str | None = None) -> list[Image]:
            return await self.get_selected_avatar_as_image(email)
