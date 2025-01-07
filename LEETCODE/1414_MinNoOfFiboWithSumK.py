# 1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k < 2: return k
        a, b = 1, 1
        while b <= k:
            a, b = b, a + b
        return self.findMinFibonacciNumbers(k - a) + 1
    
        """def findMinFibonacciNumbers(self, k):
        res, a, b = 0, 1, 1
        while b <= k:
            a, b = b, a + b
        while a > 0:
            if a <= k:
                k -= a
                res += 1
            a, b = b - a, a
        return res"""
        
# If no dup, no adjacent, we must take the biggest.
# fibo[0] + fibo[2] + fibo[4] + ... + fibo[2n] = fibo[2n + 1] - 1
# fibo[1] + fibo[3] + fibo[5] + .... + fibo[2n-1] = fibo[2n] - 1