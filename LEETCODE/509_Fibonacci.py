class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
        
        """if n <=1:
            return n
        a, b = 0, 1
        for _ in range(2,n+1):
            a, b = b, a+b
        return b"""