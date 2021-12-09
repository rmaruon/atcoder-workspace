#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def contains_odd(A):
    for x in A:
        if x % 2 == 1:
            return True
    return False


def check(A, count):
    if contains_odd(A):
        return count

    count += 1
    return check([x / 2 for x in A], count)


N = int(readline())
A = [int(x) for x in readline().split()]

print(check(A, 0))
