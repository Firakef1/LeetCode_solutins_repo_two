class Solution(object):
    def buttonWithLongestTime(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        index = events[0][0]
        max_gap = events[0][1]

        for i in range(1,len(events)):

            gap = events[i][1] - events[i-1][1]

            if gap > max_gap:

                max_gap = gap
                index = events[i][0]

            elif gap == max_gap and events[i][0] < index:

                index = events[i][0]

        return index
        