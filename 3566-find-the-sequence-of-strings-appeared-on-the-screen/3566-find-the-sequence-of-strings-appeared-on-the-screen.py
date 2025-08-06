class Solution:
    def stringSequence(self, target: str) -> List[str]:
        import string
        letters = list(string.ascii_lowercase)
        return [target[:i] + ch for i in range(len(target)) for ch in letters[:(ord(target[i]) - 96)]]