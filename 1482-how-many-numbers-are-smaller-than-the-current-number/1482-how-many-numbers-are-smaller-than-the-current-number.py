class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        sorted_nums = list(sorted(nums))

        temp_dict = {}

        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in temp_dict:

                temp_dict[sorted_nums[i]] = i

                


        for i in range(len(nums)):

            nums[i] = temp_dict[nums[i]]

        return nums
        