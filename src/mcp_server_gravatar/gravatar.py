import httpx
from typing import overload, Literal, Union, Any

from mcp.server.fastmcp import FastMCP
from openapi_client.models.profile import Profile

from .gravatar_client import client

# Initialize FastMCP server
mcp = FastMCP("gravatar")


@mcp.tool(name="get_profile_by_email")
async def get_profile_by_email(email: str) -> dict[str, Any]:
    """
    Fetch Gravatar profile for a given email address.

    Args:
        email: User's email address.

    Returns:
        dict[str, Any]: The JSON-deserialized Gravatar profile object.
    """
    profile_id = client.hash_email(email)

    # Fetch the profile using the raw ProfilesApi client
    profile = client.profiles_api.get_profile_by_id(profile_id)

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
    profile = client.profiles_api.get_profile_by_id(hash)
    if hasattr(profile, "to_dict"):
        return profile.to_dict()
    return profile


# Type-safe overloads for get_profile_field_with_hash
@overload
async def get_profile_field_with_hash(
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
    profileIdentifier: str,
    field: Literal["is_organization"]
) -> bool: ...


@overload
async def get_profile_field_with_hash(
    profileIdentifier: str,
    field: Literal["number_verified_accounts"]
) -> int: ...


@overload
async def get_profile_field_with_hash(
    profileIdentifier: str,
    field: Literal["verified_accounts", "languages",
                   "links", "interests", "gallery"]
) -> list[dict[str, Any]]: ...


@overload
async def get_profile_field_with_hash(
    profileIdentifier: str,
    field: Literal["payments", "contact_info"]
) -> dict[str, Any]: ...

# Actual tool implementation


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
    """
    Fetch a specific field from a Gravatar profile by its SHA256 identifier.
    Returns a type-safe union based on the requested field.
    """
    profile = await get_profile_by_hash(profileIdentifier)

    # Return the field value or None for optional fields without error
    return profile.get(field)


# Type-safe overloads for get_profile_field_with_email
@overload
async def get_profile_field_with_email(
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
    email: str,
    field: Literal["is_organization"]
) -> bool: ...


@overload
async def get_profile_field_with_email(
    email: str,
    field: Literal["number_verified_accounts"]
) -> int: ...


@overload
async def get_profile_field_with_email(
    email: str,
    field: Literal["verified_accounts", "languages",
                   "links", "interests", "gallery"]
) -> list[dict[str, Any]]: ...


@overload
async def get_profile_field_with_email(
    email: str,
    field: Literal["payments", "contact_info"]
) -> dict[str, Any]: ...


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
    """
    Fetch a specific field from a Gravatar profile by email address.
    """
    profile_hash = client.hash_email(email)
    return await get_profile_field_with_hash(profile_hash, field)


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
