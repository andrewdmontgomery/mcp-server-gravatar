import os
import pathlib
from fastmcp import FastMCP
from fastmcp.server.openapi import RouteMap, RouteType
import httpx
import yaml
import anyio

# Initialize FastMCP server


def create_mcp_server():
    # Get the path to the OpenAPI spec file
    current_dir = pathlib.Path(__file__).parent.parent.parent
    openapi_path = current_dir / "openapi.yaml"

    # Load OpenAPI spec as a dictionary
    with open(openapi_path, "r") as f:
        openapi_spec = yaml.safe_load(f)

    # Authentication setup
    GRAVATAR_API_TOKEN = os.environ.get("GRAVATAR_API_TOKEN")
    USER_AGENT = "gravatar-mcp/1.0"

    # Create authenticated client
    api_client = httpx.AsyncClient(
        verify=False,
        base_url="https://api.gravatar.com/v3",
        headers={
            "Authorization": f"Bearer {GRAVATAR_API_TOKEN}",
            "User-Agent": USER_AGENT
        }
    )

    # Create custom maps
    custom_maps = [
        # FastMCP doesn't support creating RESOURCE_TEMPLATE from an endpoint with query parameters
        RouteMap(methods=["GET"],
                 pattern=r"^/me/associated-email",
                 route_type=RouteType.TOOL),
    ]

    # Initialize FastMCP server with OpenAPI support
    mcp = FastMCP.from_openapi(
        openapi_spec=openapi_spec,
        client=api_client,
        route_maps=custom_maps,
        log_level="DEBUG"
    )

    return mcp


def serve():
    """
    Run the MCP server.
    """
    mcp = create_mcp_server()
    mcp.run()
