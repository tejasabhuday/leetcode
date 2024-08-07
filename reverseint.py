class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        reverse = int(str(abs((x)))[::-1])
        if negative:
            reverse = -reverse
        if reverse < -2**31 or reverse >  2**31-1:
            return 0
        return reverse
    


    