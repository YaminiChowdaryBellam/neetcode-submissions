from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        for key in frequency.keys():
            if frequency[key] == 1:
                return key
