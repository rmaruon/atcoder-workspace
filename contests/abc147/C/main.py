#!/usr/bin/env python3

# input
N = int(input())
testimonies = []

for _ in range(N):
    A = int(input())
    testimonies_i = []

    for _ in range(A):
        x, y = map(int, input().split())
        testimonies_i.append((x - 1, y))  # 0-originにする

    testimonies.append(testimonies_i)


# solve
def is_honest(pattern, i):
    # i番目の人が正直者であるか (0-origin)
    return (pattern >> i) & 1


def contradiction_exists(pattern, testimonies_i):
    # ある人の複数の証言に矛盾があるか
    for testimony in testimonies_i:
        if is_honest(pattern, testimony[0]) != testimony[1]:
            return True
            break

    return False


def solve():
    max_honest = 0

    # すべての人が 正直者 or not であるパターンをbit全探索する
    for pattern in range(2**N):
        for i in range(N):
            # 正直者の証言に矛盾がないかを検証する
            if is_honest(pattern, i) and contradiction_exists(
                    pattern, testimonies[i]):
                break

        else:
            count_honest = bin(pattern).count('1')
            if count_honest > max_honest:
                max_honest = count_honest

    print(max_honest)


solve()
