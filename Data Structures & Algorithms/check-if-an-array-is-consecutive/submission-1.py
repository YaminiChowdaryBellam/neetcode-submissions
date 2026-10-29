class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        num_set = set(nums)
        if len(num_set) != len(nums):
            return False

        smallest = min(nums)
        length = len(nums) + smallest
        for i in range(smallest, length):
            if i not in num_set:
                return False
        return True
