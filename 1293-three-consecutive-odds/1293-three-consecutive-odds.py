class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        counter = 0

        for i in arr:

            if i%2 == 1:

                counter += 1

            else:

                counter = 0
            
            if counter >= 3:

                return True

        return False
        