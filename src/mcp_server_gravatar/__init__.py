import click
from .gravatar import serve


@click.command()
def main():
    import asyncio

    asyncio.run(serve())


if __name__ == "__main__":
    print("Calling main()...")
    main()
