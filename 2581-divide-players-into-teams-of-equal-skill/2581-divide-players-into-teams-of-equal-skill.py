class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res = 0
        skill.sort()
        tmp = skill[0] + skill[-1]
        n = len(skill)
        cnt = n // 2

        for i in range(cnt):
            if (skill[i] + skill[n - i - 1]) != tmp:
                return -1
            res += skill[i] * skill[n - i - 1]
        return res