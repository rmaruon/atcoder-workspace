#!/usr/bin/env python3
import itertools


def 全ての電球が点灯する(pattern, S, P):
    for 電球のスイッチの番号リスト, 電球の点灯条件 in zip(S, P):
        電球のスイッチの点灯状況 = [on for i, on in enumerate(pattern) if i + 1 in 電球のスイッチの番号リスト]
        if not 電球のスイッチの点灯状況:
            continue

        スイッチonの数 = sum(電球のスイッチの点灯状況)

        if スイッチonの数 % 2 != 電球の点灯条件:
            return False

    return True


def solve(N, M, S, P):
    count = 0

    for pattern in itertools.product([0, 1], repeat=N):
        if 全ての電球が点灯する(pattern, S, P):
            count += 1

    print(count)


def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split()))[1:] for _ in range(M)]
    P = list(map(int, input().split()))
    solve(N, M, S, P)


if __name__ == "__main__":
    main()
