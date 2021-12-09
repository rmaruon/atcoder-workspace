#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
A = list(map(int, readline().split()))
A.sort(reverse=True)

alice = bob = 0

for i, num in enumerate(A):
    if i % 2 == 0:
        alice += num
    else:
        bob += num

print(alice - bob)
