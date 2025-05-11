class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        group = list(range(1, n+1))

        start = 0
        while len(group) != 1:

            start = start+(k-1)

            start = start% len(group)

            group.pop(start)


        return group[0]

        