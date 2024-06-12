# ######################################################################
# #    11/7 Onsite 四轮
# ######################################################################

# 第一轮韩国刚有孩子的爸爸，第二轮国人年轻人很有活力，第三轮单身大龄烙印，第四轮结婚的国人面。

# * 第一轮     写hash insert，handle collision using linkedlist，问    TLB     ml     tcp 比较水
#     * LC简单版本  https://leetcode.com/problems/design-hashmap/description/

# * 第二轮     thread vs process?    linked list题目 detect cycle + find intersection 组合题，重整代码结构，拆分函数
#     * follow up 再加一题给一个list找其中sorted最后，最大的两个值的差值，bucket sort  =》O(n)
#     * LC 141. Linked List Cycle https://leetcode.com/problems/linked-list-cycle/description/
#     * LC 160. Intersection of Two Linked Lists https://leetcode.com/problems/intersection-of-two-linked-lists/

# * 第三轮     烙印面 先解释uber的project画图讲架构ok，然后30min做题很简单的list题目没错出来，remove duplicate from sorted array改一下，如果duplicated就写两次，否则改写一次，inplace改 
#     * 开始题目都听的蒙圈，问了下这个老印口音也没听太懂
#     *  接下来还是代码写的有点乱，虽然很简单的题目但是就是被他反复质疑很烦人
#     * 升级版 https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# * 第四轮     DFS 图中找words
#     * followup有什么优化? 我给了个他意料之外的会带，说wordlist input如果找到的可以cache它的prefix，如果prefix有直接找到。没有问什么bq和os network，就是做题。
#     *         LC word search II
#   经过研究才发现原来最优解就是用Trie做caching
#         * I  med    https://leetcode.com/problems/word-search/description/
#         * II hard    https://leetcode.com/problems/word-search-ii/description/


########################################################
# producer consumenr
########################################################
import threading

class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cur = 0
        self.queue = collections.deque()
        self.cond = threading.Condition() # init with a lock

    def enqueue(self, element):
        """
        :type element: int
        :rtype: void
        """
        self.cond.acquire()     # acquire lock
        while self.cur >= self.cap:
            self.cond.wait()    # wait for consumer/dequeue
        
        self.queue += element,
        self.cur += 1
        
        self.cond.notifyAll()   # wake all producer, queue not full now
        self.cond.release()     # release lock
        

    def dequeue(self):
        """
        :rtype: int
        """
        self.cond.acquire()
        while self.cur == 0:
            self.cond.wait()    # wait for producer
        
        ans = self.queue.popleft()
        self.cur -= 1
        
        self.cond.notifyAll()   # wake all consumer, queue not empty now
        self.cond.release()
        return ans
        

    

########################################################
# design
########################################################
# # 146. LRU Cache

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:  Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
########################################################
from collections import OrderedDict  # == hashmap + PQ

class LRUCache():
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.orderedDict = OrderedDict()    # (key,value) pairs ordered by input order
        self.capacity = capacity        # only used for put() method reaching capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        
        get might not be true if key not existed in the map 
        """
        if key not in self.orderedDict:
            return - 1
        # update the key in the map, move to end so that priority is top
        self.orderedDict.move_to_end(key)
        return self.orderedDict[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        
        put is alwasy true, can always insert the key value pair
        """
        # update the key in the map, move to end so that priority is top
        if key in self.orderedDict:
            self.orderedDict.move_to_end(key)
        
        # update the key,value pair, value can be updated
        self.orderedDict[key] = value
        
        # check if reach the capacity, if so, pop the most recently not used item
        if len(self.orderedDict) > self.capacity:
            self.orderedDict.popitem(0)  # pop the front in FIFO order

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



########################################################
# Array
########################################################
# 215. Kth Largest Element in an Array
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
########################################################
import heapq

class Solution:
    # def findKthLargestNaive(self, nums: List[int], k: int) -> int:
    #     '''
    #     Time O(N log N)
    #     Space O(1)
    #     '''
    #     return sorted(nums)[-k] 

    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
            The idea is to init a heap "the smallest element first", 
            and add all elements from the array into this heap one by one keeping the size of the heap always less or equal to k
            Time O(N log k)
            Space O(k)
        '''
        minHeap = []
        for n in nums:
            heapq.heappush(minHeap, n)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]
    
        #######################################################
        # OR
        #######################################################
        #return heapq.nlargest(k, nums)[-1]



########################################################
# Tree
########################################################
# 108. Convert Sorted Array to Binary Search Tree
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted array: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5
########################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
            Partition the array into subarray and construct the subtree from it
            
            Time: O(n)
            Space: O(n) in the case of skewed binary tree.
        '''
        def convert(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
    
            # build the tree
            node = TreeNode(nums[mid])
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
    
            return node
        
        return convert(0, len(nums) - 1)

####################################################################
# 98. Validate Binary Search Tree
####################################################################
def isValidBST(root: TreeNode) -> bool:
    
    def isBSTUtil(root, min_node, max_node):
        # base case 
        if not root:
            return True
        
        # Recursive step:
        #   to check if a subtree is valid, just check if the node is max of its left and the min of its right
        if (min_node and root.val <= min_node.val) or (max_node and root.val >= max_node.val):   
            return False 
        
        return isBSTUtil(root.left, min_node, root) and isBSTUtil(root.right, root, max_node)

    return isBSTUtil(root, None, None)


####################################################################
# 230. Kth Smallest Element in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
####################################################################
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
            traverse the tree in order: left -> curr -> right 
            store in a list and return the kth largest
        '''    
        def inorder(node):
            '''traverse the tree in order'''
            if not node:
                return [] 
            return inorder(node.left) + [node.val] + inorder(node.right)

        inorder_list = inorder(root)

        return inorder_list[k-1]

# Find the kth largest in a BST 同理但是order 改一下： right -> curr -> left 



####################################################################
#   题型3     BFS     level order traversal
####################################################################

##########################################################
# 102. Binary Tree Level Order Traversal

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
##########################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
            modified BFS for level order traversal
            Time:   O(N)  since each node is processed exactly once.
            Space:  O(N)  to keep the output structure which contains N node values.
        '''
        res = []     # store nodes in current level
        if not root:
            return res
        
        level = 0   # track currect level
        queue = [root]
        
        # modified BFS traversal
        while queue:
            # start the current level
            res.append([]) 
            level_length = len(queue)   # number of elements in the current level 
            
            for i in range(level_length):
                # 1 dequeue all nodes in curr level and fulfill the current level
                node = queue.pop(0)
                res[level].append(node.val)
                
                # 2 add all child nodes of the current level in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return res



##########################################################
# Linkedlist 
# 题型 1     直接traverse 单链 linked list  
#        用prev和 curr 两个pointer
#        必要的话可以create 一个dummy node 放在head前边， prev= dummyNode()
##########################################################
# 题型 2    快慢指针  OR  hashset追踪
##########################################################




##########################################################
# 876. Middle of the Linked List
# Given a non-empty, singly linked list with head node head, 
# return a middle node of linked list.

# EX1
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])

