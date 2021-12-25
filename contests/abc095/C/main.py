#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, X: int, Y: int):
    ans = float("inf")

    for ab in range(max(X, Y) * 2 + 1):
        cost = C * ab

        x = X - ab / 2
        y = Y - ab / 2

        if x > 0:
            cost += A * x
        if y > 0:
            cost += B * y

        ans = min(ans, int(cost))

    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(A, B, C, X, Y)


if __name__ == "__main__":
    main()
