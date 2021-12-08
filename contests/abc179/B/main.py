#!/usr/bin/env python3

N = int(input())
count = max_count = 0

for _ in range(N):
    d1, d2 = map(int, input().split())

    if d1 == d2:
        count += 1

        if count > max_count:
            max_count = count

    else:
        count = 0

if max_count >= 3:
    print("Yes")
else:
    print("No")
