#!/usr/bin/env python3
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = input()
words = ("dream", "dreamer", "erase", "eraser")

while True:
    if S == "":
        print("YES")
        break

    for word in words:
        if S.endswith(word):
            S = S[: -len(word)]
            break
    else:
        print("NO")
        break
