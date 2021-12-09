#!/usr/bin/env python3


def solve(N, A):
    MOD = 10 ** 9 + 7
    total = sum(A)
    ans = 0

    for i in range(N - 1):
        total -= A[i]
        ans += A[i] * total
        ans %= MOD

    return ans


def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = solve(N, A)

    print(ans)


if __name__ == "__main__":
    main()
