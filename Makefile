.PHONY: generate clean

# Directory where the generated code will be output
GENERATED_DIR = gravatar_client

# The OpenAPI spec file
SPEC_FILE = openapi.yaml

# Docker image for OpenAPI Generator
DOCKER_IMAGE = openapitools/openapi-generator-cli

# Target to generate the Python client using Docker
generate:
	docker run --rm -v $(PWD):/local $(DOCKER_IMAGE) generate -i /local/$(SPEC_FILE) -g python -o /local/$(GENERATED_DIR)

# Target to clean up generated files
clean:
	rm -rf $(GENERATED_DIR)