#!/usr/bin/env python3
import sys


def pinの並びが存在する(pin: str, s: int):
    for c in pin:
        idx = s.find(c)

        if idx == -1:
            return False

        s = s[slice(idx + 1, None)]

    return True


def solve(N: int, S: str):
    count = 0
    for i in range(1000):
        pin = f"{i:03}"
        if pinの並びが存在する(pin, S):
            count += 1

    print(count)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == "__main__":
    main()
