# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # RECURSIVE METHOD
        # def solve(node):
        #     if node ==  None :
        #         return 0
        #     LH = solve(node.left)
        #     RH = solve(node.right)

        #     return 1+max(LH,RH)
        # return solve(root)

        # ITERATIVE METHOD
        if not root:
            return 0
        q = deque()
        q.append(root)
        height = 0
        while q:
            height+=1

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return height