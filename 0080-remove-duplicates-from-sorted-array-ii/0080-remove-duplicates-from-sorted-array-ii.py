class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start, end = 0, 2

        while end < len(nums):

            window = nums[start:end]

            if window[0] != window[1]:

                start += 1
                end += 1
                continue

            if window[1] == nums[end]:

                nums[start] = "_"

            else:

                start += 1
                end += 1

        left = 0

        for right in range(len(nums)):

            if nums[right] != "_":
                nums[left] = nums[right]
                left += 1
        
        for i in range(len(nums)-1, left-1, -1):

            nums.pop(i)

        return len(nums)