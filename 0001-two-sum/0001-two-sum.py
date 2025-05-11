class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp =  sorted(nums)

        left, right = 0, len(nums)-1

        while left < right:


            left_element, right_element = temp[left], temp[right]

            if left_element + right_element == target:

                if left_element == right_element:

                    first_index = nums.index(left_element)

                    second_index = nums.index(right_element, first_index+1)

                    return [first_index, second_index]

                return [nums.index(left_element), nums.index(right_element)]

            elif left_element + right_element > target:

                right -= 1
            
            else:

                left += 1

                