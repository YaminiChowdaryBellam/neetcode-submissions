from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Hashmap1 = Counter(s)
        Hashmap2 = Counter(t)

        if len(s) == len(t) and Hashmap1 == Hashmap2:
            return True
        return False
            


             