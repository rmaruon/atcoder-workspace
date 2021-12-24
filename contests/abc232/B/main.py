#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def _next(char):
    if char == "z":
        return "a"

    return chr(ord(char) + 1)


def solve(S: str, T: str):
    for _ in range(26):
        if S == T:
            print(YES)
            return
        S = "".join([_next(char) for char in S])
    print(NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(S, T)


if __name__ == "__main__":
    main()
