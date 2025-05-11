class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        nums.sort()

        left, right = 0, len(nums)-1
        min_average = float("inf")

        while left < right:

            min_max_sum = nums[left] + nums[right]

            if min_max_sum/2 < min_average:

                min_average = min_max_sum/2

            left +=1
            right -=1

        return min_average
        