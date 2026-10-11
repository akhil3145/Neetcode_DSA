class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        l,h = 0 , len(nums)-1
        while h>=l:
            mid = (l+h)//2
            if nums[mid] == target:
                return True 
            elif nums[mid]>target:
                h = mid-1
            else:
                l = mid+1
        return False        