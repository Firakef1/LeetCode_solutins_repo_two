

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [True] * n
        if n >= 2:
            primes[0] = primes[1] = False
        
        elif n == 1:

            primes[0] = False

        for i in range(2, int(n**0.5)+1):

            mult = 2

            if primes[i]:

                while i*mult < n:

                    primes[i*mult] = False
                    mult += 1
        
        return len([i for i in primes if i])