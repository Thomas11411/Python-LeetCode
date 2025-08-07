class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(map(lambda x : int(x) if x.isdigit() else len(x), strs))