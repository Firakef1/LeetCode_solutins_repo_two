class Solution:
    def tribonacci(self, n: int, memo={}) -> int:
        if n in memo:

            return memo[n]

        elif n == 0:

            memo[n] = 0
            return memo[n]

        elif n == 1 or n == 2:
            
            memo[n] = 1
            return memo[n]

        memo[n] = self.tribonacci(n-1, memo) + self.tribonacci(n-2, memo) + self.tribonacci(n-3, memo)
        return memo[n]