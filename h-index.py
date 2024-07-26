class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        h=0
        length = len(citations)

        for i in range(length):
            item = citations[i]
            if item >= length - i:
                h+=1
        return h
    