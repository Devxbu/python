#!/usr/bin/env python3
import sys


def input_validation(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def calculate_analytics(arr):
    print(f"Scores processed: {arr}")
    print(f"Total players: {len(arr)}")
    print(f"Total score: {sum(arr)}")
    print(f"Average score: {sum(arr) / len(arr):.1f}")
    print(f"High score: {max(arr)}")
    print(f"Low score: {min(arr)}")
    print(f"Score range: {max(arr) - min(arr)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    arr = sys.argv[1:]
    int_arr = []
    for arg in arr:
        if input_validation(arg):
            int_arr.append(int(arg))
        else:
            print(f"Invalid parameter: '{arg}'")
    if len(int_arr) > 0:
        calculate_analytics(int_arr)
    else:
        print("No scores provided.", end=" ")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
