class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for r in box:
            now = len(r)-1
            for j in range(len(r)-1,-1,-1):
                if r[j] == "*":
                    now = j - 1
                elif r[j] == "#":

                    r[now],r[j] = r[j],r[now]
                    now -= 1
        return zip(*box[::-1])