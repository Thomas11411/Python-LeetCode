class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if complexity[0] > min(complexity) or complexity.count(complexity[0]) > 1:
            return 0
        return factorial(len(complexity) - 1) % (10 ** 9 + 7)