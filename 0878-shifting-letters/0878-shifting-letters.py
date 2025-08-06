class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        S = S[:len(shifts)]
        shift = sum(shifts) % 26
        result =[]
        for index,value in enumerate(S):
            result.append(chr(ord('a') + (ord(value) - ord('a') + shift) % 26))
            shift = (shift - shifts[index]) % 26
        return "".join(result)