#!/usr/bin/env python3
import sys
import math


def solve(N: int):
    税込金額 = math.floor(N * 1.08)
    if 税込金額 < 206:
        print("Yay!")
    elif 税込金額 == 206:
        print("so-so")
    else:
        print(":(")


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
