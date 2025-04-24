import json
from mcp.server.fastmcp import FastMCP
from .tools import profile_tools, avatar_tools


def register_resources(mcp: FastMCP):
    @mcp.resource(
        uri="gravatar://profiles/{profileIdentifier}",
        name="Get Profile by ID",
        description="Returns a profile object as json",
        mime_type="application/json")
    async def get_profile(profileIdentifier: str) -> str:
        profile = await profile_tools._get_profile_by_hash(profileIdentifier)
        return json.dumps(profile)

    @mcp.resource(
        uri="gravatar://me/avatars",
        name="List Avatars",
        description="Returns a list of avatars",
        mime_type="application/json")
    async def get_avatars() -> str:
        avatars = await avatar_tools._get_avatars()
        return json.dumps(avatars)
