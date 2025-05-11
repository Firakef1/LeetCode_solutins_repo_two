class Solution:
    def climbStairs(self, n: int, memo={}) -> int:

            if n in memo:
                return memo[n]
            
            elif n == 0:
                memo[n] = 1
                return memo[n]
            
            elif n == 1:
                memo[n] = self.climbStairs(n-1, memo)
                return memo[n]

            memo[n] =  self.climbStairs(n-1) + self.climbStairs(n-2)
            return memo[n]
        