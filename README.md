# MCP Server for Gravatar

A stdio-based Model Context Protocol (MCP) server that provides access to Gravatar profile and avatar data. Clients (e.g., Claude Desktop, custom IDE plugins) can discover and invoke tools via MCP to fetch Gravatar profiles and avatars.

## Features

- Fetch Gravatar profile by email or SHA256 hash
- Retrieve specific profile fields
- List user avatars and fetch avatar image bytes
- Works over stdio for easy integration with MCP-aware clients
- Uses FastMCP's native OpenAPI support for direct integration with the Gravatar API

## Prerequisites

- Python 3.10 or later
- [uv](https://github.com/uvdevtool/uv) CLI tool installed (provides `uv sync` and `uv run`)

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/andrewdmontgomery/mcp-server-gravatar.git
   cd mcp-server-gravatar
   ```

2. **Install dependencies**

   ```bash
   uv sync
   ```

   This will install all Python dependencies specified in `pyproject.toml` into your active virtual environment.

## Configuration

### Usage with Claude Desktop

Add this to your `claude_desktop_config.json`:

<details>
<summary>Using uvx</summary>

```json
"mcpServers": {
  "git": {
    "command": "uvx",
    "args": ["--from", "git+https://github.com/andrewdmontgomery/mcp-server-gravatar", "mcp-server-git"]
  }
}
```
</details>

## Running the MCP Server

You can start the server directly as a module:

```bash
# Run the MCP server
uv run -m mcp_server_gravatar
```

## Architecture

This MCP server uses FastMCP's native OpenAPI support to automatically generate MCP components from the Gravatar API OpenAPI specification. The key components are:

1. **OpenAPI Integration**: The server loads the OpenAPI spec (`openapi.yaml`) and uses FastMCP's `from_openapi()` method to automatically generate MCP tools and resources.

2. **Custom Tools**: Additional custom tools are provided for functionality not directly covered by the OpenAPI spec, such as image conversion and specialized queries.

3. **Prompts**: The server includes prompts for common tasks like summarizing Gravatar profiles.

## Debugging with MCP Inspector

You can use the MCP Inspector to trace and debug prompt and tool executions. For example:

1. Run Inspector:
   ```bash
   npx @modelcontextprotocol/inspector uv run mcp-server-gravatar
   Starting MCP inspector...
   ⚙️ Proxy server listening on port 6277
   🔍 MCP Inspector is up and running at http://127.0.0.1:6274
   ```
2. Open the Inspector UI in your browser
   - In the example above: `http://localhost:6274`.

For more details, see the official docs:  
https://modelcontextprotocol.io/docs/tools/inspector

## Environment Variables

- `GRAVATAR_API_TOKEN` — your Gravatar API key

---
