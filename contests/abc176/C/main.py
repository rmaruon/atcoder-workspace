#!/usr/bin/env python3

N = int(input())
A = map(int, input().split())

prev = 0
total = 0

for i, a in enumerate(A):
    if i == 0:
        prev = a
        continue

    if a >= prev:
        prev = a
        continue

    total += prev - a

print(total)
