class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res_time , res = releaseTimes[0] , keysPressed[0]

        for i in range(1,len(releaseTimes)):
            nowtime = releaseTimes[i] - releaseTimes[i - 1]
            if nowtime > res_time:
                res_time = nowtime
                res = keysPressed[i]
            elif nowtime == res_time:
                if keysPressed[i] > res:
                    res = keysPressed[i]
        return res