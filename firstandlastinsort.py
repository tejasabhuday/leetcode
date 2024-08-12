class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        result = [-1,-1]
        for i in range(len(nums)):
            if nums[i] == target:
                result [0] = i
                break
        if result[0] == -1:
            return result
        for j in range(len(nums)-1,-1,-1):
            if nums[j] == target:
                result[1] = j
                break
        return result