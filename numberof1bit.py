class Solution:
    def hammingWeight(self, n: int) -> int:
        x = bin(n).replace("0b","")
        count = 0
        for i in range (len(x)):
            if x[i] == '1':
                count += 1 
        return count