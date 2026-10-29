from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        k = [key for key, value in frequency.items() if value == 1]
        return max(k) if k else -1
    
