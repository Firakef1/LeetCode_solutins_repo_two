class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0

        for right in range(1,len(nums)):

            if nums[right] != nums[left] and abs(right-left) != 1:

                left = right
                continue

            elif nums[right] != nums[left]:
                left += 1
                continue 
            
            nums[right] = "_"

        left = 0

        for right in range(len(nums)):

            if nums[right] != "_":

                nums[left] = nums[right]
                left +=1

        for i in range(len(nums)-1, left-1, -1):

            nums.pop(i)

        return len(nums)
        