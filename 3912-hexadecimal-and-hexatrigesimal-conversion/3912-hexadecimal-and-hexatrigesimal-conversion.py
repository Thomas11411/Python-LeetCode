class Solution:
    def concatHex36(self, n: int) -> str:
        import string

        res16 = hex(n ** 2)[2:]
        all_num = '0123456789' + string.ascii_lowercase
        n3 = n ** 3
        res36 = ''

        while n3 > 0:
            n3, tmp = divmod(n3, 36)
            res36 += all_num[tmp]

        return (res16 + res36[::-1]).upper()