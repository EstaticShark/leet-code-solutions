from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        full_list = []
        full_list.extend(nums1 + nums2)

        while len(full_list) != 1 and len(full_list) != 2:
            # Find the smallest and the largest number and remove them
            smallest_index = 0
            largest_index = 0

            for i in range(len(full_list)):
                if full_list[i] > full_list[largest_index]:
                    largest_index = i
                if full_list[i] < full_list[smallest_index]:
                    smallest_index = i
            full_list.pop(max(largest_index, smallest_index))
            full_list.pop(min(largest_index, smallest_index))

        if len(full_list) == 1:
            return float(full_list[0])
        else:
            return float((full_list[0] + full_list[1]) / 2)