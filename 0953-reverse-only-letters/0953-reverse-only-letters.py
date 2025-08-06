class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        not_char = []
        is_char= []
        for i,v in enumerate(S):
            if v.isalpha():
                is_char.append(v)
            else:
                not_char.append(v)

        rev_char = list(reversed(is_char))
        is_char_place ,not_char_place = 0,0

        final = [0] * len(S)
        for j in range(len(S)):
            if S[j].isalpha():
                final[j] = rev_char[is_char_place]
                is_char_place += 1
            else:
                final[j] = not_char[not_char_place]
                not_char_place += 1
        return "".join(final)