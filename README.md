# MCP Server for Gravatar

A stdio-based Model Context Protocol (MCP) server that provides access to Gravatar profile and avatar data. Clients (e.g., Claude Desktop, custom IDE plugins) can discover and invoke tools via MCP to fetch Gravatar profiles and avatars.

## Features

- Fetch Gravatar profile by email or SHA256 hash
- Retrieve specific profile fields
- List user avatars and fetch avatar image bytes
- Works over stdio for easy integration with MCP-aware clients

## Prerequisites

- Python 3.10 or later
- [uv](https://github.com/uvdevtool/uv) CLI tool installed (provides `uv sync` and `uv run`)
- (Optional) Docker, if you need to regenerate the OpenAPI client via `make generate`

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


## Regenerating the OpenAPI client
(if you’ve updated `openapi.yaml`)
> [!CAUTION]
> Regenerating the client will cause problems.  There are manual changes that have been applied to the generated code in order to fix issues.
> If you re-generate the openapi_client, those changes should be retained.  Ideally these changes would by applied as a post-generation step.

   ```bash
   make generate
   ```

   This runs the OpenAPI Generator Docker image and synchronizes the generated `gravatar_api_client/openapi_client` into `src/openapi_client`.

## Configuration

### Usage with Claude Desktop

Add this to your `claude_desktop_config.json`:

<details>
<summary>Using uvx</summary>

```json
"mcpServers": {
  "git": {
    "command": "uvx",
    "args": ["--from", "git+https://github.com/andrewdmontgomery/mcp-server-gravatar", "mcp-server-gravatar"]
  }
}
```

Or if you want to load a specific branch (e.g. `add/my-feature`):

```json
"mcpServers": {
  "git": {
    "command": "uvx",
    "args": ["--from", "git+https://github.com/andrewdmontgomery/mcp-server-gravatar@add/my-feature", "mcp-server-gravatar"]
  }
}
```

</details>

## Running the MCP Server

You can start the server directly:

```bash
# Run the MCP server
uv run mcp-server-gravatar
```

This can be helpful for debugging startup issues.

With `uvx`, you can also start the server from the repo:

```bash
uvx --from git+https://github.com/andrewdmontgomery/mcp-server-gravatar mcp-server-gravatar
```

You can specify a branch, too (e.g. `add/my-feature`):

```bash
uvx --from git+https://github.com/andrewdmontgomery/mcp-server-gravatar@add/my-feature mcp-server-gravatar
```


## Debugging with MCP Inspector

You can use the MCP Inspector to trace and debug prompt and tool executions. For example:

1. Run Inspector:
   ```bash
   make inspector
   ```
   
   Or manually:
   ```bash
   npx @modelcontextprotocol/inspector uv run mcp-server-gravatar
   Starting MCP inspector...
   ⚙️ Proxy server listening on port 6277
   🔍 MCP Inspector is up and running at http://127.0.0.1:6274
   ```
3. Open the Inspector UI in your browser
   - In the example above: `http://localhost:6274`.

For more details, see the official docs:  
https://modelcontextprotocol.io/docs/tools/inspector


## Makefile Targets

- `make generate` — regenerate and sync the OpenAPI client
- `make clean`    — remove generated client files

## Environment Variables

- `GRAVATAR_API_TOKEN` — your Gravatar API key

---
