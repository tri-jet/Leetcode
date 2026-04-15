# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # go thru tree
        # dfs style, list all nodes to current point
        # check common furthest along num to both
        # e.g. ex1 - 3,5 vs 3,1 => 3
        # ex2 - 3,5 vs 3,5,2,4 => 5
        pathP = []
        pathQ = []
        self.dfs(root, p, pathP)
        self.dfs(root, q, pathQ)

        # choose common furthest along point
        common = pathP[0]
        for a,b in zip(pathP[1:], pathQ[1:]):
            if a == b:
                common = a
            else: break
        return common

    def dfs(self, root, target, pathSoFar):
        if not root:
            return
        pathSoFar.append(target) # append regardless of if target or not
        if root.val == target:
            return
        self.dfs(root.left, target, pathSoFar)
        self.dfs(root.right, target, pathSoFar)
        
