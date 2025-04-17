import httpx
import json
import os
from openapi_client import Configuration, ApiClient, ProfilesApi


class GravatarApiClient:
    """
    A client for interacting with the Gravatar API using the generated OpenAPI client.
    """

    def __init__(self, config_path: str):
        """
        Initialize the API client by loading access token from a JSON configuration file.

        Args:
            config_path (str): Path to JSON config file containing 'access_token'.
        """
        self.access_token = self._load_token(config_path)

    def get_profile_by_id(self, profile_id: str) -> dict:
        """
        Retrieve the Gravatar profile for a given profile id using the generated client.

        Args:
            profile_id (str): The identifier for the profile.

        Returns:
            dict: JSON response of the user's profile.
        """
        # Setup the configuration for the generated client
        config = Configuration()
        config.access_token = self.access_token
        # If necessary, you can set the host explicitly:
        # config.host = "https://api.gravatar.com/v3"

        # Create an instance of the generated ApiClient
        api_client = ApiClient(configuration=config)

        # Instantiate the ProfilesApi from the generated client
        api_instance = ProfilesApi(api_client)

        # Call the API to get the profile by ID
        profile = api_instance.get_profile_by_id(profile_id)
        return profile

    # Optionally, add more methods to wrap other API endpoints as needed.

    def _load_token(self, config_path: str) -> str:
        """
        Load access token from a JSON configuration file.
        """
        if not os.path.isfile(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")
        with open(config_path, 'r') as f:
            data = json.load(f)
        token = data.get('access_token') or data.get('token')
        if not token:
            raise ValueError("Missing 'access_token' in configuration file")
        return token
