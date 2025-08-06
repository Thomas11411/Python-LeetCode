class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            for i in range(len(code)):
                temp = 0
                for j in range(1,k+1):
                    temp += code[(i + j) % len(code)]
                res.append(temp)
        elif k < 0:
            for i in range(len(code)):
                temp = 0
                for j in range(1,-k+1):
                    temp += code[(i + (len(code) + k - 1) + j) % len(code)]
                res.append(temp)
        return res