from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occurences = list(count.values())
        return len(occurences) == len(set(occurences))
