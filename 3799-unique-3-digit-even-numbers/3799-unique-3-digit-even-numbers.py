class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        import itertools

        return sum(i != 0 and k % 2 == 0 for i, j, k in set(itertools.permutations(digits, 3)))