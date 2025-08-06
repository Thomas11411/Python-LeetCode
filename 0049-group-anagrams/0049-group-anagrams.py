class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dict = {}
        for i in strs:
            val = ''.join(sorted(i))
            if val not in dict:
                dict[val] = []
            dict[val].append(i)
        return dict.values()