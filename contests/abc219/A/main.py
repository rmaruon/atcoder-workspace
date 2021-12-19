#!/usr/bin/env python3
import sys


def solve(X: int):
    if 0 <= X < 40:
        print(40 - X)
    elif 40 <= X < 70:
        print(70 - X)
    elif 70 <= X < 90:
        print(90 - X)
    else:
        print("expert")
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)


if __name__ == "__main__":
    main()
