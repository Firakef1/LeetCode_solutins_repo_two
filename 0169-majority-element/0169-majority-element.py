class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        temp_dict = {}

        for i in nums:

            if i not in temp_dict:

                temp_dict[i] = 1
                continue
            temp_dict[i] += 1

        for i in temp_dict:

            if temp_dict[i] == max(temp_dict.values()):

                return i

        