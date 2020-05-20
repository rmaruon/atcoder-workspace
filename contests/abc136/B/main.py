#!/usr/bin/env python3
N = int(input())
count = 0

for i in range(1, N + 1):
    digit = len(str(i))
    if digit % 2 == 1:
        count += 1

print(count)
