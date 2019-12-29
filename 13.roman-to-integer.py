#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start


class Solution:
    def romanToInt(self, s: str) -> int:
        state = {'symbol': None, 'total': 0, 'hold': 0}
        for c in s:
            state = reduce(state, c)
        state = reduce(state, '')
        return state['total']


def reduce(state, s: str):
    if s == '':
        return {'total': state['total'] + state['hold']}
    currentSymbol = state['symbol']
    if currentSymbol is None:
        if s not in ['I', 'X', 'C']:
            return {"symbol": None, 'total': state['total'] + getVal(s), 'hold': 0}
        else:
            return {"symbol": s, 'total': state['total'], 'hold': getVal(s)}
    if currentSymbol in ['I', 'X', 'C']:
        if s in getPossibleFollowed(currentSymbol):
            return {"symbol": None, 'total': state['total'] + getVal(s) - state["hold"], 'hold': 0}
        elif s in ['I', 'X', 'C']:
            return {"symbol": s, 'total': state['total'] + state["hold"], 'hold': getVal(s)}
        else:
            return {"symbol": None, 'total': state['total'] + getVal(s) + state["hold"], 'hold': 0}
    return state


def getVal(symbol: str) -> int:
    map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    return map[symbol]


def getPossibleFollowed(symbol: str) -> List[str]:
    map = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}
    return map[symbol]


# @lc code=end

# 3999/3999 cases passed (52 ms)
# Your runtime beats 55.62 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)
