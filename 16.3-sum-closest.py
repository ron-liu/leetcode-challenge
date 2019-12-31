#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        list = sorted(nums)
        ans = float('inf')
        for i in range(len(list) - 2):
            j,k=i+1, len(list) - 1
            while j<k:
                s = list[j] + list[k] +  list[i]
                ans = s if abs(s - target) < abs(ans - target) else ans
                if s < target:
                    j += 1
                elif s == target:
                    return target
                else:
                    k -= 1
        return ans

"""解体思路：
1. 先排序
2. 3 points 都可以通过先固定一个，从而转化成 2 points 问题
3. 先固定一个，做剩下的array里面，用一前一后2个pointer，逐渐逼近。
"""
        
# @lc code=end

