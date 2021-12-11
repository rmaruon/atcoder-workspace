#!/usr/bin/env python3

V, T, S, D = map(int, input().split())
time = D / V

if T <= time <= S:
    print("No")
else:
    print("Yes")
