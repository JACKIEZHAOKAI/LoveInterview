
###########################################################################
# 二面coding + OS + math proof 。。。 苍天啊
# 应该是公司发展不好 招不到人，美国准备卖了，C++的infra不用了用python搭建infra
#   基础知识太差，OS 
#   coding败露了。。。


# 问题描述
# 小明和小红玩一个游戏：从若干带有分数的小球上依照规则拿出分数之和最多的小球。 小球相连摆放，只有一个球为起点，我们称之为“根”。 
# 除了“根”之外，每个小球有且只有一个“父“小球与之相连。一番侦察之后，聪明的小明意识到 “所有小球的排列类似于一棵二叉树”。 不能同时选择两个相连的小球。

# 计算在该规则下，小明能获得的最高分数。

# 数据样例
# 输入: [3,4,5,1,3,null,1]

#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1

# 输出: 9
# 解释: 小明能获得的最高分数 = 4 + 5 = 9.

# 数据范围
# 0 <= Node.val <= 10^4
# ChatGPT
# 你可以使用动态规划来解决这个问题。在每个节点上，我们可以选择拿这个节点的分数或不拿这个节点的分数，然后递归处理子树。

# 以下是一个Python的示例代码：
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rob(root):
    if not root:
        return 0
    
    # 定义一个字典，用于存储每个节点的最优结果
    memo = {}
    
    # 定义一个递归函数，计算以当前节点为根的子树的最大分数
    def dp(node):
        if not node:
            return 0
        if node in memo:
            return memo[node]
        
        # 选择拿当前节点的分数
        rob_current = node.val
        if node.left:
            rob_current += dp(node.left.left) + dp(node.left.right)
        if node.right:
            rob_current += dp(node.right.left) + dp(node.right.right)
        
        # 不拿当前节点的分数
        not_rob_current = dp(node.left) + dp(node.right)
        
        # 计算当前节点的最优结果
        result = max(rob_current, not_rob_current)
        
        memo[node] = result
        return result
    
    return dp(root)

def build_tree_from_list(nums, index):
    if index >= len(nums) or nums[index] is None:
        return None

    root = TreeNode(nums[index])
    root.left = build_tree_from_list(nums, 2 * index + 1)
    root.right = build_tree_from_list(nums, 2 * index + 2)
    return root

# Example usage:
nums = [3, 4, 5, 1, 3, None, 1]
root = build_tree_from_list(nums, 0)


# os 双进程 死循环 context swithching 发生了什么
# ChatGPT
# 在操作系统中，当有两个或多个进程同时运行，并且它们都处于死循环状态时，会发生不断的上下文切换（Context Switching）。

# p1执行如何被计算？



# 2 core cpu 2 thread如何调度 多线程同步机制

# 如何抢同一把锁？

# 如何implement实现一个锁？

# Cpp vector vs java arraylist， 时间复杂度是多少？
# prove 均摊时间复杂度O(1)

    # 均摊时间复杂度的证明通常基于摊还分析的思想。我们将使用一个具体的示例来说明如何证明均摊时间复杂度为O(1)。

    # 考虑一个动态数组（比如ArrayList）的插入操作。这个动态数组具有以下性质：

    # 当数组空间不足时，会触发一次动态扩容操作，将数组大小扩大为原来的两倍。

    # 每次扩容操作需要将原数组的元素复制到新数组中，这个过程需要O(N)的时间，其中N是当前数组的大小。

    # 除了扩容操作外，插入操作本身（将元素添加到数组末尾）需要O(1)的时间。

    # 现在我们来证明均摊时间复杂度为O(1)：

    # 假设我们进行了N次插入操作，其中M次触发了扩容操作，而其他N-M次没有触发扩容操作。每次扩容操作的开销是O(N)。我们将这些扩容操作的总开销记为T（T = M * O(N)）。

    # 由于每次扩容操作都会使数组大小扩大为原来的两倍，因此总的插入次数N可以表示为：

    # N = 1 + 2 + 4 + ... + 2^k

    # 其中k是扩容操作的次数，即k = log2(N)。这是因为第一次扩容后数组大小为2，第二次扩容后数组大小为4，以此类推，直到数组大小达到N。

    # 现在，我们来计算总的插入次数N的上界：

    # N = 1 + 2 + 4 + ... + 2^k
    # < 2^0 + 2^1 + 2^2 + ... + 2^k
    # = 2^(k+1) - 1

    # 因此，总的插入次数N的上界是2^(k+1) - 1。现在我们可以计算均摊时间复杂度：

    # 均摊时间复杂度 = (T + N * O(1)) / N
    # = (M * O(N) + (2^(k+1) - 1) * O(1)) / (2^(k+1) - 1)
    # = (M * O(N) + O(2^k)) / (2^(k+1) - 1)
    # <= (M * O(N) + O(N)) / (2^(k+1) - 1) # 因为2^k <= N
    # = (M + 1) * O(N) / (2^(k+1) - 1)

    # 在上述公式中，M是扩容操作的次数，N是插入操作的总次数，k是扩容操作的总次数。

    # 由于M是小于等于N的，而2^(k+1) - 1是一个常数，因此均摊时间复杂度为O(1)。

    # 这就证明了在动态数组的插入操作中，均摊时间复杂度是O(1)，即使包含了不频繁但可能显著影响性能的扩容操作。这是均摊分析的典型例子，通过将操作的成本分摊到多次操作中，我们可以得出更精确的平均时间复杂度。




###########################################################################
# 傻逼图森，拆分之后打卡10-7-5
# 介绍简历项目之后就做三道题，也不怎么问思路。。。
# 代码切出去有提示，无所谓了。。。from collections import deque

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
def isValid(s):
    stack = []  # 用于存储左括号
    mapping = {')': '(', '}': '{', ']': '['}  # 映射右括号到对应的左括号

    for char in s:
        if char in mapping:
            # 当遇到右括号
            top_element = stack.pop() if stack else '#'
            if top_element != mapping[char]:
                return False
        else:
            # 当遇到左括号
            stack.append(char)

    return not stack  # 如果栈为空，说明字符串有效，否则无效

# 测试示例
print(isValid("()"))  # 输出: True
print(isValid("()[]{}"))  # 输出: True
print(isValid("(]"))  # 输出: False
print(isValid("([)]"))  # 输出: False
print(isValid("{[]}"))  # 输出: True


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

# 示例用法
my_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quicksort(my_list)
print(sorted_list)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_traversal(root):
    if root is None:
        return
    
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()  # Dequeue the current node
        print(node.value)       # Visit the current node

        if node.left:
            queue.append(node.left)  # Enqueue the left child
        if node.right:
            queue.append(node.right) # Enqueue the right child

# Example usage:
# Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform a BFS traversal
bfs_traversal(root)

