#!/usr/bin/env python3

X, Y = map(int, input().split())
diff = abs(X - Y)

if diff < 3:
    print("Yes")
else:
    print("No")
