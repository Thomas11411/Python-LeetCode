from datetime import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        date_format = "%Y-%m-%d"
        start = datetime.strptime(str(int(date[:4]) - 1) + '-12-31', date_format)
        end = datetime.strptime(date, date_format)
        delta = end - start
        return delta.days