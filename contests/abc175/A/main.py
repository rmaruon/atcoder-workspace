#!/usr/bin/env python3

S = input()
count = 0
max_days = 0

for x in S:
    if x == "S":
        count = 0

    if x == "R":
        count += 1
        if count > max_days:
            max_days = count

print(max_days)
