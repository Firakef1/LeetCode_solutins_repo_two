class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        number = ""

        for i in digits:

            number += str(i)

        number = int(number) +1

        number = str(number)

        digits = list(map(int, number))

        return digits



        