# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # q = collections.deque([[root,root.val]])
        # res = 1
        # while q:
        #     for i in range(len(q)):
        #         node,max_val = q.popleft()
        #         if node:
        #             if node.left and node.left.val >= max_val:
        #                 res +=1
        #                 q.append([node.left,node.left.val])
        #             else:
        #                 q.append([node.left,max_val])
                    
        #             if node.right and node.right.val >= max_val:
        #                 res +=1
        #                 q.append([node.right,node.right.val])
        #             else:
        #                 q.append([node.right,max_val])
        # return res
        # More efficient solution
        def dfs(node,max_val):
            if not node:
                return 0
            
            res = 1 if node.val>=max_val else 0
            max_val = max(node.val,max_val)
            res += dfs(node.left,max_val)
            res += dfs(node.right,max_val)
            return res
        
        return dfs(root,root.val)
