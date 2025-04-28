from fastmcp import FastMCP
from .tools.avatar_tools import AvatarTools
from .tools.profile_tools import ProfileTools
from . import gravatar_client

# Initialize FastMCP server
mcp = FastMCP("gravatar")
client = gravatar_client.client
profile_tools = ProfileTools(client=client)
avatar_tools = AvatarTools(client=client)


def register_tools(mcp: FastMCP):
    profile_tools.register_tools(mcp)
    avatar_tools.register_tools(mcp)


def register_resources(mcp: FastMCP):
    profile_tools.register_resources(mcp)
    avatar_tools.register_resources(mcp)


def register_prompts(mcp: FastMCP):
    profile_tools.register_prompts(mcp)


def serve():
    # Run the MCP server over stdio
    register_tools(mcp)
    register_resources(mcp)
    register_prompts(mcp)
    mcp.run(transport="stdio")
