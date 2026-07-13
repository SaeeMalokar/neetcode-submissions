# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.current_node = root
        res = []
        que = []
        if root is None :
            return None
        que.append(self.current_node)
        while que:
            self.current_node = que.pop(0)
            self.current_node.left, self.current_node.right = (
            self.current_node.right,
            self.current_node.left
           )
            if self.current_node.left:
                que.append(self.current_node.left)
            if self.current_node.right:
                que.append(self.current_node.right)           
        return root

        
        
        