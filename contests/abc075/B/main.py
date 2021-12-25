#!/usr/bin/env python3
import sys
from typing import List


def 周りの爆弾の数を数える(H: int, W: int, S: "List[str]", x: int, y: int):
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    count = 0

    for _x in dx:
        for _y in dy:
            point = {
                "x": x + _x,
                "y": y + _y,
            }

            マスが存在する = 0 <= point["y"] <= H - 1 and 0 <= point["x"] <= W - 1
            if not (マスが存在する):
                continue

            square = S[point["y"]][point["x"]]
            爆弾マスである = square == "#"
            if 爆弾マスである:
                count += 1

    return count


def n文字目の文字を置換する(string: str, n: int, new_char: str):
    return string[:n] + new_char + string[n + 1 :]


def solve(H: int, W: int, S: "List[str]"):
    for y, line in enumerate(S):
        for x, square in enumerate(line):
            if square == "#":
                continue

            count = 周りの爆弾の数を数える(H, W, S, x, y)
            S[y] = n文字目の文字を置換する(S[y], x, str(count))

    print("\n".join(S))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)


if __name__ == "__main__":
    main()
