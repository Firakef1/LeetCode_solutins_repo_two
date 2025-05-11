class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)

        for row in range(n):

            left, right = 0, n-1

            while left < right:
                
                if image[row][left] == image[row][right] and image[row][right] == 1:
                    image[row][right] = image[row][left] = 0

                elif image[row][left] == image[row][right] and image[row][right] == 0:
                    image[row][right] = image[row][left] = 1

                left += 1
                right -= 1
                continue

            if n%2 == 1:

                if image[row][left] == 0:

                    image[row][left] = 1
                else:

                    image[row][left] = 0

        return image

        