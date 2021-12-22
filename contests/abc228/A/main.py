#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: int, T: int, X: int):
    if S < T:
        if S <= X < T:
            print(YES)
        else:
            print(NO)
    else:
        if X < T or S <= X:
            print(YES)
        else:
            print(NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(S, T, X)


if __name__ == "__main__":
    main()
