#!/usr/bin/env python3
import sys


def solve(S: str):
    ANSWER = "Hello,World!"

    if S == ANSWER:
        print("AC")
    else:
        print("WA")


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
