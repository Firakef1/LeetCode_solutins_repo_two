class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """


        min_count = len(blocks)

        start, end = 0, k

        while end <= len(blocks):


            number = blocks[start:end].count("W")

            min_count = min(min_count, number)

            start += 1
            end += 1

        return min_count


        