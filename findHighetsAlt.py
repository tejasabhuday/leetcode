class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        currAlt = 0
        for g in gain:
            currAlt += g
            if currAlt > maxAlt:
                maxAlt = currAlt

        return maxAlt