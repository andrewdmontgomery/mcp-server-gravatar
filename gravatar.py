import hashlib
import os
import json
import httpx
from typing import Any
from mcp.server.fastmcp import FastMCP
from gravatar_api_client import GravatarApiClient

# Initialize FastMCP server
mcp = FastMCP("gravatar")

# Constants
GRAVATAR_API_BASE = "https://api.gravatar.com/v3"
USER_AGENT = "gravatar-mcp/1.0"

# Load configuration and initialize Gravatar API client
# You can override via environment var GRAVATAR_CONFIG_PATH, otherwise defaults to './config.json'
CONFIG_PATH = os.environ.get("GRAVATAR_CONFIG_PATH", "config.json")
client = GravatarApiClient(CONFIG_PATH)


@mcp.tool()
async def get_profile(email: str) -> dict[str, Any]:
    """
    Fetch Gravatar profile for a given email address.

    Args:
        email: User's email address.
    """
    # Normalize and hash the email
    normalized = email.strip().lower()
    profile_id = hashlib.sha256(normalized.encode("utf-8")).hexdigest()

    # Fetch the profile using your client
    profile = client.get_profile_by_id(profile_id)

    # If the returned object has a to_dict method (e.g. a generated model), convert it:
    if hasattr(profile, "to_dict"):
        return profile.to_dict()

    # Otherwise assume it's already JSON‐serializable
    return profile


if __name__ == "__main__":
    # Run the MCP server over stdio
    mcp.run(transport="stdio")
