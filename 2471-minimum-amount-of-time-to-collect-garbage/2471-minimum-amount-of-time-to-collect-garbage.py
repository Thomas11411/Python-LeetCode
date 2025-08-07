class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0

        sum_travel = [0]

        for t in travel:
            sum_travel.append(sum_travel[-1] + t)

            
        g_idx = -1
        p_idx = -1
        m_idx = -1

        for i in range(len(garbage)):
            
            if garbage[i].count("G") > 0:
                g_idx = i
            if garbage[i].count("P") > 0:
                p_idx = i
            if garbage[i].count("M") > 0:
                m_idx = i
                
            res += len(garbage[i])

        res += (sum_travel[g_idx] if g_idx != -1 else 0) + (sum_travel[p_idx] if p_idx != -1 else 0) + (sum_travel[m_idx] if m_idx != -1 else 0)

        return res