class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        l,r = 0, len(height)-1
        leftMax = 0
        rightMax = 0
        while r>l:
            if height[l]<=height[r]:   #if left side is smaller than it will decide the water lvl
                if height[l] >= leftMax:
                    leftMax = height[l]
                else:
                    res += leftMax - height[l]
                l+=1
            else:
                #otherwise if right side wall is smaller then it will decide the water lvl
                if height[r] >= rightMax:
                    rightMax = height[r]
                else:
                    res += rightMax - height[r]
                r-=1
        return res