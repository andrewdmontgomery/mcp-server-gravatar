from mcp.server.fastmcp import FastMCP
from .tools.avatar_tools import AvatarTools
from .tools.profile_tools import ProfileTools
from .resources import register_resources
from . import gravatar_client

# Initialize FastMCP server
mcp = FastMCP("gravatar")
client = gravatar_client.client


def register_tools(mcp: FastMCP):
    ProfileTools(client=client).register_tools(mcp)
    AvatarTools(client=client).register_tools(mcp)


def serve():
    # Run the MCP server over stdio
    register_tools(mcp)
    register_resources(mcp)
    mcp.run(transport="stdio")
