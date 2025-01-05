## Easy
class solution:
    def ispalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        while temp > 0:
            digits = temp % 10
            rev = rev * 10 + digits
            temp = temp // 10
        if rev == x:
            return True
        else:
            return False


solution = solution()
print(solution.ispalindrome(int(input("Enter Number: "))))  # True
