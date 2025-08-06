class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        now , step , ans = 0 , 0 , [0] * len(boxes)
        for i in range(len(boxes)):
            ans[i] += step
            if boxes[i] == '1':
                now += 1
            step += now 

        now , step = 0 , 0
        for i in range(len(boxes)-1,-1,-1):
            ans[i] += step
            if boxes[i] == '1':
                now += 1
            step += now 

        return ans