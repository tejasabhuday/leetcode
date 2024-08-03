class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = [1,1,2,3,4,5,2,2,2,2]
        nums_set = set(nums)
        left = 0
        right = len(nums_set)-1
        mid = (right+left)-1

        while left < right:
            total = nums[right]+nums[left]+nums[mid]
            if total == 0:
                return right, left , mid
            else:
            