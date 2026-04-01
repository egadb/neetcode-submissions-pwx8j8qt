class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sletters = {}
        tletters = {}

        for c in s:
            if c not in sletters:
                sletters[c] = 1
            else:
                sletters[c]+=1

        for c in t:
            if c not in tletters:
                tletters[c] = 1
            else:
                tletters[c]+=1

        return sletters == tletters
        