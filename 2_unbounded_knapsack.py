# _*_ coding:utf-8 _*_
"""
file: unbounded_knapsack.py.py
date: 2024-12-09 17:49
author: AJNB
desc: 完全背包问题
"""

# 返回最高价值和每个物品放几个
def unbounded_knapsack(cap: int, wgt: list[int], val: list[int]):
    n = len(wgt)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    selectNum = [[0] * (cap + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, cap + 1):
            if j < wgt[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                if dp[i - 1][j] > dp[i][j - wgt[i - 1]] + val[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - wgt[i - 1]] + val[i - 1]
                    selectNum[i][j] = selectNum[i][j - wgt[i - 1]] + 1

    items_selected = []
    c = cap
    for i in range(n, 0, -1):
        if selectNum[i][c] > 0:
            items_selected.append(selectNum[i][c])
            c -= wgt[i - 1] * selectNum[i][c]
        else:
            items_selected.append(0)
    items_selected.reverse()
    return dp[n][cap], items_selected


if __name__ == '__main__':
    # wgt = [1, 2, 3]
    # val = [5, 11, 15]
    # cap = 4
    wgt = [10, 20, 30, 40, 50]
    val = [50, 120, 150, 210, 240]
    cap = 50
    print(unbounded_knapsack(cap, wgt, val))
