.PHONY: generate clean

# Directory where the generated code will be output
GENERATED_DIR = gravatar_api_client

# The OpenAPI spec file
SPEC_FILE = openapi.yaml

# Docker image for OpenAPI Generator
DOCKER_IMAGE = openapitools/openapi-generator-cli

inspector:
	@npx @modelcontextprotocol/inspector uv run mcp-server-gravatar

# Target to generate the Python client using Docker
generate:
	@docker run --rm -v $(PWD):/local $(DOCKER_IMAGE) generate -i /local/$(SPEC_FILE) -g python -o /local/$(GENERATED_DIR)
	@mkdir -p src/openapi_client
	@rsync -a --delete $(GENERATED_DIR)/openapi_client/ src/openapi_client/

# Target to clean up generated files
clean:
	rm -rf $(GENERATED_DIR)