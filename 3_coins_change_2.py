# _*_ coding:utf-8 _*_
"""
file: 3_coins_change_1.py
date: 2024-12-12 14:46
author: AJNB
desc:
给定几种硬币，第i种硬币的面值为 coinsi-1，目标金额为 amt，每种硬币可以重复选取，问凑出目标金额的 硬币组合数量。
dp[i][a]表示前i种硬币在a的金额目标下的组合数量
当i等于0时,表示没有硬币时,那么是不能凑出金额 a 的,所以每个dp[0][a] = 0,
当apt等于0时,表示金额为0时,那么是不用硬币的,也就是每个dp[i][0] = 1,方案为1
"""

def coins_change(cap: int, wgt: list[int]):
    n = len(wgt)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    selectNum = [[0] * (cap + 1) for _ in range(n + 1)]
    # 凑出amt的最多硬币
    MAX = amt + 1

    for i in range(0, n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, cap + 1):
            if j < wgt[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - wgt[i - 1]]
                selectNum[i][j] = selectNum[i][j - wgt[i - 1]] + 1

    return dp[n][cap] if dp[n][cap] != MAX else -1

if __name__ == '__main__':
    coins = [1, 2, 5]
    amt = 9
    print(coins_change(amt, coins))





