class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c != len(mat)*len(mat[0]):

            return mat

        new_mat = [[None]*c for _ in range(r)]

        new_row = 0
        new_col = 0

        for row in range(len(mat)):

            for col in range(len(mat[0])):

                if new_col == c:

                    new_row += 1
                    new_col = 0
                

                new_mat[new_row][new_col] = mat[row][col]
                new_col += 1

                
        return new_mat     