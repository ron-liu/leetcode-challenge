class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        cache = {}
        for i in range(len(arr)):
            cache[i] = (cache[i-1] if i > 0 else 0) ^ arr[i]

        print(cache)
        for i in range(len(queries)):
            x = queries[i]
            ans.append((cache[x[0] - 1] if x[0] > 0 else 0) ^ cache[x[1]])

        return ans
