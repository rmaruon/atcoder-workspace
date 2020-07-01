#!/usr/bin/env python3

X, Y = map(int, input().split())

# a + b = X
# 2a + 4b = Y

for a in range(X + 1):
    b = X - a

    if (2 * a + 4 * b) == Y:
        print("Yes")
        exit()

print("No")
