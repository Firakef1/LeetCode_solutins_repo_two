class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        max_num = max(nums)
        len_max_num = len(str(max_num))
        deviser = 1

        for _ in range(len_max_num):

            buket = [[] for i in range(10)]

            for j in nums:

                index = (j//deviser)%10

                buket[index].append(j)

            nums = []

            for i in buket:

                nums.extend(i)

            deviser *=10

        max_gap = 0

        for i in range(1,len(nums)):

            gap = nums[i] - nums[i-1]

            if gap > max_gap:

                max_gap = gap


        return max_gap

        
        