#!/usr/bin/env python3


def S(n):
    a, b, c = map(int, list(str(n)))
    return a + b + c


def main():
    A, B = map(int, input().split())
    sa = S(A)
    sb = S(B)

    if sa >= sb:
        print(sa)
    else:
        print(sb)


if __name__ == "__main__":
    main()
