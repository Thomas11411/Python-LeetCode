class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = "aeiou"

        cnt = [0]

        for x in words:
            cnt.append(cnt[-1] + (x[0] in vowel and x[-1] in vowel))
                
        return [cnt[j+1] - cnt[i] for i,j in queries]