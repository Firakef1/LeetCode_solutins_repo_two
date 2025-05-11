class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums 
        self.output = [nums[0]]

        for i in nums[1:]:

            self.output.append(self.output[-1]+i)


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        if left == 0:

            return self.output[right]


        return self.output[right]-self.output[left-1]


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)