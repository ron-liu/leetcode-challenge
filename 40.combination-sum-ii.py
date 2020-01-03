#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # combinations = {}
        def getCombination(subList: List[int], t):  # set o
            if len(subList) <= 0 or t <= 0:
                return None
            subCombinations = set()  # set of tuple
            if t in subList:
                subCombinations.add((t,))
            for index, item in enumerate(subList):
                if t-item > 0:
                    newList = subList[:index] + subList[index+1:]
                    c = getCombination(newList, t-item)  # set of tuple
                    if c is not None:
                        subCombinations = subCombinations.union(
                            set(map(lambda x: tuple(sorted(x + (item,))), c)))
            if bool(subCombinations):
                # combinations[t] = subCombinations
                return subCombinations
            else:
                return None

        final = getCombination(candidates, target)
        return list(map(lambda x: list(x),  final if final else set()))

# @lc code=end
# 172/172 cases passed (1320 ms)
# Your runtime beats 5.01 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
