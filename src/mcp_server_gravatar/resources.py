import json
from mcp.server.fastmcp import FastMCP
from .tools import profile_tools


def register_resources(mcp: FastMCP):
    @mcp.resource(
        uri="profiles://profileIdentifier/{profileIdentifier}",
        name="Get Profile by ID",
        description="Returns a profile object as json",
        mime_type="application/json")
    async def get_profile(profileIdentifier: str) -> str:
        profile = await profile_tools._get_profile_by_hash(profileIdentifier)
        return json.dumps(profile)

    @mcp.resource(
        uri="profiles://email/{email}",
        name="Get Profile by email",
        description="Returns a profile object as json",
        mime_type="application/json")
    async def get_profile(email: str) -> str:
        profile = await profile_tools._get_profile_by_email(email)
        return json.dumps(profile)
