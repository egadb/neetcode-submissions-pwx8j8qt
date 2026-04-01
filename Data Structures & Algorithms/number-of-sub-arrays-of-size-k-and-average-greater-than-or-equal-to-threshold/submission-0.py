class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        res = 0
        currSum = 0

        for R in range(len(arr)):
            currSum += arr[R] 
            if (R - L + 1) == k:
                if currSum/k >= threshold:
                    res += 1
                
                currSum -= arr[L]
                L += 1

        return res