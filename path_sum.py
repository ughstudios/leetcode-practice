# https://leetcode.com/problems/path-sum/
from utils import TreeNode
from typing import Optional

def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    def depth_first_search(node: Optional[TreeNode], current_sum: int) -> bool:
        if not node:
            return False
        
        current_sum += node.val
        if not node.left and not node.right:
            return current_sum == target_sum
        return depth_first_search(node.left, current_sum) or depth_first_search(node.right, current_sum)
    
    return depth_first_search(root, 0)
