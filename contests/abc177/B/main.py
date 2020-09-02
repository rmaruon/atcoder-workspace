#!/usr/bin/env python3


def solve(S, T):
    ans = len(T)

    # Sのi文字目から、Tに一致するかどうかを調べる
    for i in range(len(S) - len(T) + 1):
        target = S[i:]
        diff = 0

        # target と t の diff を算出
        for j in range(len(T)):
            if target[j] != T[j]:
                diff += 1

        ans = min(ans, diff)

    return ans


def main():
    S = input()
    T = input()
    result = solve(S, T)
    print(result)


if __name__ == "__main__":
    main()
