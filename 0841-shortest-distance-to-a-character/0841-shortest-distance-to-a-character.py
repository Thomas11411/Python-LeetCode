class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        output = []
    
        cins = [index for index, value in enumerate(S) if value == C]

        for i in range(len(S)) :
            if i in cins :
                output.append(0)
            else :
                output.append(min(map(lambda x : abs(x-i),cins)))
        
        return output