class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def helper(S, currS, currIndex, res):
            if currIndex >= len(S):
                res.append(currS)
                return
            
            if S[currIndex].isalpha():
                helper(S, currS[:currIndex] + currS[currIndex].lower() + currS[currIndex+1:], currIndex + 1, res)
                helper(S, currS[:currIndex] + currS[currIndex].upper() + currS[currIndex+1:], currIndex + 1, res)
            else:
                helper(S, currS, currIndex + 1, res) 
                
        res = []
        helper(S, S, 0, res)
        return res