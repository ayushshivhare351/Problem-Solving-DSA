class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        i = 1
        j = x
        while i<j:
            mid = (i+j)//2
            if mid**2 == x:
                return mid
            elif mid**2 < x and (mid+1)**2>x:
                return mid
            elif mid**2 > x:
                j = mid
            else:
                i = mid+1
