import os
import json
import hashlib
from typing import Optional
from openapi_client import Configuration, ApiClient
from openapi_client.api.profiles_api import ProfilesApi
from openapi_client.api.avatars_api import AvatarsApi

GRAVATAR_API_TOKEN = os.environ.get("GRAVATAR_API_TOKEN")
USER_AGENT = "gravatar-mcp/1.0"


class GravatarClient:
    """
    Encapsulates configuration, authentication, and API clients for Gravatar.
    """

    def __init__(self):
        # Configure API client
        config = Configuration()
        config.access_token = GRAVATAR_API_TOKEN

        self._api_client = ApiClient(configuration=config)
        self._api_client.user_agent = USER_AGENT

        self.profiles_api = ProfilesApi(self._api_client)
        self.avatars_api = AvatarsApi(self._api_client)

    @staticmethod
    def hash_email(email: str) -> str:
        """
        Normalize an email address and return its SHA256 hash.
        """
        normalized = email.strip().lower()
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


# Singleton client instance for convenience
client = GravatarClient()
