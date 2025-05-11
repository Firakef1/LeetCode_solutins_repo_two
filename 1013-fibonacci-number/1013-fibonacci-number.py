class Solution:
    def fib(self, n: int) -> int:

        if n == 0:

            return 0
        
        prev_one = 0
        prev_two = 1

        for i in range(1, n):

            prev_one, prev_two = prev_two, prev_one + prev_two

        return prev_two

        