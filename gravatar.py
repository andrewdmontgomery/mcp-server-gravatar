import hashlib
from typing import Any
from mcp.server.fastmcp import FastMCP
from openapi_client import Configuration, ApiClient, ProfilesApi
from openapi_client.api.avatars_api import AvatarsApi
import os
import json

# Initialize FastMCP server
mcp = FastMCP("gravatar")

# Constants
GRAVATAR_API_BASE = "https://api.gravatar.com/v3"
USER_AGENT = "gravatar-mcp/1.0"

# Load configuration and initialize Gravatar API client
# You can override via environment var GRAVATAR_CONFIG_PATH, otherwise defaults to './config.json'
CONFIG_PATH = os.environ.get("GRAVATAR_CONFIG_PATH", "config.json")


def _load_token(config_path: str) -> str:
    """
    Load access token from a JSON configuration file.
    """
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
    with open(config_path, 'r') as f:
        data = json.load(f)
    token = data.get('access_token') or data.get('token')
    if not token:
        raise ValueError("Missing 'access_token' in configuration file")
    return token


def _hash_email(email: str) -> str:
    """
    Normalize an email address and return its SHA256 hash.
    """
    normalized = email.strip().lower()
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


# Load the access token
token = _load_token(CONFIG_PATH)

# Initialize the raw ProfilesApi client for hash-based lookup
_config = Configuration()
_config.access_token = token
_api_client = ApiClient(configuration=_config)
profiles_api = ProfilesApi(_api_client)

# Initialize the AvatarsApi client for listing avatars
avatars_api = AvatarsApi(_api_client)


@mcp.tool(name="get_profile_by_email")
async def get_profile_by_email(email: str) -> dict[str, Any]:
    """
    Fetch Gravatar profile for a given email address.

    Args:
        email: User's email address.

    Returns:
        dict[str, Any]: The JSON-deserialized Gravatar profile object.
    """
    profile_id = _hash_email(email)

    # Fetch the profile using the raw ProfilesApi client
    profile = profiles_api.get_profile_by_id(profile_id)

    # If the returned object has a to_dict method (e.g. a generated model), convert it:
    if hasattr(profile, "to_dict"):
        return profile.to_dict()

    # Otherwise assume it's already JSON‐serializable
    return profile


@mcp.tool(name="get_profile_by_hash")
async def get_profile_by_hash(hash: str) -> dict[str, Any]:
    """
    Fetch Gravatar profile for a given SHA256 hash (by hash).

    Args:
        hash: SHA256 hash of the lowercase email string.

    Returns:
        dict[str, Any]: The JSON-deserialized Gravatar profile object.
    """
    profile = profiles_api.get_profile_by_id(hash)
    if hasattr(profile, "to_dict"):
        return profile.to_dict()
    return profile


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
        avatars = avatars_api.get_avatars(
            selected_email_hash=selected_email_hash)
    else:
        avatars = avatars_api.get_avatars()
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
    selected_hash = _hash_email(email)
    avatars = await get_avatars(selected_email_hash=selected_hash)
    images: list[bytes] = []
    # TODO: Use a proper CA for SSL certificate validation
    async with httpx.AsyncClient(verify=False) as client:
        for avatar in avatars:
            if not avatar.get("selected"):
                continue
            url = avatar.get("image_url")
            if not url:
                continue
            response = await client.get(url)
            response.raise_for_status()
            images.append(response.content)
            break
    return images


if __name__ == "__main__":
    # Run the MCP server over stdio
    mcp.run(transport="stdio")
