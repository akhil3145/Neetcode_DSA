class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 0
        nums.sort()
        for r in range(1,len(nums)):
            if nums[l] == nums[r]:
                return nums[l]
            l+=1
            r+=1        