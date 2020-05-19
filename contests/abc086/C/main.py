#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
prev_x = prev_y = prev_t = 0

for _ in range(N):
    t, x, y = map(int, readline().split())

    time = t - prev_t
    dist = abs(x - prev_x) + abs(y - prev_y)

    if dist > time or dist % 2 != time % 2:
        print("No")
        break

    prev_x, prev_y, prev_t = x, y, t

else:
    print('Yes')
