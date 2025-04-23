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

3. **Generate the OpenAPI client** (if you’ve updated `openapi.yaml`)

   ```bash
   make generate
   ```

   This runs the OpenAPI Generator Docker image and synchronizes the generated `openapi_client` into `src/openapi_client`.

4. **Configure access token**

   Create a `config.json` in the project root (or set the `GRAVATAR_CONFIG_PATH` environment variable) with your Gravatar API token:

   ```json
   {
     "access_token": "YOUR_GRAVATAR_API_TOKEN"
   }
   ```

## Running the MCP Server

You can start the server directly as a module:

```bash
# Ensure src/ is on PYTHONPATH
export PYTHONPATH="$PWD/src"

# Run the MCP server
uv run -m mcp_server_gravatar
```

Or, after installation, use the console script:

```bash
pip install -e .
mcp-server-gravatar
```

The server will listen on stdio and respond to MCP `list_tools` and `call_tool` requests.

## Testing

Run the unit tests with:

```bash
uv run pytest -q
```

## Makefile Targets

- `make generate` — regenerate and sync the OpenAPI client
- `make clean`    — remove generated client files

## Environment Variables

- `GRAVATAR_CONFIG_PATH` — path to your `config.json` (default: `./config.json`)

---

© 2025 Andrew Montgomery. Licensed under MIT.
