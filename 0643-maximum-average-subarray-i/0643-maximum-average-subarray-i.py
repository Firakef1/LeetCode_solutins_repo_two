class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """


        total_sum = sum(nums[0:k-1])
        max_sum = float("-inf")
        
        left, right = 0, k-1

        print(total_sum)
        while right < len(nums):
            
            total_sum += nums[right]
            max_sum = max(max_sum, total_sum)
            total_sum -= nums[left]

            left+=1
            right += 1

        return max_sum/float(k)