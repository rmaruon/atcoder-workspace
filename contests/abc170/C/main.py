#!/usr/bin/env python3

X, N = map(int, input().split())

if N == 0:
    print(X)
    exit()

P = set(map(int, input().split()))

current_small = current_big = X

while True:
    if current_small not in P:
        print(current_small)
        break

    if current_big not in P:
        print(current_big)
        break

    current_small -= 1
    current_big += 1
