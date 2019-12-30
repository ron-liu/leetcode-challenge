#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, maxProfit = float('inf'), 0
        for price in prices:
            buy, maxProfit = min(buy, min(buy, price)), max(
                price - buy, maxProfit)
        return maxProfit


# @lc code=end

# 200/200 cases passed (72 ms)
# Your runtime beats 49.85 % of python3 submissions
# Your memory usage beats 72.41 % of python3 submissions (13.9 MB)
