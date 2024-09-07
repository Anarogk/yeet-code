# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root,level):
            if not root: # if root is None return
                return
            # we sum each val on this level and add it to level key in dict
            d[level]+=root.val 
            # run dfs for curr's left and right
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        
        # default dict init
        d=defaultdict(int)
        # initiate dfs
        dfs(root,0)
        
        # mx is max level key of d
        mx=max(d)
        return d[mx] # we return added sum of nodes at max level