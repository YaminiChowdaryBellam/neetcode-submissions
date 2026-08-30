class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = 0
        b = len(nums) - 1
        while (a <= b):
            if nums[a]!= val:
                a+=1
            else:
                if nums[b] != val:
                    nums[a]=nums[b]
                    b-=1
                    a+=1
                else: 
                    b-=1
        return a
    




            
            



