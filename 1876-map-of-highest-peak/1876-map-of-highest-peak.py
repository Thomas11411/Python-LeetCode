class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        place = [[i,j] for i in range(m) for j in range(n) if isWater[i][j] == 1]
        res = [[isWater[i][j] - 1 for j in range(n)] for i in range(m)]

        height = 0

        while place:
            height += 1
            new = []
            for x,y in place:
                if x + 1 < m and res[x+1][y] < 0:
                    res[x+1][y] = height
                    new.append([x+1,y])
                if x - 1 >= 0 and res[x-1][y] < 0:
                    res[x-1][y] = height
                    new.append([x-1,y])
                if y + 1 < n and res[x][y+1] < 0:
                    res[x][y+1] = height
                    new.append([x,y+1])
                if y - 1 >= 0 and res[x][y-1] < 0:
                    res[x][y-1] = height
                    new.append([x,y-1])
            place = new

        return res