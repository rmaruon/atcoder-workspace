#!/usr/bin/env python3
import sys
from typing import List
import itertools


def 条件を満たすパスが存在する(paths, ab):
    for path in paths:
        path = tuple(sorted(path))
        if path not in ab:
            return False
    return True


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    ab = tuple(zip(a, b))
    count = 0

    for pattern in itertools.permutations(range(1, N + 1)):
        if pattern[0] != 1:
            continue

        paths = tuple(zip(pattern, pattern[1:]))
        if 条件を満たすパスが存在する(paths, ab):
            count += 1

    print(count)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)


if __name__ == "__main__":
    main()
