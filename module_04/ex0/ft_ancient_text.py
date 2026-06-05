#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)

    file_name = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")

    try:
        file: typing.IO = open(file_name, "r")
        print("---\n")
        for line in file:
            print(line, end="")
        print("\n---")
        file.close()
        print(f"File '{file_name}' closed.")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file_name}': {e}")


if __name__ == "__main__":
    main()
