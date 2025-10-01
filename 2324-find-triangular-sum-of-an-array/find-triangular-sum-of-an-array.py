class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for j in range (len(nums)-1):
            for i in range(len(nums)-1):
                if (i < len(nums)-1) and ((i+1) <= len(nums)-1):
                    nums[i] = (nums[i] + nums[i+1]) % 10
                else :
                    continue

        return nums[0]
