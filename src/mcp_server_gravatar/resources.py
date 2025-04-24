import json
from mcp.server.fastmcp import FastMCP
from .tools import profile_tools, avatar_tools


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

    @mcp.resource(
        uri="avatars://me",
        name="List Avatars",
        description="Returns a list of avatars",
        mime_type="application/json")
    async def get_avatars() -> str:
        avatars = await avatar_tools._get_avatars()
        return json.dumps(avatars)

    @mcp.resource(
        uri="avatars://me/{selected_email_hash}",
        name="List Avatars showing selected",
        description="Returns a list of avatars",
        mime_type="application/json")
    async def get_avatars(selected_email_hash: str) -> str:
        avatars = await avatar_tools._get_avatars(selected_email_hash=selected_email_hash)
        return json.dumps(avatars)
