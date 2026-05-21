class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        count = 1
        for i in range(n-1):
            if nums[i]!=nums[i+1]:
                i+=1
            else:
                count+=1
        if count>1:
            return True 

        else:
            return False

        