#!/usr/bin/env python3
import itertools


def 正直者の証言に矛盾はない(pattern, 正直者の証言):
    for 証言リスト in 正直者の証言:
        for 証言 in 証言リスト:
            x, y = 証言
            if pattern[x - 1] != y:
                return False

    return True


def solve(N, 証言):
    正直者の最大人数 = 0

    for pattern in itertools.product([0, 1], repeat=N):
        正直者の証言 = [証言リスト for i, 証言リスト in enumerate(証言) if pattern[i] == 1]
        if not 正直者の証言:
            continue

        if 正直者の証言に矛盾はない(pattern, 正直者の証言):
            正直者の人数 = sum(pattern)
            正直者の最大人数 = max(正直者の最大人数, 正直者の人数)

    print(正直者の最大人数)


def main():
    N = int(input())

    証言 = []
    for _ in range(N):
        証言数 = int(input())
        証言.append([list(map(int, input().split())) for _ in range(証言数)])

    solve(N, 証言)


if __name__ == "__main__":
    main()
