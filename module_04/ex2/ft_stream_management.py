#!/usr/bin/env python3

import sys
import typing


def read_file(file_name: str) -> list[str]:
    content: list[str] = []

    try:
        sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
        sys.stdout.write(f"Accessing file '{file_name}'\n")

        with open(file_name, "r") as f:
            sys.stdout.write("---\n\n")
            for line in f:
                sys.stdout.write(line)
                content.append(line.rstrip("\n") + "#\n")
            sys.stdout.write("\n\n---\n")

        sys.stdout.write(f"File '{file_name}' closed.\n\n")
        return content

    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file_name}': {e}\n")
        sys.exit(1)


def save_file(content: list[str]) -> None:
    try:
        sys.stdout.write("Transform data:\n")
        sys.stdout.write("---\n\n")
        for line in content:
            sys.stdout.write(line)
        sys.stdout.write("\n---\n")

        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()

        new_file = sys.stdin.readline().strip()

        if new_file == "":
            sys.stdout.write("Not saving data\n")
            sys.exit(0)

        sys.stdout.write(f"Saving data to '{new_file}'\n")

        with open(new_file, "w") as f:
            f.writelines(content)

        sys.stdout.write(f"Data saved in file '{new_file}'\n")

    except (FileNotFoundError, PermissionError, OSError) as e:
        sys.stderr.write(f"[STDERR] Error opening file '{new_file}': {e}\n")
        sys.stdout.write("Data not saved.\n")
        sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        sys.stderr.write("[STDERR] Usage: ft_stream_management.py <file>\n")
        sys.exit(1)

    file_name = sys.argv[1]
    content = read_file(file_name)
    save_file(content)


if __name__ == "__main__":
    main()
