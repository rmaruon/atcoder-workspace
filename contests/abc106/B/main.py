#!/usr/bin/env python3
import sys


def 奇数(n: int):
    return n % 2 == 1


def 約数の個数(n: int):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def 約数を8個持つ(n: int):
    return 約数の個数(n) == 8


def solve(N: int):
    count = 0
    for i in range(1, N + 1):
        if 奇数(i) and 約数を8個持つ(i):
            count += 1
    print(count)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == "__main__":
    main()
