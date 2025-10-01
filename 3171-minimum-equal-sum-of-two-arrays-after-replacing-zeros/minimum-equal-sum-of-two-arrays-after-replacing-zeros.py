from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(x for x in nums1 if x != 0)
        s2 = sum(x for x in nums2 if x != 0)
        z1 = nums1.count(0)
        z2 = nums2.count(0)

        # Case 1: No zeros at all
        if z1 == 0 and z2 == 0:
            return s1 if s1 == s2 else -1

        # Case 2: Zeros only in nums1
        if z1 > 0 and z2 == 0:
            if s2 >= s1 + z1:
                return s2
            else:
                return -1

        # Case 3: Zeros only in nums2
        if z2 > 0 and z1 == 0:
            if s1 >= s2 + z2:
                return s1
            else:
                return -1

        # Case 4: Both have zeros
        return max(s1 + z1, s2 + z2)
