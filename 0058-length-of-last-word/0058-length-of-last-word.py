class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        prev = ""

        for i in s:

            if prev == " " and i != " ": counter = 1

            elif i != " ": counter +=1

            prev = i

        return counter


            