class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = "{0:b}".format(N)
        re_binary = [0] * len(binary)
        for i in range(len(binary)):
            re_binary[i] = str(1 - int(binary[i]))
        re_binary = ''.join(re_binary)
        return int(re_binary, 2)