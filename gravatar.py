import hashlib
from typing import Any
from mcp.server.fastmcp import FastMCP
from openapi_client import Configuration, ApiClient, ProfilesApi
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


# Load the access token
token = _load_token(CONFIG_PATH)

# Initialize the raw ProfilesApi client for hash-based lookup
_config = Configuration()
_config.access_token = token
_api_client = ApiClient(configuration=_config)
profiles_api = ProfilesApi(_api_client)


@mcp.tool(name="get_profile_by_email")
async def get_profile(email: str) -> dict[str, Any]:
    """
    Fetch Gravatar profile for a given email address.

    Args:
        email: User's email address.
    """
    # Normalize and hash the email
    normalized = email.strip().lower()
    profile_id = hashlib.sha256(normalized.encode("utf-8")).hexdigest()

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
    """
    profile = profiles_api.get_profile_by_id(hash)
    if hasattr(profile, "to_dict"):
        return profile.to_dict()
    return profile

if __name__ == "__main__":
    # Run the MCP server over stdio
    mcp.run(transport="stdio")
