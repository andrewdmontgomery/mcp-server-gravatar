#!/usr/bin/env python3
import argparse
import asyncio
import os

from gravatar import (
    get_profile_by_email,
    get_profile_by_hash,
    get_avatars,
    get_selected_avatar_as_image,
    _hash_email,
    get_profile_field,
)

# Ensure config path is set
os.environ.setdefault("GRAVATAR_CONFIG_PATH", "config.json")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Test Gravatar MCP tool functions"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    sp = subparsers.add_parser(
        "get_profile_by_email", help="Fetch profile by email")
    sp.add_argument("--email", required=True, help="User's email address")

    sp = subparsers.add_parser(
        "get_profile_by_hash", help="Fetch profile by hash")
    sp.add_argument("--hash", required=True, help="SHA256 hash of the email")

    sp = subparsers.add_parser("get_avatars", help="List avatars")
    group = sp.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--selected_email_hash",
        help="SHA256 hash of an email to mark selected avatar",
    )
    group.add_argument(
        "--selected_email",
        help="User's email address to hash and mark selected avatar",
    )

    sp = subparsers.add_parser(
        "get_selected_avatar_as_image",
        help="Fetch the selected avatar image for an email",
    )
    sp.add_argument("--email", required=True, help="User's email address")

    sp = subparsers.add_parser(
        "get_profile_field", help="Fetch a single field from a profile"
    )
    sp.add_argument(
        "--profileIdentifier", required=True,
        help="SHA256 hash of the profile identifier"
    )
    sp.add_argument(
        "--field", required=True,
        help="Name of the profile field to return"
    )

    return parser


async def run_command(args: argparse.Namespace):
    cmd = args.command
    if cmd == "get_profile_by_email":
        return await get_profile_by_email(args.email)
    elif cmd == "get_profile_by_hash":
        return await get_profile_by_hash(args.hash)
    elif cmd == "get_avatars":
        if args.selected_email:
            hash_val = _hash_email(args.selected_email)
        else:
            hash_val = args.selected_email_hash
        print(f"Hash: {hash_val}")
        return await get_avatars(selected_email_hash=hash_val)
    elif cmd == "get_selected_avatar_as_image":
        return await get_selected_avatar_as_image(args.email)
    elif cmd == "get_profile_field":
        return await get_profile_field(args.profileIdentifier, args.field)
    else:
        raise ValueError(f"Unknown command: {cmd}")


async def main():
    parser = build_parser()
    args = parser.parse_args()
    result = await run_command(args)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
