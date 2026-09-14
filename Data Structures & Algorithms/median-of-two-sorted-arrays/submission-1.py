class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        fin=nums1+nums2
        fin.sort()
        n=len(fin)
        if n%2!=0:
            return fin[n//2]
        else:
            return (fin[n // 2 - 1] + fin[n // 2]) / 2