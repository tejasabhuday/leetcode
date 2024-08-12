class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums1 = set(nums)
        if len(nums1) == len(nums) :
            return False
        else:
            return True