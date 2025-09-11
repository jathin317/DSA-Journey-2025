class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = list(s)
        unsorted = []
        positions = []
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        for i in range(len(s)):
            if s[i] in vowels:
                unsorted.append(s[i])
                positions.append(i)

        unsorted.sort()
        for idx, pos in enumerate(positions):
            r[pos] = unsorted[idx]

        return ''.join(r)
        
        

            