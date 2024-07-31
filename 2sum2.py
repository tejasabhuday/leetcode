class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers)-1
        while left<right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left+1,right+1]
            elif total>target:
                right -= 1
            else:
                left += 1


    
# find the index of 2 values in the array that give the sum to be equal to target