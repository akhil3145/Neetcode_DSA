class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>=nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
                    j+=1
                else:
                    
                    j+=1

        return nums


                



        """
        Do not return anything, modify nums in-place instead.
        """
        