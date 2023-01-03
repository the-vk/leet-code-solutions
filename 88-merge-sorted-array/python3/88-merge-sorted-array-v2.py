class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        mi = m - 1
        ni = n - 1
        while k >= 0:
            if mi == -1:
                nums1[k] = nums2[ni]
                ni -= 1
            elif ni == -1:
                nums1[k] = nums1[mi]
                mi -= 1
            elif (nums1[mi] >= nums2[ni]):
                nums1[k] = nums1[mi]
                mi -= 1
            else:
                nums1[k] = nums2[ni]
                ni -= 1
            k -= 1