# EX2
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
##########################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        '''
            Time    O(n)
            Space   O(1)
        '''
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

##########################################################
# 206. Reverse Linked List

# Reverse a singly linked list.
# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
########################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
            Solving using iteration:
                the basic idea is using a prev to store the 1st part of the list and curr is point to the next
            Time O(n)
            Space O(1)
        '''
        if not head or not head.next:
            return head

        # swap A and B, need C to hold A, assign B to A, assign C to B 
        prev = None
        curr = head 

        while curr != None:
            nextTemp = curr.next 
            curr.next = prev
            prev = curr         # use prev to bridge the separated linked list
            curr = nextTemp     # move curr to 2nd linkedlist

        return prev


##########################################################
# 141. Linked List Cycle
# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which 
# represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
##########################################################
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''
            Use two pointer to tarverse the linkedlist, if has cycle, then they will meet at some point
            Time    O(n)
            Space   O(1)
        '''
        if not head or not head.next or not head.next.next:
            return None 
    
        slow = head.next
        fast = head.next.next
        
        # detect cycle
        # EX    head = [3,2,0,-4], pos = 1
        # ending at     slow = 2 0 -4
        #               fast = 0 2 -4
        while fast and slow != fast:
            slow = slow.next
            if not fast.next:
                return False 
            fast = fast.next.next
        
        if fast == None:
            return False        

        return True


##########################################################
# 142. Linked List Cycle II
# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


# Example 2:

# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
##########################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
            Floyd's Tortoise and Hare for Cycle detection, math Prove !!! 
            Use two pointer to tarverse the linkedlist, if has cycle, then they will meet at some point
            then, find the beginning of the cycle
            Time    O(n)
            Space   O(1)
        '''
        if not head or not head.next or not head.next.next:
            return None 
    
        slow = head.next
        fast = head.next.next
        
        # 1. detect cycle
        # EX    head = [3,2,0,-4], pos = 1
        # ending at     slow = 2 0 -4
        #               fast = 0 2 -4
        while fast and slow != fast:
            slow = slow.next
            if not fast.next:
                return None 
            fast = fast.next.next
        
        if fast == None:
            return None        

        # 2. find the beginning of the cycle, mat
        # EX    head = [3,2,0,-4], pos = 1
        # slow = 3  2
        # fast = -4 2
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
         
        return slow
    
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
            Use a hashset to store the visited node and check if revisit a node
            Time    O(n)
            Space   O(n)
        '''
        visited = set()

        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next

        return None



##########################################################
# DP 
##########################################################
# 1143. Longest Common Subsequence
# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
##########################################################
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Time & space: O(m * n)
        '''
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        # build the DP table
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j] 
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        # return the right down side as result
        return dp[-1][-1]


##########################################################
# 221. Maximal Square
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4
##########################################################
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
            经典DP for 2D matrix
            状态转移方程   dp[i][j] = 1 + dp[i-1][j-1]    if matrx[i][j-1], matrx[i-1][j], matrx[i-1][j-1] are all ones
            
                    ==>  dp[i][j] = min( dp[i-1][j-1] + min(dp[i][j-1], dp[i-1][j]) ) + 1
            
            Time    O(m*n)
            Space   O(m*n)   可以优化到O(min(m,n))  单方向traverse，只存上一个行/列 并且不断update
        """
        if not matrix:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        largest_len = 0
        
        # build the dp matrix and 
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min( dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    largest_len = max(largest_len, dp[i][j])

        return largest_len ** 2


##########################################################
# 304. Range Sum Query 2D - Immutable
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper
# left corner (row1, col1) and lower right corner (row2, col2).
##########################################################
class NumMatrix:
    '''
    Time: O(1) time per query, O(mn) time pre-computation. 
    Space: O(mn) to build the dp matrix
'''
    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        self.dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)] 
        
        # build the dp matrix
        for r in range(rows):
            for c in range(cols):
                self.dp[r + 1][c + 1] = self.dp[r + 1][c] + self.dp[r][c + 1] + matrix[r][c] - self.dp[r][c]
 
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
