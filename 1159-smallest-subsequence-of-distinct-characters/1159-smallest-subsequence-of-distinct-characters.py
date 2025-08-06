class Solution(object):
    def smallestSubsequence(self, text):
        from collections import defaultdict
        dictionary = defaultdict(int)
        for char in text:
            dictionary[char] +=1
        stack = []
        for char in text:
            dictionary[char] -=1
            if char in stack:
                continue
            while len(stack) and dictionary[stack[-1]] > 0  and stack[-1] >= char :
                stack.pop()
            stack.append(char)
        return "".join(stack)
        