from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #k = 2
        count_words = Counter(words).items()
        first_sort = sorted(count_words, key = lambda x: x[0])
        sort_words = sorted(first_sort, key = lambda x: x[1],reverse = True)
        final = []
        for i in range(k):
            final.append(sort_words[i][0])
        return final