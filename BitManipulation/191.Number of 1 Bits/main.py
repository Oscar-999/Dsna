class Solution:
    def hammingWeight(self,n:int) -> int:
        res = 0
        while n:
            if n % 2 == 1:
                res += 1
            n = n >> 1
        return res
#  res += n % 2
# n = n >> 1
#  Time and space both 0(1)

    # Sweaty version
class Solution:
    def hammingWeight(self,n:int) -> int:
        res = 0
        while n:
            n = n & (n-1)  #can be written as n &= (n-1)
            res += 1
        return res
