#!/usr/bin/env python3

D, T, S = map(int, input().split())

time = D / S

if time <= T:
    print("Yes")
else:
    print("No")
