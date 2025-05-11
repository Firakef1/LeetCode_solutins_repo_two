class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        new_img = []

      
        for row in range(len(img)):

            new_img.append([])

            for col in range(len(img[0])):

                # print([r[max(0, col - 1): col + 2] for r in img[max(0, row - 1): row + 2]])

                window = [r[max(0, col - 1): col + 2] for r in img[max(0, row - 1): row + 2]]

                # print(window)
                
                total_sum = sum(sum(i) for i in window)
                total_elemnt = len(window)*len(window[0])

                new_img[-1].append(total_sum//total_elemnt)
            

        return new_img
