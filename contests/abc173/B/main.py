#!/usr/bin/env python3
d = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}

N = int(input())
for _ in range(N):
    S = input()
    d[S] += 1

for k, v in d.items():
    print(f"{k} x {v}")
