#!/usr/bin/env python3

import sys
import typing


def ft_archive_creation(file_content: list[str]) -> None:
    try:
        new_file_name = input("Enter new file name (or empty): ")
        if not new_file_name:
            print("Not saving data.")
            sys.exit(0)
        print(f"\nSaving data to '{new_file_name}'")
        new_file: typing.IO = open(new_file_name, "w")
        new_file.writelines(file_content)
        new_file.close()
        print(f"Data saved in file '{new_file_name}'.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{new_file_name}': {e}")
        print("Data not saved.")
        sys.exit(1)


def read_and_transform(file_name: str) -> list[str]:
    transformed_content: list[str] = []
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.IO = open(file_name, "r")
        print("---\n")
        for line in file:
            print(line, end="")
            transformed_content.append(line.rstrip("\n") + "#\n")
        print("\n---")
        file.close()
        print(f"File '{file_name}' closed.")
        return transformed_content
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file_name}': {e}")
        sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)
    file_name = sys.argv[1]
    file_content = read_and_transform(file_name)
    print("Transform data:")
    print("---\n")
    for line in file_content:
        print(line, end="")
    print("\n---")
    ft_archive_creation(file_content)


if __name__ == "__main__":
    main()
