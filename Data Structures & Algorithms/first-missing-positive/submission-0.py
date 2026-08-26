class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        seen = set(nums)
        for i in range(1,len(nums)+2):
            if i not in seen:
                return i 
        