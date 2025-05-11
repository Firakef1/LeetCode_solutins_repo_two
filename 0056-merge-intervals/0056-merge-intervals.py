class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        temp = [intervals[0]]

        for i in intervals[1:]:

            if temp[-1][-1] >= i[0]:

                if temp[-1][-1] < i[-1]:
                    
                    temp[-1][-1] = i[-1]

                if temp[-1][0] > i[0]:

                    temp[-1][0] = i[0]

            else:

                temp.append(i)

        return temp


        