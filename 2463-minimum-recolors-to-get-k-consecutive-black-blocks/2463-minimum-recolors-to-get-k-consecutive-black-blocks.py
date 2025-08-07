class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = w_cnt = blocks[0:k].count('W')

        for i in range(k,len(blocks)):
            w_cnt += ( - (blocks[i - k] == "W") + (blocks[i] == "W"))
            res = min(res,w_cnt)

        return res