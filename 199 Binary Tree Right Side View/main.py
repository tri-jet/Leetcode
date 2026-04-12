# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # need to check levels + prefer right, but use left if no right, so bfs
        # or use dfs - but check which levels need left usage
        rights = []
        q = []  # to look at
        q.append(root)

        while q:
            right = None
            for x in range(len(q)): # only goes for q at the time of running the for loop first time.
                node = q.pop(0)
                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)
            if right:
                rights.append(right.val)

        return rights
