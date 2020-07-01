#!/usr/bin/env python3


def f(n):
    if n == 0:
        return ''

    n -= 1
    return f(n // 26) + chr(ord('a') + n % 26)


N = int(input())
print(f(N))
