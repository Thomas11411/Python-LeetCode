class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split(" ")
        res = []
        for i in title:
            if len(i) <= 2:
                res.append(i.lower())
            else:
                res.append(i.capitalize())

        return " ".join(res)