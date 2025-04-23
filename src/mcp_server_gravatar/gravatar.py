import httpx
from typing import overload, Literal, Union, Any

from mcp.server.fastmcp import FastMCP
from openapi_client.models.profile import Profile

from .gravatar_client import client
from .tools import profile_tools

# Initialize FastMCP server
mcp = FastMCP("gravatar")
profile_tools.register_tools(mcp)


@mcp.tool(name="get_avatars")
async def get_avatars(selected_email_hash: str | None = None) -> list[dict[str, Any]]:
    """
    List all avatars for the authenticated user in JSON-friendly format.

    Args:
        selected_email_hash: Optional SHA256 hash of an email to mark that avatar as selected.

    Returns:
        list[dict[str, Any]]: A list of avatar metadata dictionaries.
    """
    if selected_email_hash is not None:
        avatars = client.avatars_api.get_avatars(
            selected_email_hash=selected_email_hash)
    else:
        avatars = client.avatars_api.get_avatars()
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


@mcp.tool(name="get_selected_avatar_as_image")
async def get_selected_avatar_as_image(email: str | None = None) -> list[bytes]:
    """
    Fetch and return the raw image bytes for the selected avatar.

    Args:
        email: User's email address to determine which avatar is selected.

    Returns:
        list[bytes]: A single-element list containing the selected avatar image bytes.
    """
    # Reuse the metadata tool to get avatar URLs
    selected_hash = client.hash_email(email)
    avatars = await get_avatars(selected_email_hash=selected_hash)
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


def serve():
    # Run the MCP server over stdio
    mcp.run(transport="stdio")
