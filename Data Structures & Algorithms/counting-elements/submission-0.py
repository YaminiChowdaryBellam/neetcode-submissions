class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for i,num in enumerate(arr):
            if arr[i]+1 in arr:
                count += 1
        return count