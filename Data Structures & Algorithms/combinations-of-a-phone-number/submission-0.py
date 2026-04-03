class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numbersToLetters = {'2': 'abc',
                            '3': 'def',
                            '4': 'ghi',
                            '5': 'jkl',
                            '6': 'mno',
                            '7': 'pqrs',
                            '8': 'tuv',
                            '9': 'wxyz'}
        res = []
        def dfs(combination, i):
            if i == len(digits):
                if combination: res.append(combination)
                return

            for c in numbersToLetters[digits[i]]:
                dfs(combination + c,i+1)

        dfs('',0)
        return res
            