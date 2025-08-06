class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {i:j for i,j in knowledge}
        i = 0
        n = len(s)
        res = []

        while i < n:
            if s[i] == "(":
                key = ""
                i += 1
                while s[i] != ")":
                    key += s[i]
                    i += 1

                res.append(d.get(key,"?"))
                i += 1

            else:
                res.append(s[i])
                i += 1

        return ''.join(res) 