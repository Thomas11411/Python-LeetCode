class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        start = 0
        w , u = -1 , 0

        for i,v in logs:

            use = v - start

            if use > u:

                u = use
                w = i

            elif use == u:

                w = min(w,i)

            start = v

        return w