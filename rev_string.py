class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rev_words = words[::-1]
        reversed_string = ' '.join(rev_words)
        return reversed_string
    



# best solution
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()[::-1] #split and reverse together
        print(s)
        s = " ".join(s)
        return s