#!/usr/bin/env python3
import sys


def main():
    print("=== Command Quest ===")
    arr = sys.argv
    print(f"Program name: {arr[0]}")
    if len(arr) > 1:
        print(f"Arguments received: {len(arr) - 1}")
        for i, arg in enumerate(arr[1:]):
            print(f"Argument {i + 1}: {arg}")
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(arr)}")


if __name__ == "__main__":
    main()
