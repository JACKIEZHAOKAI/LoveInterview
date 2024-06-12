
# ## HR chat
# Neeki Zohadi <neeki.zohadi@doordash.com>

# 5 min 自我介绍

# Questions:

#     major coding language: Java Python 
#     Active interviewing, No hard dealine 
#     Now in bay area!!!
#     H1b visa Oct 2023, I-140

# Role: 

#     SDE 2 / L4 
#     Infra -- Remote, work
#     Compute, K8s, traffic
#     Traffic team

# Interview Rounds:

#     1 coding + 1 debugging
#     3-4 interviews, team hiring, on-site(remote) 


# Software Engineer, Compute， 

# 2+ years of experience in Infrastructure and/or Platform, experience with (GCP, AWS, AZURE ..)


################
# ```Python
# // Given a binary tree, find the maximum path sum from any two "alive nodes" within the tree. We can assume a node is an alive node if and only if it is a leaf node, indicated by an asterisk below.

# // Example 1

# // Input

# //              5
# //            /    \  
# //          2       0 
# //         /       /  \
# //       *25      *14  *15

# // Output:

# // 47 = 25 + 2 + 5 + 15
# // Example 2

# // Input

# //              5
# //            /    \  
# //          2       0 
# //         /  \     / \
# //       *100 *50  *4 *15
# // Output:

# // 152 = 100 + 2 + 50

# */

# // Input

# //              5
# //            /    \  
# //          2*       0 
# //         /  \     / \
# //       100*  50* 4*  15*

# // Output: 102

# 5 - 2 - 100
#       - 50

# // We can see we don't include 50 here because 2* is an alive node and must be at the end of a path.
# // 100 + 2 = 102

class TreeNode:
    def __init__(self, val=0, left=None, right=None, isStar=False):
        self.val = val
        self.left = left
        self.right = right
        self.isStar = isStar

class Solution:
    def findMaxPathSum(self, root: TreeNode):
        # pass in tree root node, return max sum
        self.max_sum = float('-inf')
        
        def dfs(node: TreeNode):
            # check if curr node isStar
            if not node:
                return [0, 0]
            if not node.left and not node.right:
                return [node.val, 0]
            
            # compute left and right path sum recursively             
            left_sum, left_dead_sum = dfs(node.left)
            right_sum, right_dead_sum = dfs(node.right)
            
            node_sum = node.val + max(left_sum, 0) + max(right_sum, 0)
            node_dead_sum = max(left_dead_sum, 0) + max(right_dead_sum, 0)
                
            # update self.max_sum
            self.max_sum = max(self.max_sum, node_sum, node_dead_sum)
            if node.isStar:
                 
                            
            return [node.val + max(max(left_sum, right_sum), 0), max(left_dead_sum, right_dead_sum)]

        dfs(root)
        return self.max_sum

# //              5
# //            /    \  
# //          2       0 
# //         /  \     / \
# //       *100 *50  *4 *15
root = TreeNode(5, TreeNode(2, TreeNode(100, None, None), TreeNode(50, None, None)), TreeNode(0, TreeNode(4, None, None), TreeNode(15, None, None)) )
print(Solution().findMaxPathSum(root))
```

