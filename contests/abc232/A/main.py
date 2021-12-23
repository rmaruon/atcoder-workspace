#!/usr/bin/env python3
import sys


def solve(S: str):
    ans = int(S[0]) * int(S[2])
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == "__main__":
    main()
