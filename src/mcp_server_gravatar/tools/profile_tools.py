from __future__ import annotations
from enum import Enum
import json
import httpx
from typing import overload, Literal, Union, Any, Protocol
from fastmcp import FastMCP, Context
from fastmcp.prompts import Message, UserMessage


class ProfileField(Enum):
    hash = "hash"
    display_name = "display_name"
    profile_url = "profile_url"
    avatar_url = "avatar_url"
    avatar_alt_text = "avatar_alt_text"
    location = "location"
    description = "description"
    job_title = "job_title"
    company = "company"
    verified_accounts = "verified_accounts"
    pronunciation = "pronunciation"
    pronouns = "pronouns"
    timezone = "timezone"
    languages = "languages"
    first_name = "first_name"
    last_name = "last_name"
    is_organization = "is_organization"
    header_image = "header_image"
    background_color = "background_color"
    links = "links"
    interests = "interests"
    payments = "payments"
    contact_info = "contact_info"
    gallery = "gallery"
    number_verified_accounts = "number_verified_accounts"
    last_profile_edit = "last_profile_edit"
    registration_date = "registration_date"


class ProfileTools:

    def __init__(self, client):
        """
        Initialize with a Gravatar API client.
        """
        self.client = client

    async def get_profile_by_email(self, email: str) -> dict[str, Any]:
        """
        Fetch Gravatar profile for a given email address.
        """
        profile_id = self.client.hash_email(email)
        profile = self.client.get_profile_by_id(profile_id)
        if hasattr(profile, "to_dict"):
            return profile.to_dict()
        return profile

    async def get_profile_by_hash(self, hash: str) -> dict[str, Any]:
        """
        Fetch Gravatar profile for a given SHA256 hash.
        """
        profile = self.client.get_profile_by_id(hash)
        if hasattr(profile, "to_dict"):
            return profile.to_dict()
        return profile

    @overload
    async def get_profile_field_with_hash(
        self,
        profile_identifier: str,
        field: Literal[
            "hash", "display_name", "profile_url", "avatar_url", "avatar_alt_text",
            "location", "description", "job_title", "company",
            "pronunciation", "pronouns", "timezone", "first_name", "last_name",
            "header_image", "background_color", "last_profile_edit", "registration_date"
        ]
    ) -> str: ...

    @overload
    async def get_profile_field_with_hash(
        self,
        profile_identifier: str,
        field: Literal["is_organization"]
    ) -> bool: ...

    @overload
    async def get_profile_field_with_hash(
        self,
        profile_identifier: str,
        field: Literal["number_verified_accounts"]
    ) -> int: ...

    @overload
    async def get_profile_field_with_hash(
        self,
        profile_identifier: str,
        field: Literal["verified_accounts", "languages",
                       "links", "interests", "gallery"]
    ) -> list[dict[str, Any]]: ...

    @overload
    async def get_profile_field_with_hash(
        self,
        profile_identifier: str,
        field: Literal["payments", "contact_info"]
    ) -> dict[str, Any]: ...

    async def get_profile_field_with_hash(
        self,
        profile_identifier: str,
        field: ProfileField
    ) -> Union[str, bool, int, list[dict[str, Any]], dict[str, Any]]:
        """
        Fetch a specific field from a Gravatar profile by its SHA256 identifier.
        """
        profile = await self.get_profile_by_hash(profile_identifier)
        return profile.get(field.value)

    @overload
    async def get_profile_field_with_email(
        self,
        email: str,
        field: Literal[
            "hash", "display_name", "profile_url", "avatar_url", "avatar_alt_text",
            "location", "description", "job_title", "company",
            "pronunciation", "pronouns", "timezone", "first_name", "last_name",
            "header_image", "background_color", "last_profile_edit", "registration_date"
        ]
    ) -> str: ...

    @overload
    async def get_profile_field_with_email(
        self,
        email: str,
        field: Literal["is_organization"]
    ) -> bool: ...

    @overload
    async def get_profile_field_with_email(
        self,
        email: str,
        field: Literal["number_verified_accounts"]
    ) -> int: ...

    @overload
    async def get_profile_field_with_email(
        self,
        email: str,
        field: Literal["verified_accounts", "languages",
                       "links", "interests", "gallery"]
    ) -> list[dict[str, Any]]: ...

    @overload
    async def get_profile_field_with_email(
        self,
        email: str,
        field: Literal["payments", "contact_info"]
    ) -> dict[str, Any]: ...

    async def get_profile_field_with_email(
        self,
        email: str,
        field: ProfileField
    ) -> Union[str, bool, int, list[dict[str, Any]], dict[str, Any]]:
        """
        Fetch a specific field from a Gravatar profile by email address.
        """
        profile_identifier = self.client.hash_email(email)
        return await self.get_profile_field_with_hash(profile_identifier, field)

    def register_tools(self, mcp: FastMCP):
        """
        Register all profile-related tools with the MCP server.
        """

    def register_resources(self, mcp: FastMCP):
        @mcp.resource(
            uri="profiles://profileIdentifier/{profileIdentifier}",
            mime_type="application/json"
        )
        async def get_profile_by_id(profileIdentifier: str) -> str:
            """
            Returns a profile object as JSON.
            """
            profile = await self.get_profile_by_hash(profileIdentifier)
            return json.dumps(profile)

        @mcp.resource(
            uri="profiles://email/{email}",
            mime_type="application/json"
        )
        async def get_profile_by_email(email: str) -> str:
            """
            Returns a profile object as JSON.
            """
            profile = await self.get_profile_by_email(email)
            return json.dumps(profile)

        @mcp.resource(
            uri="profiles://profileIdentifier/{profileIdentifier}/field/{field}",
            mime_type="application/json"
        )
        async def get_profile_field_by_id(profileIdentifier: str, field: str) -> str:
            """
            Returns a profile object as JSON.
            """
            profile = await self.get_profile_field_with_hash(profile_identifier=profileIdentifier, field=ProfileField(field))
            return json.dumps(profile)

        @mcp.resource(
            uri="profiles://email/{email}/field/{field}",
            mime_type="application/json"
        )
        async def get_profile_field_by_email(email: str, field: str) -> str:
            """
            Returns a profile object as JSON.
            """
            profile = await self.get_profile_field_with_email(email=email, field=ProfileField(field))
            return json.dumps(profile)

    def register_prompts(self, mcp: FastMCP):

        @mcp.prompt()
        async def summarize_gravatar_profile(email: str, ctx: Context) -> list[Message]:
            """
            Read a Gravatar profile via MCP resource and summarize it
            """
            # Log the start of the prompt execution
            await ctx.debug(f"summarize_gravatar_profile called with email={email}")

            # Read the profile JSON from the MCP resource
            contents = await ctx.read_resource(f"profiles://email/{email}")
            if not contents:
                await ctx.error(f"No profile found for email {email}")
                profile_json = "{}"
            else:
                profile_json = contents[0].content

            profile_data = json.loads(profile_json)
            # Build messages for the model
            return [
                UserMessage(
                    f"You are a professional assistant skilled at writing concise, engaging summaries of user profiles.\n\n"
                    f"Here is the profile JSON data:\n{profile_data}\n\n"
                    f"Next, extract the fields display_name, location, description, job_title, company, timezone, languages, interests, and verified_accounts.\n"
                    f"Finally, produce a one- to two-paragraph professional summary, using natural, flowing sentences without bullet points."
                )
            ]

        @mcp.prompt()
        async def summarize_gravatar_profile_via_tool(email: str) -> list[Message]:
            """
            Read a Gravatar profile using the get_profile tool and summarize it
            """
            return [
                UserMessage(
                    f"You are a professional assistant skilled at writing concise, engaging summaries of user profiles.\n\n"
                    f"First, call the get_profile_by_email tool with argument email='{email}' to fetch the raw profile JSON.\n"
                    f"Next, extract the fields display_name, location, description, job_title, company, timezone, languages, interests, and verified_accounts.\n"
                    f"Finally, produce a one- to two-paragraph professional summary, using natural, flowing sentences without bullet points."
                ),
            ]
