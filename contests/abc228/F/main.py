#!/usr/bin/env python3
import sys


def solve(H: int, W: int, h: "List[int]", w: "List[int]", A: "List[List[int]]"):
    return


# Generated by 2.11.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    h = [int()] * (2)  # type: "List[int]"
    w = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        h[i] = int(next(tokens))
        w[i] = int(next(tokens))
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, h, w, A)

if __name__ == '__main__':
    main()