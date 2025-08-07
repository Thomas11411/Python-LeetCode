class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        s1 = 0
        s2 = 0
        ten1 = []
        ten2 = []

        for i in range(len(player1)):
            if ten1 and i - ten1[-1] <= 2:
                s1 += 2 * player1[i]
            else:
                s1 += player1[i]
                
                
            if ten2 and i - ten2[-1] <= 2:
                s2 += 2 * player2[i]
            else:
                s2 += player2[i]
                
                
            if player1[i] == 10:
                ten1.append(i)
                
            if player2[i] == 10:
                ten2.append(i)

        if s1 > s2:
            return 1
        elif s1 < s2:
            return 2
        else:
            return 0