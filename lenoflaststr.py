class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = 'tejas abhuday pandey'
        z = s.split()
        print(z)
        return len(z[-1])
solution = Solution()
print(solution.lengthOfLastWord("tejas abhuday pandey"))
    