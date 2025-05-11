class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        new_mat = [[0]*rows for _ in range(cols)]

        for row in range(rows):

            for col in range(cols):

                new_mat[col][row] = matrix[row][col]

        
        return new_mat