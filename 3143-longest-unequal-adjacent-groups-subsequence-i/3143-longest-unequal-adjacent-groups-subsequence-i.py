class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:

        g = groups[0]
        ans = [words[0]]

        for i in range(1,len(words)):
            if groups[i] != g:
                g = groups[i]
                ans.append(words[i])
                
        return ans