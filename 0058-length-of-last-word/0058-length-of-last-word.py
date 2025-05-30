class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = s.split()
        last = s_list[-1]

        return len(last)


            