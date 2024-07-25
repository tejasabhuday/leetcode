class Solution(object):
    def majorityElement(self, nums):
        x= set(nums)
        for i in x:
            if nums.count(i)> len(nums)/2:
                return i
