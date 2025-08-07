class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        import itertools

        ans = set()

        for i,j,k in set(itertools.permutations(digits, 3)):

            if i != 0 and k % 2 == 0:

                ans.add(100 * i + 10 * j + k)
                
        return sorted(ans)