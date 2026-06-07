#!/usr/bin/env python3
import sys


def input_validation(s: str) -> bool:
    for ch in s:
        if ch < "0" or ch > "9":
            return False
    return len(s) > 0


def to_int(c: str) -> int:
    if c == "0":
        return 0
    if c == "1":
        return 1
    if c == "2":
        return 2
    if c == "3":
        return 3
    if c == "4":
        return 4
    if c == "5":
        return 5
    if c == "6":
        return 6
    if c == "7":
        return 7
    if c == "8":
        return 8
    if c == "9":
        return 9
    raise ValueError


def calculate_analytics(arr: list[int]) -> None:
    print(f"Scores processed: {arr}")
    print(f"Total players: {len(arr)}")
    print(f"Total score: {sum(arr)}")
    print(f"Average score: {sum(arr) / len(arr):.1f}")
    print(f"High score: {max(arr)}")
    print(f"Low score: {min(arr)}")
    print(f"Score range: {max(arr) - min(arr)}")


def main() -> None:
    print("=== Player Score Analytics ===")
    arr = sys.argv[1:]
    int_arr: list[int] = []

    for arg in arr:
        if input_validation(arg):
            int_arr = int_arr + [to_int(arg)]
        else:
            print(f"Invalid parameter: '{arg}'")

    if len(int_arr) > 0:
        calculate_analytics(int_arr)
    else:
        print("No scores provided.", end=" ")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
