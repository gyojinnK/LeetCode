# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = collections.deque([root])
        vals = []
        res = 0

        while q:
            node = q.popleft()
            vals.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        sorted_vals = sorted(vals)
        start = sorted_vals.index(low)
        end = sorted_vals.index(high)

        for i in range(start, end+1):
            res += sorted_vals[i]

        return res
        