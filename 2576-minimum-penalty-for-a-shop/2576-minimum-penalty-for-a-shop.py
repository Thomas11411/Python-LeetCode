class Solution:
    def bestClosingTime(self, customers: str) -> int:

        from collections import Counter

        d = Counter(customers)

        p = d["Y"]
        min_ = d["Y"]
        res = 0

        if d["Y"] == len(customers):
            return len(customers)
        if d["N"] == len(customers):
            return 0


        for i,v in enumerate(customers):    
            if v == "Y":
                p -= 1
            else:
                p += 1
                
            if p < min_:
                min_ = p
                res = i + 1
                
        return res