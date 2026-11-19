class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        sorted_array = sorted(nums)
        w,x = sorted_array[0],sorted_array[1]
        y,z= sorted_array[-1],sorted_array[-2]
        prod_diff = (y* z) -(w * x )
        return prod_diff