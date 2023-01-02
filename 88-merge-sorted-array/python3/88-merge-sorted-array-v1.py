class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = [None] * (m + n)
        mi = 0
        ni = 0
        while (mi < m) and (ni < n):
            l = nums1[mi]
            r = nums2[ni]
            if l <= r:
                res[mi + ni] = l
                mi += 1
            else:
                res[mi + ni] = r
                ni += 1
        if (mi < m):
            for i in range(mi, m):
                res[ni + i] = nums1[i]
        if (ni < n):
            for i in range(ni, n):
                res[mi + i] = nums2[i]
        for i in range(len(res)):
            nums1[i] = res[i]
