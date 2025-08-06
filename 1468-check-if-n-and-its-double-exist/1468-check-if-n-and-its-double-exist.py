class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            arr2 = arr.copy()
            now = arr2.pop(i)
            if (now * 2) in arr2:
                return True
        return False