class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordList = s.split()

        print(len(pattern))
        print(len(wordList))

        if len(pattern) != len(wordList):
            return False

        seen = set()
        pToWord = {}

        for i, c in enumerate(pattern):
            if c in pToWord:
                if pToWord[c] != wordList[i]:
                    return False
                else:
                    continue
            else:
                if wordList[i] in seen:
                    return False
                seen.add(wordList[i])
                pToWord[c] = wordList[i]

        return True
