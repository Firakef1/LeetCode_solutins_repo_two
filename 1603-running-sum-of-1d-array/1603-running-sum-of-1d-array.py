class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = []

        curent_sum = 0

        for i in nums:

            curent_sum += i
            output.append(curent_sum)

        return output
        