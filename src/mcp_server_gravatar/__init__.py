import click
from .gravatar import serve


@click.command()
def main():
    """Run the Gravatar MCP server."""
    serve()


if __name__ == "__main__":
    print("Calling main()...")
    main()
