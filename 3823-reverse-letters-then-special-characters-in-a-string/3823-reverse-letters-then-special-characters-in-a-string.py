class Solution:
    def reverseByType(self, s: str) -> str:

        AL = []
        SP = []

        for i in s[::-1]:
            if i.isalpha(): AL.append(i)
            else: SP.append(i)

        AL.reverse()
        SP.reverse()

        res = []

        for i in s:
            if i.isalpha(): res.append(AL.pop())
            else: res.append(SP.pop())

        return ''.join(res)