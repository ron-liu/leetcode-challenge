
from collections import Counter


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        bfs, visited = {id}, {id}
        for _ in range(level):
            bfs = {j for i in bfs for j in friends[i] if j not in visited}
            visited |= bfs
        ans = Counter([q for p in bfs for q in watchedVideos[p]])
        return list(map(lambda x: x[0], sorted(ans.items(), key=lambda x: (x[1], x,))))
