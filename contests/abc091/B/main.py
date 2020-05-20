#!/usr/bin/env python3

# input
N = int(input())
blue = {}
for _ in range(N):
    s = input()
    if s not in blue:
        blue[s] = 1
    else:
        blue[s] += 1

M = int(input())
red = {}
for _ in range(M):
    s = input()
    if s not in red:
        red[s] = 1
    else:
        red[s] += 1

# solve
max_point = 0

for s, blue_count in blue.items():
    red_count = red.get(s) or 0
    point = blue_count - red_count

    if point > max_point:
        max_point = point

print(max_point)
