class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L, R = 0, 0
        res = 1
        prev = ''
        
        while R < len(arr):
            if arr[R-1] > arr[R] and prev != '>':
                R+=1
                prev = '>'
            elif arr[R-1] < arr[R] and prev != '<':
                R+=1
                prev = '<'
            else:
                R = R + 1 if arr[R] == arr[R-1] else R
                L = R - 1
                prev = ''
            res = max(res, R-L)
        return res