class Solution:
    def freqAlphabets(self, s: str) -> str:
        def map(ss: str) -> (str, int):
            if len(ss) < 3 or ss[2] != '#':
                return (chr(ord(ss[0]) + 48), 1)
            else:
                return (chr(int(ss[:2]) + ord('j') - 10), 3)
        pos, ans = 0, ''
        while pos < len(s):
            c, num = map(s[pos:])
            ans = ans + c
            pos += num
        return ans
