

###########################################################
''' TuSimple 一面

     再记录一遍面筋，要相信一定是越面越强的！
     而且面的越多题目覆盖面和方向一定更广，对之后面试侧重点肯定是有帮助的。

     新年第一面图森的一大姐，开始搞了半天我以为打电话耽误15min而且电脑屏幕没搞好很depressed。
     之后硬上出的是LC 原题 K distance to a node, 直接照搬代码一分钟理解直接边打边讲。
     面试真的就是看思路，根本不care的coding。10min不到coding完。

     剩下30 min给我整一个followup真扯淡了，要improve space 到O(1),说之前面试者提出的solution。
     给了hint也听不懂，消耗时间，只能去LC再找O（1） solution，最后还是看不懂。。。

     证实了刘铮说的，硬实力的面试关键，必须要naive solution快速解，甚至还要能回答出followUP。

    以后准备面试的努力方向可以不用放在题量上，更侧重一道题如何吃透！！！
    如果自己设计面试，站在面试官角度思考如果准备每道题的followUp，并一步步吃透，现在阶段质比量更重要！
'''

###########################################################
# for binary tree, all the nodes have the unique int value
# we give the target node value, all the nodes k distance away from the target node
# define the k distance away
# you have to go through k edges to arrive the node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def findKDistance(root, target, K):
    
    parentMap = {}  # map node to its parent
    parentMap[root] = None 
    
    # improve or refine o(n) space o(1)
    
    # 1 convert the tree to graph  O(n)
    def dfs(node, parent=None):
        if node:
            parentMap[node] =  parent
            dfs(node.left, node)
            dfs(node.right, node)
    dfs(root)
    
    # 2 run BFS to traverse the graph  O(n)
    queue = [(target, 0)]
    visited = set([target])
    res = []
    
    while queue:
        # match dist, restore all node to res
        if queue[0][1] = K:
            for node, d in queue:
                res.append(node.value)
            break
        
        node, d = queue(0)
        for neighbour in (node.left, node.right, parentMap[node]):
            if neighbour and neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour,d+1))

#######################################################
########## follow Up  improve to O(1) space???  #######
#######################################################
# 对着LC 代码看了半天也没完全理解，实力问题
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/143886/Java-O(1)-space-excluding-recursive-stack-space

# he use k , distance
# distance for recording the edges
# for k, if we meet target, return k-1
# for not meeting the target, return -1
#               5 
#         1          6
#     3     2      11   10
      #   9    8
#     target 3 distance k is 3   node: 6
   #  5    <--1  <--  3
   # dfs --> dfs --> 
   #     <--
       
   #      k = 2 , target = 1
   #      5 --> recursive would his children some position, 
   #      5 get the positive response to find  the qualified -- > k - 2 
   #  1 returbn k -1 --> 1 

#######################################################


###########################################################
''' TuSimple 二面

    BFS to find shortest distance on a matrix
    follow Up 
        是如果要print path怎么做
        再接着就是如果要save space怎么做    backtracking其实就是存个parentMap 好像也不是那么难
    
    全程中文面试，算正常发挥吧，开始写完有一两个小bug和var declare不清晰补上了
    毕竟是无参考代码的情况下撸出来的，也不用跑test
'''
###########################################################
"""
0 1 a 0 0 0 1
0 0 0 1 0 1 0
0 0 1 0 0 0 0
0 0 0 0 0 b 0

BFS breath first search 
    if found any    return distance
    if no path, queue empty, return int("inf")

"""

def BFS(board, pointA, pointB):
    if not board:
        return None
    if pointA == pointB:
        return 0, [] 
        
    R, C = len(board), len(board[0])
    queue = [(pointA,0)]    # store(nei, dist, parent)
    visited = {pointA}        # visited points
    parentMap = {}  # map curr to parent 
    
    ##############################################
    def backtracking(point):
        # backtrack to pointA and print the path
        res = []
        while point != pointA:
            res.append(point)
            point = parentMap[point]
        return reversed(res)
    ##############################################
    
    while queue:
        currPoint, currDist, currPath = queue.pop(0)
        # found target
        if currPoint == pointB:
            return backtracking(currPoint)
            # return currDist, currPath
        
        currRow, currCol = currPoint[0], currPoint[1]
        # explore its neighbour 
        for (row, col) in [(currRow+1,currCol), (currRow-1,currCol), (currRow,currCol-1), (currRow,currCol+1)]:
            # check in range and board[x][y]==0
            if 0<= row <R and 0<= col <C and board[row][col]==0:
                if currPoint not in visited:
                    visited.add(currPoint)
                    # add into new list
                    # newList = copy(currPath)    # currPath[:]
                    # newList.append((row, col))
                    
                    # update parent map
                    parentMap[(row, col)] = currPoint
                    
                    queue.add((currPoint,currDist+1))       
        
    return int("inf"),[]




###########################################################
# Mocking Interview of TuSimple with LIU ZHENG
###########################################################
'''
    1   简单样例走一遍 先不跑testcase
    2   思路不用特别久     节约时间
    3   coding 先考虑work  根据时间判断优化

    知识性 思考太慢    简单的例子先过一遍   4-5min  快速过一遍
    计算+two pointer List

    复杂度 细节！！！需要更熟悉数据结构

    思路走对  可以开始敲了 主体代码  edge case是可以加进去
    
    没想清楚之前最好不要说，如果有一点思路3-5 min 先想一遍。。。
        如果完全没思路再去要hint

    有效沟通！   让面试官知道我在想什么，思路纠正提示。  把握好尺度  不是自言自语
    
    尤其是店面 coding 过程中的沟通是不care的，coding完才会看。自言自语没有意义！
        边code边打备注

    1   开始思路不够清楚？简洁清楚   不用把情况说清楚
    2   代码转换！！！
'''

