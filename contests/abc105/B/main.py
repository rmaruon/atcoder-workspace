#!/usr/bin/env python3

N = int(input())

for x in range(N // 7 + 1):
    if (N - 7 * x) % 4 == 0:
        print("Yes")
        break
else:
    print("No")

# 7x + 4y = N
# y = (N - 7x) / 4 (4で割り切れる)
