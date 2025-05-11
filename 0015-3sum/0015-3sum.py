class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        if nums.count(0) == len(nums):
            return [[0,0,0]]

        nums.sort()

        for i in range(len(nums)):

            left, right = i+1, len(nums)-1

            while left < right:

                if left == i:

                    left +=1
                    continue

                elif right == i:

                    right -= 1
                    continue

                if nums[i] + nums[left] + nums[right] == 0:

                    # cheking if the numbers add up to zero in three cases just to not leave any combination unchecked
                    #case one
                    numbers = [nums[i],nums[left], nums[right]]
                    numbers.sort()

                    if numbers not in output:
                        output.append(numbers)

                    #case two
                    if nums[i] + nums[left + 1] + nums[right] == 0:

                        numbers = [nums[i],nums[left+1], nums[right]]
                        numbers.sort()

                        if numbers not in output:
                            output.append(numbers)
                        
                    
                    #case three
                    if nums[i] + nums[left] + nums[right-1] == 0:

                        
                        numbers =  [nums[i],nums[left], nums[right-1]]
                        numbers.sort()

                        if numbers not in output:

                            output.append(numbers)

                    # incrementing both pointers
                    left += 1
                    right -= 1


                    continue

                if nums[i]+nums[left]+nums[right] > 0:

                    right -= 1
                else:

                    left += 1

        return output