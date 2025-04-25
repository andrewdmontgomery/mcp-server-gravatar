import json
from typing import overload, Literal, Union, Any, Protocol
from mcp.server.fastmcp import FastMCP, Context
from mcp.server.fastmcp.prompts.base import UserMessage


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
        field: Literal[
            "hash", "display_name", "profile_url", "avatar_url", "avatar_alt_text",
            "location", "description", "job_title", "company",
            "verified_accounts", "pronunciation", "pronouns", "timezone",
            "languages", "first_name", "last_name", "is_organization",
            "header_image", "background_color", "links", "interests", "payments",
            "contact_info", "gallery", "number_verified_accounts",
            "last_profile_edit", "registration_date"
        ]
    ) -> Union[str, bool, int, list[dict[str, Any]], dict[str, Any]]:
        """
        Fetch a specific field from a Gravatar profile by its SHA256 identifier.
        """
        profile = await self.get_profile_by_hash(profile_identifier)
        return profile.get(field)

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
        field: Literal[
            "hash", "display_name", "profile_url", "avatar_url", "avatar_alt_text",
            "location", "description", "job_title", "company",
            "pronunciation", "pronouns", "timezone", "first_name", "last_name",
            "header_image", "background_color", "links", "interests", "payments",
            "contact_info", "gallery", "number_verified_accounts",
            "last_profile_edit", "registration_date"
        ]
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
        @mcp.tool(
            name="get_profile_by_email",
            description="Fetch a profile using an email address"
        )
        async def get_profile_by_email(email: str) -> dict[str, Any]:
            return await self.get_profile_by_email(email)

        @mcp.tool(
            name="get_profile_by_hash",
            description="Fetch a profile using the profile identifier of an email address"
        )
        async def get_profile_by_hash(hash: str) -> dict[str, Any]:
            return await self.get_profile_by_hash(hash)

        @mcp.tool(
            name="get_profile_field_with_hash",
            description="Fetch a specific field from a Gravatar profile using a profile identifier."
        )
        async def get_profile_field_with_hash(
            profileIdentifier: str,
            field: Literal[
                "hash", "display_name", "profile_url", "avatar_url", "avatar_alt_text",
                "location", "description", "job_title", "company",
                "verified_accounts", "pronunciation", "pronouns", "timezone",
                "languages", "first_name", "last_name", "is_organization",
                "header_image", "background_color", "links", "interests", "payments",
                "contact_info", "gallery", "number_verified_accounts",
                "last_profile_edit", "registration_date"
            ]
        ) -> Union[str, bool, int, list[dict[str, Any]], dict[str, Any]]:
            return await self.get_profile_field_with_hash(profileIdentifier, field)

        @mcp.tool(
            name="get_profile_field_with_email",
            description="Fetch a specific field from a Gravatar profile using the profile identifier of an email address"
        )
        async def get_profile_field_with_email(
            email: str,
            field: Literal[
                "hash", "display_name", "profile_url", "avatar_url", "avatar_alt_text",
                "location", "description", "job_title", "company",
                "pronunciation", "pronouns", "timezone", "first_name", "last_name",
                "header_image", "background_color", "links", "interests", "payments",
                "contact_info", "gallery", "number_verified_accounts",
                "last_profile_edit", "registration_date"
            ]
        ) -> Union[str, bool, int, list[dict[str, Any]], dict[str, Any]]:
            return await self.get_profile_field_with_email(email, field)

    def register_resources(self, mcp: FastMCP):
        @mcp.resource(
            uri="profiles://profileIdentifier/{profileIdentifier}",
            name="Get Profile by ID",
            description="Returns a profile object as json",
            mime_type="application/json")
        async def get_profile(profileIdentifier: str) -> str:
            profile = await self.get_profile_by_hash(profileIdentifier)
            return json.dumps(profile)

        @mcp.resource(
            uri="profiles://email/{email}",
            name="Get Profile by email",
            description="Returns a profile object as json",
            mime_type="application/json")
        async def get_profile(email: str) -> str:
            profile = await self.get_profile_by_email(email)
            return json.dumps(profile)

    def register_prompts(self, mcp: FastMCP):
        @mcp.prompt()
        def summarize_gravatar_profile(email: str) -> str:
            """
            Prompt that instructs the model to summarize a Gravatar profile.
            """
            return [
                UserMessage(
                    f"You are an assistant that summarizes Gravatar profiles.  Use data from the profile at 'profiles://email/{email}'.  If the profile contains `verified_accounts`, visit the `url` for each account.  Include what you find there in your summary. "
                )
            ]
