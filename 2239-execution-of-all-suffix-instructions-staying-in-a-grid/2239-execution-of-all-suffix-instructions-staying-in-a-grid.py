class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        dir_len = len(s)
        def check(i):
            y , x = startPos
            for j in range(i,dir_len):
                if s[j] == 'R':
                    x += 1
                elif s[j] == 'L':
                    x -= 1
                elif s[j] == 'U':
                    y -= 1
                else:
                    y += 1

                if not (0 <= y < n and 0 <= x < n):
                    return j - i
            return dir_len - i

        return map(check,range(dir_len))