#######################################################
#   1   分析问题
#   分析问题    给一个简单样例 走一遍


#   TestCase

# V0 = 1
# [(1, 2), (10, 3)]       t1,tv1
# [(5, 4)]            s1,sv1

# T = 28      S ?

# 1*1=1       t’=1, update s’=1, v’=2,    2<28, not yet 

# Assume no change by s list, 10-1 * 2 + 1 = 19
#     Since 19 > 5,   assumption false
# s1-s’/v’ = 5-1 / 2 = 2      s’= 5, update t’=1 + 2, v’=4        5<28, not yet

# S list empty,   tv2-t’ * v’ =  10-3 * 4 = 28    t’=10, s’=28, update v’=3   10<28, not yet
# T list empty,   keep the speed, 
#     T-t’ * v’ = 28-10  * 3 =  54    t’=28, update s’ = 28 + 54= 82, v’ = 3
# Output 82 


# T0’     T1  T    T2
# S0’     S1        S’+++++S2(V2)

#######################################################
# FollowUp    + 复杂度
# tList   n       
# sList   m   

# Worst   m+n
# Best    1

# pop ?   linked list     O(1)
#         Python List, pop(0)  O(n)
#                      pop()    O(1)
#   Access by index, pointer 
    


#   example     给一遍！！！edge case 想清楚

#   coding ！！！ 慢    Naive => 优化

#######################################################
# 2     Coding  独立
def caclDistanec(tList, sList, v0, T):  
    prevV = v0
    V’ = v0
    S’ = 0
    T’ = 0
    L1Index = 0
    L2Index = 0
    ReachTerminal = false

    # compare head of two list by dist 
    While tList and sList: 
        T1,tv1 = tList[L1Index]
        S1, sv1 = sList[L2Index]

        # calc dist
        If (S’ + V’*T1) < S1:
            # update with head of tList
            S’ = S’ + V’*T1
            T’ = T1
            prevV = V’
            V’ = tv1
            tList.pop(0)
            L1Index = L1Index + 1 
        Else:
            # update with head of sList
            S’ = S1
            T’ = T’ + (S1- S’)//V’
            prevV = V’
            V’ = sv1
            L2Index = L2Index + 1
        
        # check if reach T, still left some in either list 
        If T’ > T:
            ReachTerminal = True 
            Break 

    If ReachTerminal:
        Return S’ - (T’-T) * prevV

    # Keep traversing tList
    While tList:
        T1,tv1 = tList[L1Index]
        S’ = S’ + V’*T1
        T’ = T1
        prevV = V’
        V’ = tv1
        tList.pop(0)
        
        If T’ > T:
            ReachTerminal = True 
            Break  

    If ReachTerminal:
        Return S’ - (T’-T) * prevV

    # Keep traversing sList
    While sList:
        S1, sv1 = sList[0]
        S’ = S1
        T’ = T’ + (S1- S’)//V’
        prevV = V’
        V’ = sv1
        sList.pop(0)
        
        If T’ > T:
            ReachTerminal = True 
            Break  

    If ReachTerminal:
        Return S’ - (T’-T) * prevV
    
    Return S’ + (T - T’) * V’



#######################################################
# LZ Mock 2
# 华容道问题     8 puzzle       类似 Airbnb二面
#   其实就是个简单的BFS，backtracking并不需要那么复杂，
#   简单的backtraking就是存一个parent map然后反向traverse到root node
#######################################################

def nextMove(currEmpty, board, R, C):
    nextBoards = []
    moves = [ 'right', 'left', 'up', 'down']
    currX, currY = currEmpty[0], currEmpty[1]

    # find all up to 4 possible next boards 
    for i, (x,y) in enumerate( [(currX, currY+1), 
                                (currX-1, currY), 
                                (currX+1, currY), 
                                (currX, currY-1)] ):
        if (0 <= x <R) and (0 <= y < C):
            newBoard = copy(board)
            # swap to modify the board
            newBoard[x][y], newBoard[currX][currY] = newBoard[x][y], newBoard[currX][currY]
            nextBoards.append((newBoard, moves[i]))

    return nextBoards

def  findEmptySlot(board, R, C):
    for x in range(R):
        for y in range(C):
            if board[x][y] == 0:
                return (x,y)

def hash(board, R, C):
    # 0-16, 0-9, abcdef
    # hash and return an int, different board return different int
    S = 0
    for x in range(R):
        for y in range(C):
            # RC 进制转 10 进制(int)
            S += board[x][y] * [(R*C)**(R*x+y)]
    return S


def BFS(board, target)
    
    R, C = len(board), len(board[0])
    queue = [(board, [])]
    Visited[board] = [move]

    emptySlot = findEmptySlot(board, R, C)

    # run BFS
    while queue:
        board, moveList = queue.pop(0)

            if  board ==  target:
            return moveList

    for nextBoard, move in nextMove( emptySlot, board, R, C):
        hashNext = hash(nextBoard, R, C)
        if hashNext not in visited:
            visited.add(hashNext)
            newmoveList = copy(moveList)
            newmoveList.add(move)       
            queue.add((nextBoard, newmoveList))

        return []


