class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root, val: int) -> Optional[TreeNode]:

        while root:
            if root.val < val:
                if root.right:
                    root = root.right
                else:
                    return
            elif root.val > val:
                if root.left:
                    root = root.left
                else:
                    return
            else:
                return root