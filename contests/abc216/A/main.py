#!/usr/bin/env python3


def solve(X: int, Y: int):
    result = str(X)

    if 0 <= Y <= 2:
        result += "-"
    elif 7 <= Y <= 9:
        result += "+"

    print(result)


def main():
    # Failed to predict input format
    X, Y = [int(i) for i in input().split(".")]
    solve(X, Y)


if __name__ == "__main__":
    main()
