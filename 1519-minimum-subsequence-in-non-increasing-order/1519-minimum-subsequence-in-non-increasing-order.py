class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:

        large_sum = []

        while sum(large_sum) <= sum(nums):

            max_number = max(nums)

            max_number = nums.pop(nums.index(max_number))

            large_sum.append(max_number)
        
        return large_sum
        