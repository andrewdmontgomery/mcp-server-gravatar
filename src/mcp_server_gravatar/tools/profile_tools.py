from typing import overload, Literal, Union, Any
from mcp.server.fastmcp import FastMCP


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
        profile = self.client.profiles_api.get_profile_by_id(profile_id)
        if hasattr(profile, "to_dict"):
            return profile.to_dict()
        return profile

    async def get_profile_by_hash(self, hash: str) -> dict[str, Any]:
        """
        Fetch Gravatar profile for a given SHA256 hash.
        """
        profile = self.client.profiles_api.get_profile_by_id(hash)
        if hasattr(profile, "to_dict"):
            return profile.to_dict()
        return profile

    @overload
    async def get_profile_field_with_hash(
        self,
        profileIdentifier: str,
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
        profileIdentifier: str,
        field: Literal["is_organization"]
    ) -> bool: ...

    @overload
    async def get_profile_field_with_hash(
        self,
        profileIdentifier: str,
        field: Literal["number_verified_accounts"]
    ) -> int: ...

    @overload
    async def get_profile_field_with_hash(
        self,
        profileIdentifier: str,
        field: Literal["verified_accounts", "languages",
                       "links", "interests", "gallery"]
    ) -> list[dict[str, Any]]: ...

    @overload
    async def get_profile_field_with_hash(
        self,
        profileIdentifier: str,
        field: Literal["payments", "contact_info"]
    ) -> dict[str, Any]: ...

    async def get_profile_field_with_hash(
        self,
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
        """
        Fetch a specific field from a Gravatar profile by its SHA256 identifier.
        """
        profile = await self.get_profile_by_hash(profileIdentifier)
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
        profile_hash = self.client.hash_email(email)
        return await self.get_profile_field_with_hash(profile_hash, field)

    def register_tools(self, mcp: FastMCP):
        """
        Register all profile-related tools with the MCP server.
        """
        @mcp.tool(name="get_profile_by_email")
        async def get_profile_by_email(email: str) -> dict[str, Any]:
            return await self.get_profile_by_email(email)

        @mcp.tool(name="get_profile_by_hash")
        async def get_profile_by_hash(hash: str) -> dict[str, Any]:
            return await self.get_profile_by_hash(hash)

        @mcp.tool(
            name="get_profile_field_with_hash",
            description="Fetch a specific field from a Gravatar profile by its SHA256 identifier."
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
            description="Fetch a specific field from a Gravatar profile by email address."
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
