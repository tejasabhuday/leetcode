class Solution:
    def reverseVowels(self, s: str) -> str:
        i  = 0
        j = len(s)-1
        vowel = "aeiouAEIOU"
        st = list(s)
        while i < j:
            if st[i] in vowel and st[j] in vowel:
                temp = st[i]
                st[i] = st[j]
                st[j] = temp
                i += 1
                j -= 1
            elif st[i] not in vowel:
                i += 1
            else:
                j -= 1
        return "".join(st)



# swap the vowels that are present in a string
