class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        from collections import defaultdict

        d = defaultdict(int)

        res , cnt = '' , 0

        for i in range(len(senders)):
            d[senders[i]] += len(messages[i].split(" "))

            if d[senders[i]] > cnt:
                res = senders[i]
                cnt = d[senders[i]]
            elif d[senders[i]] == cnt:
                res = max(res,senders[i])

        return res