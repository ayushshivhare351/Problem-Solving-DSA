class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        from math import gcd
        sumOdd = n*n
        sumEven = n*(n+1)
        return gcd(sumOdd,sumEven)