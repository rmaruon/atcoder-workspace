#!/usr/bin/env python3
import sys


def solve(D: int):
    ans = D / 100
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    D = int(next(tokens))  # type: int
    solve(D)


if __name__ == "__main__":
    main()
