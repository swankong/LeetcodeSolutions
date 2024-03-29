# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = 0, 0, 0  # index of nums1, nums2, and insert numbers
        while i < m and j < n:
            if nums1[i + k] <= nums2[j]:
                i += 1
            else:
                nums1[i + k + 1:m + k + 1] = nums1[i + k:m + k]  # make space for inserted number
                nums1[i + k] = nums2[j]  # insert number
                k += 1
                j += 1
        if i == m and j < n:
            nums1[i + k:m + n] = nums2[j:n]
        return

