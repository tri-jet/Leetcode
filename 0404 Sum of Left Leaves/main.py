# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: # if empty then 0
            return 0
        # if root's left child exist and that child has no child then add the left child + any values from the right side
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)

        # here: left must have children of its own, so go through it in same way as ^^
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
