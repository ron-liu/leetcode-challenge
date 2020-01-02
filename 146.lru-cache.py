#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start


class LRUCache:

    def __init__(self, capacity: int):
        self.hashTable = {}
        self.head = DoubleLinkedList(None, None)
        self.tail = DoubleLinkedList(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        node = self.hashTable.get(key)
        if node is None:
            return -1
        self.setNodeLeastUsed(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.hashTable.get(key)
        if node is not None:
            node.val = value
            self.setNodeLeastUsed(node)
            return
        node = DoubleLinkedList(key, value)
        self.hashTable[key] = node
        self.appendOnHead(node)
        if self.size < self.capacity:
            self.size += 1
            return
        del self.hashTable[self.tail.prev.key]
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

    def setNodeLeastUsed(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.appendOnHead(node)

    def appendOnHead(self, node):
        self.head.next.prev = node
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class DoubleLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


# @lc code=end
# 18/18 cases passed (220 ms)
# Your runtime beats 55.45 % of python3 submissions
# Your memory usage beats 9.09 % of python3 submissions (22.2 MB)
