class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        res = []
        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([i,1])
        for i,v in stack:
            res.append(i * v)
        return ''.join(res)