class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        fin = []
        def dfs(arr,res):
            if not arr:
                fin.append(res)
            else:
                for i in range(len(arr)):
                    dfs(arr[:i]+arr[i+1:],res + [arr[i]])
        dfs(nums,[])
        return fin