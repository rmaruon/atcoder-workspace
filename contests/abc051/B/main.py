#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read

K, S = map(int, read().split())
count = 0

for x in range(K + 1):
    for y in range(K + 1):
        z = S - x - y
        if 0 <= z <= K:
            count += 1

print(count)
