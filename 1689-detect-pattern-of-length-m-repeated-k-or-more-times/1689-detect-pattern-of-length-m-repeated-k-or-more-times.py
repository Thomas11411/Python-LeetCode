class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m * k + 1):
            now = arr[i:i+m] * k
            if ', '.join(map(str, now)) in ', '.join(map(str, arr)) :
                return True
        return False