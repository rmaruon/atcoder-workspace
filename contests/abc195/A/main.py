#!/usr/bin/env python3

M, H = [int(x) for x in input().split()]

win = H % M == 0

if win:
    print("Yes")
else:
    print("No")
