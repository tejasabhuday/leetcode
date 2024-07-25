
class Solution(object):
    def rotate(self, nums, k):
        k= k% len(nums)
        r = len(nums)-k
        move = nums[0:r]
        nums[0:r]= []
        nums.extend(move)
        