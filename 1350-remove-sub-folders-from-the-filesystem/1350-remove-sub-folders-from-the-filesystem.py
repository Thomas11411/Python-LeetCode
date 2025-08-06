class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]
        now = folder[0] + '/'
        for i in range(1,len(folder)):
            if folder[i].find(now) == -1:
                now = folder[i] + '/'
                res.append(folder[i])
        return res