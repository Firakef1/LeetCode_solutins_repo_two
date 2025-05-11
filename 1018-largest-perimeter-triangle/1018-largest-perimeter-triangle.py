class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        while True:
            try:
                if nums[-3] + nums[-2] > nums[-1]:
                    return sum(nums[-3:])
            
                nums.pop()
            
            except:

                return 0