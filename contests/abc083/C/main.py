#!/usr/bin/env python3

X, Y = map(int, input().split())

count = 0
num = X

while True:
    if not X <= num <= Y:
        break

    num *= 2
    count += 1

print(count)
