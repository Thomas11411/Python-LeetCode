class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        tmp = [0] * (len(s)+1)

        for st,ed,d in shifts:
            if d == 0:
                tmp[st] -= 1
                tmp[ed+1] += 1
            else:
                tmp[st] += 1
                tmp[ed+1] -= 1
                
        move = [0] * (len(s))
        move[0] = tmp[0]

        for i in range(1,len(s)):
            move[i] = move[i-1] + tmp[i]

        res = []

        for j in range(len(s)):
            res.append(chr((ord(s[j]) - 97 + move[j]) % 26 + 97))
            
        return ''.join(res)