class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        if len(str(num)) == 1:

            return num

        temp = 0

        for i in str(num):

            temp += int(i)

        num = temp

        return self.addDigits( num)
        