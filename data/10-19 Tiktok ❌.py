
# 15min 问简历。。。

# Challenge?

# Activiy service - tracing 的时候怎么用多个服务的log去集成标准
# 问的好detailed 还是需要再准备详细一点。。。

# cloud Native: 
# 	resouce management 
# 	cluster lifecycle 管理 / k8s接入 / 资源运营 3-4个

'''
    A binary search tree is a rooted tree, in which:
    * each vertex can have at most one left child and at most one right child,
    * for each non-leaf vertex 𝑥, all vertices in its left subtree are less than 𝑥. and all vertices in its right subtree are greater than 𝑥.
    You are given a tree with 𝑛 vertices. Can this tree, being rooted at some vertex, be a binary search tree, and if it can, what vertices can be a root?
    Input
        The first line contains an integer 
        𝑛  — the number of vertices in the tree.
        Each of the next n−1 lines contains two integers 𝑢[𝑖] and 𝑣[𝑖](1≤𝑢[𝑖],𝑣[𝑖]≤𝑛)— the edges of the tree.
    Output
        If this tree can't be a binary search tree, output "-1".
        Otherwise, output all vertices that can be a root, in increasing order.
        
    Examples
    input
    3
    1 2
    2 3

    output
    1 2 3

    https://leetcode.com/problems/validate-binary-search-tree/description/? ???
'''

from collections import defaultdict

def is_binary_search_tree(n, edges):
    graph = defaultdict(list)
    
    # Build the graph from the given edges
    for u, v in edges:
        graph[u].append(v)
    
    def is_bst(node, min_val, max_val):
        if node not in graph:
            return True
        
        for neighbor in graph[node]:
            if not (min_val < neighbor <= max_val):
                return False
            
            if not is_bst(neighbor, min_val, node) or not is_bst(neighbor, node, max_val):
                return False
        
        return True
    
    root_candidates = []
    for root in range(1, n + 1):
        if is_bst(root, float('-inf'), float('inf')):
            root_candidates.append(root)
    
    return root_candidates if root_candidates else -1

# Input
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Calculate and output the result
result = is_binary_search_tree(n, edges)
if result == -1:
    print(-1)
else:
    print(*result)
