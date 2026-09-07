class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            temp = nums.pop()
            nums.insert(0,temp)