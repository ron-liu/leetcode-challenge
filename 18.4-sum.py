#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        list = sorted(nums)
        ret = set()
        for i in range(len(list) - 3):
            if target < list[i] * 4 or target > list[-1] * 4:
                break
            for j in range(i+1, len(list) - 2):
                if target - list[i] < list[j] * 3 or target - list[i] > list[-1] * 4:
                    break
                k, l = j+1, len(list) - 1
                while k < l:
                    s = list[i] + list[j] + list[k] + list[l]
                    if s == target:
                        ret.add((list[i], list[j], list[k], list[l]))
                        k += 1
                        l -= 1
                    elif s < target:
                        k += 1
                    else:
                        l -= 1
        retList = []
        for item in ret:
            retList.append([item[0], item[1], item[2], item[3]])
        return retList


"""
1. 这是一个可以泛化成寻找任何个数字的问题。（https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)）
2. 其基础是在一个数组中找2个数字之和等于指定数字，然后要找更多的数字就是brute force了
3. 关键点是：上面的第L13和L16，加了这两行后，效率提高10倍
"""

# @lc code=end
# 282/282 cases passed (148 ms)
# Your runtime beats 70.92 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
