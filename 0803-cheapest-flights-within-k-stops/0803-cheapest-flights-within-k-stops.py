class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """  
        dic_edges={}

        for edge in flights:
            if edge[0] in dic_edges:
                dic_edges[edge[0]].append([edge[1],edge[2]])
            else:
                dic_edges[edge[0]]=[[edge[1],edge[2]]]

        print(dic_edges)

        ans=float('inf')
        dic_check={src:0}
        while K>=0:
            dic_next={}
            for c in dic_check:
                if c in dic_edges:

                    for r in range(len(dic_edges[c])):
                        if dic_edges[c][r][0]==dst:
                            ans=min(ans,dic_check[c]+dic_edges[c][r][1]) 
                        elif dic_edges[c][r][0] not in dic_next:
                            dic_next[dic_edges[c][r][0]]=dic_check[c]+dic_edges[c][r][1]
                        elif dic_edges[c][r][0] in dic_next:
                            dic_next[dic_edges[c][r][0]]=min(dic_next[dic_edges[c][r][0]],dic_check[c]+dic_edges[c][r][1])
            dic_check=dic_next
            K-=1
        
        return ans if ans<float('inf') else -1