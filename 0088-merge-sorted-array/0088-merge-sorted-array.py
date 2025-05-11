class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m+n):
            if len(nums2) == 0:
                return
            if nums1[i] >= nums2[0]:

                nums1.insert(i, nums2[0])
                nums1.pop(-1)
                nums2.pop(0)
        for i in range(len(nums2)):
            nums1.pop(-1)
        nums1.extend(nums2)



        