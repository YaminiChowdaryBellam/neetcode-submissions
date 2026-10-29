from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        key = [k for k,v in frequency.items() if v > len(nums)/2]
        return key[0]