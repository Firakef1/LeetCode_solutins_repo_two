class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        state = True

        for i in range(len(nums)):

            if nums[max(0, i-1)] > nums[i]:
                if nums[max(0, i-1)] < target:

                    return -1
                state = False

            if nums[i] == target:

                return i

            if state == False and nums[i] > target:

                return -1

        return -1


