#!/usr/bin/env python3
import sys


def solve(N: int, A: int, X: int, Y: int):
    if N <= A:
        定価分 = X * N
        print(定価分)
    else:
        定価分 = X * A
        割引分 = Y * (N - A)
        print(定価分 + 割引分)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(N, A, X, Y)


if __name__ == "__main__":
    main()
