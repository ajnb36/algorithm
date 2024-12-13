# _*_ coding:utf-8 _*_
"""
file: knapsack_dfs.py
date: 2024-12-09 09:53
author: AJNB
desc: 01背包问题
"""
from timeit import timeit

wgt = [10, 20, 30, 40, 50]
val = [50, 120, 150, 210, 240]
cap = 50


def knapsack_dfs(i: int, cap: int):
    if i == 0 or cap == 0:
        return 0
    if cap < wgt[i - 1]:
        return knapsack_dfs(i - 1, cap)
    no = knapsack_dfs(i - 1, cap)
    yes = knapsack_dfs(i - 1, cap - wgt[i - 1]) + val[i - 1]
    return max(no, yes)


def knapsack_dfs_memery(i: int, cap: int, dp):
    if i == 0 or cap == 0:
        return 0
    if dp[i][cap] != 0:
        return dp[i][cap]
    if cap < wgt[i - 1]:
        return knapsack_dfs(i - 1, cap)
    no = knapsack_dfs(i - 1, cap)
    yes = knapsack_dfs(i - 1, cap - wgt[i - 1]) + val[i - 1]
    dp[i][cap] = max(no, yes)
    return dp[i][cap]


def knapsack_dfs_dp(n: int, cap: int):
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if c < wgt[i - 1]:
                dp[i][c] = dp[i - 1][c]
            else:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - wgt[i - 1]] + val[i - 1])
    return dp[n][cap]


def knapsack_dfs_comp(wgt: list[int], val: list[int], cap: int):
    n = len(wgt)
    dp = [0] * (cap + 1)
    for i in range(1, n + 1):
        for c in range(cap, 0, -1):
            if c < wgt[i - 1]:
                # dp[c] = dp[c]
                pass
            else:
                dp[c] = max(dp[c], dp[c - wgt[i - 1]] + val[i - 1])
    return dp[cap]


def test1():
    print(knapsack_dfs(5, cap))


def test2():
    dp = [[0] * (cap + 1) for _ in range(6)]
    print(knapsack_dfs_memery(5, cap, dp))


def test3():
    print(knapsack_dfs_dp(5, cap))

def test4():
    wgt = [10, 20, 30, 40, 50]
    val = [50, 120, 150, 210, 240]
    wgt = [1, 2, 3]
    val = [5, 11, 15]
    print(knapsack_dfs_comp(wgt, val, len(wgt)+1))


if __name__ == '__main__':
    print(timeit(test1, number=1))
    print(timeit(test2, number=1))
    print(timeit(test3, number=1))
    print(timeit(test4, number=1))
