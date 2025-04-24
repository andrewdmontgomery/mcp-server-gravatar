from mcp.server.fastmcp import FastMCP
from .tools import profile_tools
from .tools.avatar_tools import AvatarTools
from .resources import register_resources
from . import gravatar_client

# Initialize FastMCP server
mcp = FastMCP("gravatar")
client = gravatar_client.client
avatar_tools = AvatarTools(client=client)


def register_tools(mcp: FastMCP):
    profile_tools.register_tools(mcp)
    avatar_tools.register_tools(mcp)


def serve():
    # Run the MCP server over stdio
    register_tools(mcp)
    register_resources(mcp)
    mcp.run(transport="stdio")
