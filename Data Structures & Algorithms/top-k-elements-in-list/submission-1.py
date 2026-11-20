from collections import Counter
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Hashmap1 = Counter(nums)
        buckets = defaultdict(list)
        for key, value in Hashmap1.items():
            buckets[value].append(key)
        
        res = []
        for freq in range(len(nums), 0, -1):
            if freq in buckets:
                for num in buckets[freq]:
                    res.append(num)
                    if len(res) == k:
                        return res
        return res