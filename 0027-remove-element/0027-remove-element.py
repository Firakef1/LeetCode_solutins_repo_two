class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        for i in range(len(nums)):

            if nums[i] == val:

                nums[i] = "_"

        left = 0

        for right in range(len(nums)):

            if nums[right] != "_":

                nums[left] = nums[right]
                left += 1

        
        for i in range(len(nums)-1, left-1, -1):

            nums.pop(i)
        