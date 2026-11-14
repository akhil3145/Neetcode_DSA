# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def solve(node):
            if node ==  None :
                return 0
            LH = solve(node.left)
            RH = solve(node.right)
            self.res= max(self.res,LH+RH)
            return 1+max(LH,RH)
        solve(root)
        return self.res
        