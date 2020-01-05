# class Solution:
#     def minInsertions(self, s: str) -> int:
#         cache = {}
#         ans= 0
#         def dp(s):
#             if cache.get(s) is not None:
#                 return cache.get(s)
#             if s == s[::-1]:
#                 ans = 0
#             elif s[:1] == s[-1:]:
#                 ans = dp(s [1:-1])
#             else:
#                 ans = 1 + min(dp(s[1:]), dp(s[:-1]))
#             cache[s] = ans
#             return ans

#         return dp(s)


from functools import lru_cache


class Solution:
    def minInsertions(self, s: str) -> int:
        @lru_cache(None)
        def dp(s):
            if s == s[::-1]:
                return 0
            elif s[0] == s[-1]:
                return dp(s[1:-1])
            else:
                return 1 + min(dp(s[1:]), dp(s[:-1]))

        return dp(s)
