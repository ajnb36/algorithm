# _*_ coding:utf-8 _*_
"""
file: knapsack_dfs.py
date: 2024-12-09 09:53
author: AJNB
desc: 01背包问题
"""
from timeit import timeit

from sympy import false


def knapsack_dfs_dp(cap: int, wgt: list[int], val: list[int]) -> (int, list[int]):
    n = len(wgt)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    selected = [[false] * (cap + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for c in range(1, cap + 1):
            if c < wgt[i - 1]:
                dp[i][c] = dp[i - 1][c]
            else:
                if dp[i - 1][c] > dp[i - 1][c - wgt[i - 1]] + val[i - 1]:
                    dp[i][c] = dp[i - 1][c]
                else:
                    dp[i][c] = dp[i - 1][c - wgt[i - 1]] + val[i - 1]
                    selected[i][c] = True
    # 回溯选择的物品
    items_selected = []
    c = cap
    for i in range(n, 0, -1):
        if selected[i][c]:
            # 添加被选择的物品索引
            items_selected.append(i - 1)
            # 添加被选择的物品索引
            c -= wgt[i - 1]
    items_selected.sort()
    return dp[n][cap], items_selected



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

if __name__ == '__main__':
    wgt = [10, 20, 30, 40, 50]
    val = [50, 120, 150, 210, 240]
    cap = 50
    print(knapsack_dfs_dp(cap, wgt, val))

