from functools import reduce
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_list = reduce(lambda x, y: int(x)*int(y), list(str(n)))
        sum_list = reduce(lambda x, y: int(x)+int(y), list(str(n)))
        return int(product_list) - int(sum_list)