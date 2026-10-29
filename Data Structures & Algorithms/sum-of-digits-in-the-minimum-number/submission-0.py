class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        small = nums[0]
        count = 0
        for num in nums:
            if num < small:
                small = num

        for i in str(small):
            count += int(i)
        
        if count % 2 == 0:
            return 1
        else :
            return 0