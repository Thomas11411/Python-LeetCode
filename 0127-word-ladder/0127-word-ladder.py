import heapq
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        wordList = set(wordList)
        wordList.add(beginWord)
                
        D = collections.defaultdict(set)
        
        for w in wordList:
            for i in range(len(w)):
                for char in string.ascii_lowercase:
                    n = w[:i] + char + w[i+1:]
                    if n in wordList and n != w:
                        D[w].add(n)
                        
        len_Dict = collections.defaultdict(int)
        
        myq = [(1,beginWord)]
        heapq.heapify(myq)
        len_Dict[beginWord] = 1
        
        while myq:
            curr_d,curr_w = heapq.heappop(myq)
            
            if curr_w == endWord:
                return curr_d
            
            for nxt_w in D[curr_w]:
                if nxt_w not in len_Dict:
                    heapq.heappush(myq,(curr_d+1,nxt_w))
                    len_Dict[nxt_w] = curr_d + 1
                    
        return 0
        