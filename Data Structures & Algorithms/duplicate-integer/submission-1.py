class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        new_arr = set(nums)
        if n== len(new_arr):
            return False
        return True