class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        fin = []
        nums.sort()
        def dfs(arr,res):
            if not arr:
                fin.append(res)
            else:
                for i in range(len(arr)):
                    if i > 0 and arr[i] == arr[i-1]:
                        continue
                    dfs(arr[:i]+arr[i+1:],res + [arr[i]])
        dfs(nums,[])
        return fin