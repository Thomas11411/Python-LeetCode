class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split()
        final = []
        for i in range(len(s_split)):
            re_nums = s_split[i][::-1]
            final.append(re_nums)
        return ' '.join(final)