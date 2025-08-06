class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.strs = strs
        if len(strs) == 0:
            self.finallist = ''
        if len(strs) == 1:
            self.finallist = strs[0]
        if len(strs) > 1:           
            self.finallist = []

            for i in range(0,len(strs) - 1) :
                #if len(strs) == 0:
                #    break
                newfirstlist = []
                finalfirstlist = []
                firstlist = list(strs[0])
                secondlist = list(strs[1])
                the_range = min(len(firstlist),len(secondlist))
                for j in range(0,the_range):
                    if firstlist[j] in secondlist[j]:
                        newfirstlist.append(firstlist[j])
                    else:
                        break
                finalfirstlist.append(''.join(newfirstlist))
                if len(finalfirstlist) == 0:
                    self.finallist = ' '.join(finalfirstlist)
                    break
                del strs[:2]
                strs = finalfirstlist + strs
                if len(strs) == 1:
                    self.finallist = ' '.join(strs)
                    break
        return self.finallist