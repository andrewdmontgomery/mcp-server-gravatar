import os
import json
import hashlib
from typing import Optional
from openapi_client import Configuration, ApiClient
from openapi_client.api.profiles_api import ProfilesApi
from openapi_client.api.avatars_api import AvatarsApi

CONFIG_PATH = os.environ.get("GRAVATAR_CONFIG_PATH", "config.json")
USER_AGENT = "gravatar-mcp/1.0"


class GravatarClient:
    """
    Encapsulates configuration, authentication, and API clients for Gravatar.
    """

    def __init__(self, config_path: Optional[str] = None):
        path = config_path or CONFIG_PATH
        token = self._load_token(path)

        # Configure API client
        config = Configuration()
        config.access_token = token

        self._api_client = ApiClient(configuration=config)
        self._api_client.user_agent = USER_AGENT

        self.profiles_api = ProfilesApi(self._api_client)
        self.avatars_api = AvatarsApi(self._api_client)

    @staticmethod
    def _load_token(path: str) -> str:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Config file not found: {path}")
        with open(path, 'r') as f:
            data = json.load(f)
        token = data.get("access_token") or data.get("token")
        if not token:
            raise ValueError("Missing 'access_token' in configuration file")
        return token

    @staticmethod
    def hash_email(email: str) -> str:
        """
        Normalize an email address and return its SHA256 hash.
        """
        normalized = email.strip().lower()
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


# Singleton client instance for convenience
client = GravatarClient()
