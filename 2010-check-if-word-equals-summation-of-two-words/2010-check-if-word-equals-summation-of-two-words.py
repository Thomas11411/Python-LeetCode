class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        m,n,k = len(firstWord),len(secondWord),len(targetWord)
        f_res , s_res , t_res = [],[],[]

        for i in range(max(m,n,k)):
            if i < m:
                f_res.append(str(ord(firstWord[i])-ord("a")))
            if i < n:
                s_res.append(str(ord(secondWord[i])-ord("a")))
            if i < k:
                t_res.append(str(ord(targetWord[i])-ord("a")))

        return int(''.join(f_res)) + int(''.join(s_res)) == int(''.join(t_res))