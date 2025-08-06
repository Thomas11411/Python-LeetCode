class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []

        for i in words:
            tmp = i.split(separator)
            for t in tmp:
                if t: res.append(t)

        return res