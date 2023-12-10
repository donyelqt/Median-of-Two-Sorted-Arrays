class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_length = len(nums1) + len(nums2)
        is_even = total_length % 2 == 0
        nums = sorted(nums1 + nums2)

        if is_even:
            median = (nums[total_length // 2 - 1] + nums[total_length // 2]) / 2.0
        else:
            median = nums[total_length // 2]

        return median
