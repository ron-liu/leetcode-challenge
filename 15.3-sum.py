#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ns, ps, hasZero = {}, {}, 0
        ret = []
        for i, val in enumerate(nums):
            if val < 0:
                ns[val] = 'y' if val not in ns else 'm'
            elif val == 0:
                hasZero = hasZero + 1
            else:
                ps[val] = 'y' if val not in ps else 'm'
        if hasZero >= 3:
            ret.append([0, 0, 0])
        if hasZero > 0:
            for k in ps:
                if -k in ns:
                    ret.append([-k,  0, k])
        for kp in ps:
            for x, y in findTwoEqualToN(ns, -kp):
                ret.append([kp, x, y])
        for kn in ns:
            for x, y in findTwoEqualToN(ps, -kn):
                ret.append([kn, x, y])
        return ret


def findTwoEqualToN(dict, n):
    ret, already = [], []
    for k in dict:
        if (n - k) in dict and (n-k) not in already and (dict[k] == 'm' or n-k != k):
            ret.append((k, n-k))
            already.append(k)
    return ret


# @lc code=end

# 313/313 cases passed (388 ms)
# Your runtime beats 98.4 % of python3 submissions
# Your memory usage beats 56.43 % of python3 submissions (16.8 MB)
