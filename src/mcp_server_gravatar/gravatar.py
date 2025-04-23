from mcp.server.fastmcp import FastMCP
from .tools import profile_tools, avatar_tools

# Initialize FastMCP server
mcp = FastMCP("gravatar")


def register_tools(mcp: FastMCP):
    profile_tools.register_tools(mcp)
    avatar_tools.register_tools(mcp)


def serve():
    # Run the MCP server over stdio
    register_tools(mcp)
    mcp.run(transport="stdio")
