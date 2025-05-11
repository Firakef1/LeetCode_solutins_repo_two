class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)-1):

            if nums[i] == nums[i+1]:

                nums[i] = nums[i]*2
                nums[i+1] = 0

        
        # for i in nums:

        #     if i == 0:

        #         nums.remove(0)
        #         nums.append(0)


        

        left = 0

        for i in range(len(nums)):

            if nums[i] != 0:

                nums[left] = nums[i]
                left += 1

        for i in range(left, len(nums)):

            nums[i] = 0
    

        return nums
            



        return nums
        