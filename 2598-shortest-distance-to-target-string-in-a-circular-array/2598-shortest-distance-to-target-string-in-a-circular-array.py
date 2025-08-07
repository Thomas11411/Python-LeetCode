class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:

        if target not in words:
            return -1

        words = words + words

        l , r = startIndex , startIndex
        while words[l] != target:
            l -= 1
            
        while words[r] != target:
            r += 1
            
        res = min(startIndex - l , r - startIndex)

        return res