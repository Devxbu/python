#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")
    arr = sys.argv
    print(f"Program name: {arr[0]}")
    if len(arr) > 1:
        print(f"Arguments received: {len(arr) - 1}")
        i = 1
        while i < len(arr):
            print(f"Argument {i}: {arr[i]}")
            i += 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(arr)}")


if __name__ == "__main__":
    main()
