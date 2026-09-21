import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a=nums1+nums2
        a.sort()
        return np.median(a)