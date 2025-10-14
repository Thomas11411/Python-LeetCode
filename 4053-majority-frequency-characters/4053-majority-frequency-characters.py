class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        import collections
        cnt = collections.Counter(s).items() 
        d = collections.defaultdict(list)

        for ch, k in cnt:
            d[k].append(ch)
            
        res = max(d, key = lambda x: (len(d[x]), x))

        return ''.join(d[res])