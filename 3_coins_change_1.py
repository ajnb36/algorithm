# _*_ coding:utf-8 _*_
"""
file: 3_coins_change_1.py
date: 2024-12-12 14:46
author: AJNB
desc:
给定 n 种硬币，第 i 种硬币的面值为 coins[i-1] ，目标金额为 amt ，每种硬币可以重复选取，问能够凑出目标金额的最少硬币数量。如果无法凑出目标金额，则返回 -1 。
前 i 种硬币能够凑出金额 a 的最少硬币数量

思考：
dp[i][a]表示前i种硬币在a的金额目标下的硬币数量
状态转移方程为dp[i][a] = min(dp[i-1][a]， dp[i][a-coins[i-1]]+1)
当i等于0时,表示没有硬币时,那么是不能凑出金额 a 的,所以每个dp[0][a] = ∞,因为不好表示无穷或者容易溢出,那么就用amt+1表示最大值
当apt等于0时,表示金额为0时,那么是不用硬币的,也就是每个dp[i][0] = 0
"""


def coins_change(cap: int, wgt: list[int]):
    n = len(wgt)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    selectNum = [[0] * (cap + 1) for _ in range(n + 1)]
    # 凑出amt的最多硬币
    MAX = amt + 1
    # 状态转移：首行首列
    for a in range(1, amt + 1):
        dp[0][a] = MAX
    for i in range(1, n + 1):
        for j in range(1, cap + 1):
            if j < wgt[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                if dp[i - 1][j] < dp[i][j - wgt[i - 1]] + 1:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - wgt[i - 1]] + 1
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
    return dp[n][cap] if dp[n][cap] != MAX else -1, items_selected


if __name__ == '__main__':
    coins = [1, 3, 5, 7, 9]

    amt = 66
    print(coins_change(amt, coins))
    # (8, [0, 1, 0, 0, 7])
