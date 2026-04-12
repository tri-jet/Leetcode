# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # only right - so always exclude the left side
        # couldn't this be dfs too?
        rights = []
        def dfs(node, rightList):
            if not node:
                return
            rightList.append(node.val)
            dfs(node.right, rightList)
        
        dfs(root,rights)
        return rights
