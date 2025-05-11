class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        intervals.append(newInterval)
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


            
            



        