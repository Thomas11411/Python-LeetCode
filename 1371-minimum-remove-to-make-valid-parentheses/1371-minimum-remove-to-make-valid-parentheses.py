class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left ,right = [] , []
        for i,v in enumerate(s):
            if v == "(":
                left.append(i)
            elif v == ")" and left:
                left.pop()
            elif v == ")" and not left:
                right.append(i)
        remove_final = left + right
        return ''.join([v for i, v in enumerate(s) if i not in remove_final])