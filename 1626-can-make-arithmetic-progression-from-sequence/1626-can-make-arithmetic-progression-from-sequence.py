class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        dist = []
        for i in range(1,len(arr)):
            dist.append(arr[i] - arr[i-1])
        return True if len(set(dist)) == 1 else False