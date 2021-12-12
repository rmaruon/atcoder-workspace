#!/usr/bin/env python3

A, B = [int(x) for x in input().split()]

discount_amount = A - B
discount_rate = discount_amount / A
discount_percentage = discount_rate * 100

print(discount_percentage)
