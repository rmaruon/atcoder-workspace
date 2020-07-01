#!/usr/bin/env python3

N, K = map(int, input().split())
P = list(map(int, input().split()))

P.sort()
total = sum(P[:K])

print(total)
