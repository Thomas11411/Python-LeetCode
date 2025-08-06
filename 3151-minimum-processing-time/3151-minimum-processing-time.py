class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
            return max(map(sum, zip(sorted(processorTime),sorted(tasks)[::-4])))
        