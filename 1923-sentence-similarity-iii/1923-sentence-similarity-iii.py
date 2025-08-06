class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        import collections

        arr1 = collections.deque(sentence1.split(" "))
        arr2 = collections.deque(sentence2.split(" "))

        while arr1 and arr2 and arr1[0] == arr2[0]:
            arr1.popleft()
            arr2.popleft()

        while arr1 and arr2 and arr1[-1] == arr2[-1]:
            arr1.pop()
            arr2.pop()

        return not arr1 or not arr2