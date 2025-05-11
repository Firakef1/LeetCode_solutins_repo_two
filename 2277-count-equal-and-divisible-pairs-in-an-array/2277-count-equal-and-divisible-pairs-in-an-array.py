class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

 
        length = len(nums)
        counter = 0
        # for i in range(length):

        #     for j in range(i+1, length):

        #         if (i*j)%k == 0 and nums[i] == nums[j]:

        #             counter += 1

        #             print(i, j)


        store_dict = {}

        for i in range(length):

            if nums[i] not in store_dict:

                store_dict[nums[i]] = [i]

            else:

                store_dict[nums[i]].append(i)

        for i in store_dict.keys():

            if len(store_dict[i]) > 1:

                for j in range(len(store_dict[i])):

                    for z in range(j+1, len(store_dict[i])):

                        if (store_dict[i][j]*store_dict[i][z])%k == 0:

                            counter +=1

  

        return counter 
        