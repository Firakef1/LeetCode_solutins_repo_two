class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
        
            if self.equal(nums[:i], nums[i+1:]):

                return i
        
        return -1
    def equal(self, left: List[int], right: List[int])-> bool:

        if sum(left) == sum(right):

            return True
        
        return False