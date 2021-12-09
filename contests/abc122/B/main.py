#!/usr/bin/env python3

S = input()

s = ""
base = ("A", "C", "G", "T")
max_len = 0

for c in S:
    if c not in base:
        s = ""
        continue

    s += c

    current_len = len(s)
    if max_len < current_len:
        max_len = current_len

print(max_len)
