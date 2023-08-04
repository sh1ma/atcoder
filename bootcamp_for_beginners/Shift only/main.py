# coding: utf-8


from __future__ import annotations

_ = input()
s = list(map(int, input().split()))


def solve(s: list[int], depth: int):
    allEven = all([i % 2 == 0 for i in s])
    if allEven:
        solve([i / 2 for i in s], depth + 1)
    else:
        print(depth)


solve(s, 0)
