class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        res = 0
        if initialEnergy <= sum(energy):
            res += (sum(energy) - initialEnergy + 1)
            
        for i in experience:
            if initialExperience > i:
                initialExperience += i
            else:
                res += (i - initialExperience + 1)
                initialExperience += (2 * i - initialExperience + 1)

        return res