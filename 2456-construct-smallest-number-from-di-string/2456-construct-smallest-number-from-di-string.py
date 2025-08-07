class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = [1]

        for i in range(len(pattern)):

            if pattern[i] == "I":
                tmp = res[-1] + 1
                while tmp in res: tmp += 1
                res.append(tmp)

            else:
                res.append(res[-1])
                for j in range(len(res)-1, 0, -1):
                    if res[j - 1] == res[j]: res[j - 1] += 1

        return ''.join(map(str,res))