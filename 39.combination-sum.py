#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start

# Solution 2: dynamic programming
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sortedCandi = sorted(candidates)
        cache = {}

        def combin(t: int):
            if t < 1:
                return None
            if cache.get(t) is not None:
                return cache.get(t)
            if t in candidates:
                cache[t] = {(t,)}
            for n in candidates:
                subRet = combin(t - n)
                if subRet is None:
                    continue
                l = set(map(lambda x: tuple(sorted(x + (n,))), subRet))
                existed = cache.get(t, set())
                cache[t] = l.union(existed)
            return cache.get(t)
        final = combin(target)
        return list(map(lambda x: list(x),  final if final is not None else []))
# Runtime: 176 ms, faster than 12.67% of Python3 online submissions for Combination Sum.
# Memory Usage: 13 MB, less than 96.97% of Python3 online submissions for Combination Sum.

# Solution 1: recursion
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         sortedCandi = sorted(candidates)
#         cache = {}
#         for n in candidates:
#             cache[n] = {(n,)}
#         def combin(t:int):
#             if t < 1:
#                 return None
#             for n in candidates:
#                 subRet = combin(t - n)
#                 if subRet is None:
#                     continue
#                 l = set(map(lambda x: tuple(sorted(x + (n,))), subRet))
#                 existed = cache.get(t,set())
#                 cache[t] = l.union(existed)
#             return cache.get(t)
#         final = combin(target)
#         return list(map(lambda x: list(x),  final if final is not None else [] ))
# Runtime: 496 ms, faster than 5.32% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.2 MB, less than 51.51% of Python3 online submissions for Combination Sum.


# @lc code=end
