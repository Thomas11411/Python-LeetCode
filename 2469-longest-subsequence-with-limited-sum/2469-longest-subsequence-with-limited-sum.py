class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        import itertools
        import bisect

        nums.sort()
        acc = list(itertools.accumulate(nums))
        return [bisect.bisect(acc, i) for i in queries]