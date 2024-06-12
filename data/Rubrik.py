
#三轮都面到最后了和我说没有HC，真是坑。不过什么都经历一下波折也挺锻炼心态。

######################################################################
'''
    Rubick  11/11   店面  国人
    面的相对比较放松，thousands island 改编题，假设只有两个岛，找最短相连路径，建桥
    1   find CC
    2   find shortest path 
    最后做出了一个优化，就是只存island的边，加一个check neighbour只要有0就是边。

    但是最好的做法恰是是BFS，search by depth, 从一个岛找另一个岛，如果island比水多
    就很有优化效果

    感觉，应该能过？
'''
######################################################################
# Given a m*n matrix representing a map
# 1 - land
# 0 - water
# All connected land forms an island
# There are exactly 2 islands in the map
# Find the shortest bridge you can build to connect them
# by converting water to land

# Example1:

# [[1,1,1,1,1],
#  [1,0,0,0,1],
#  [1,0,1,0,1],
#  [1,0,0,0,1],
#  [1,1,1,1,1]]

# Answer: 1
######################################################################

import sys

def findShortestBridge(matrix):

    visited = set()
    islands = []    # a list of island boundary sets
    
    ROWS = len(matrix)
    COLS = len(matrix[0])
    
    def dfs(row, col, island):
        
        # boundary check
        if not(0 <= row < ROWS and 0 <= col < COLS):
            return False
        if matrix[row][col] == 0:
            return False

        if (row, col) not in visited:     
            visited.add((row, col))
            
            # explore its neighbours
            for d_row, d_col in (row+1,col), (row-1,col), (row,col+1), (row,col-1):
                # just add island boundary 
                if 0 <= d_row < ROWS and 0 <= d_col < COLS and matrix[d_row][d_col] == 0:
                    island.add((row, col))
                dfs(d_row, d_col, island)
            
    
        return True 
    
    # 1    find all boundary of the two islands 
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 1 and (r, c) not in visited:
                island = set()
                if dfs(r, c, island):
                    islands.append(island)    

    # 2    find the shortest bridge
    # lets say islands[0] has m positions, islands[1] has n positions, 
    # Time     O(m*n)
    # Time     O(m+n) in BFS 
    minBridge = sys.maxsize
    def dist(r0,c0,r1,c1):
        return abs(r0-r1) + abs(c0-c1)
    
    for r0,c0 in islands[0]:
        for r1,c1 in islands[1]:
            # print(minBridge)
            minBridge =  min(dist(r0,c0,r1,c1), minBridge)
    
    return minBridge-1



print(findShortestBridge([   [1,1,1,1,1],
                             [1,0,0,0,1],
                             [1,0,1,0,1],
                             [1,0,0,0,1],
                             [1,1,1,1,1]]))

print(findShortestBridge([[1,0],
                          [1,0],
                          [1,0],
                          [0,1]]
                        ))


print(findShortestBridge([  [0,1,0,0],
                            [1,1,1,0],
                            [0,1,0,1]]))


print(findShortestBridge([   [1,0,0,1,1],
                             [1,0,1,1,1],
                             [1,0,1,1,1],
                             [1,0,1,1,1],
                             [1,0,0,1,1]]))


print(findShortestBridge([   [1,1,0,0,0,1,1],
                             [1,0,0,0,0,1,0],
                             [1,0,0,0,1,1,1],
                             [1,1,0,0,0,1,0],
                             [1,0,0,0,0,1,1],
                             [1,0,0,0,0,1,1]]))
#   3

print(findShortestBridge([   [1,1,1,1,1,1,1],
                             [1,0,0,0,0,0,1],
                             [1,0,0,0,0,0,1],
                             [1,0,0,1,0,0,1],
                             [1,0,0,0,0,1,1],
                             [1,0,0,0,0,1,1]]))
# 2


# #######################################################
# Rubrik 第二轮   snapshot of a HM
# OOD 设计snapMap 好像是LC的原题，时间换空间，开始思路占用了较多时间，
# implement的时候由两三个edge case没有cover
# #######################################################
# void put(string key, string value);

# void delete(string key);

# string get(string key, Snapshot snap);

# Snapshot takeSnapshot();            # key value at the time => map 
# void deleteSnapshot(Snapshot snap);

'''
map      key value     

snapMap: map snapID to maps(ops represented by k:v):
snapID: 0 1 2 3...     store the current snapID

takeSnapshot:  add snap to snapMap, snapID++,  return ID

deleteSnapshot: take a snapID and merge the map into the next snap map with (snapID-1).
                        
get:        iterate the snapID from 0 to currentID, update the value
                EX snap 0 1 2
            return the value
            
for each snapshot, we want to store the update 
    snap 1 => map1
    snap 2 => what change from snap1 to 2, map2 = {k:newV; k:-1}

'''
def SnapShot():
    def __init__(self):
        self.currentMap = {}
        self.snapMap = {}    # map snapID to map
        self.snapID = 0
        
    def put(self, key, value):
        # check in prev snapshot
        self.currentMap[key] = value
    
    def takeSnapshot(): 
        self.snapMap[self.snapID] = copy(self.currentMap)
        self.currentMap = {}
        self.snapID += 1
        return self.snapID
            
    def get(key, snapID):
        for i in range(snapID,0,-1):        # Edge 1  improve speed
            if key in self.snapMapp[i]:
                return self.snapMap[key]
        return None
    
    def delete(key):
        self.currentMap[key] = -1        
    
    def deleteSnapshot(snapID):
        # if del snapID==1, have this copy in snapID 0  Edge 2
        if snapID == 1:
            self.snapMap[0] = copy(self.snapMap[snapID])
        # take a snapID and merge the map into the prev snap map
        for k, v in self.snapMap[snapID].items():
            # check if prev exist, decrement by 1 at each time   Edge 3
            for id in range(snapID-1,0,-1):
                if id in self.snapMap
                    break
            if k in self.snapMap[id]:
                self.snapMap[snapID-1] = v
        # delete from self.snapMap
        del self.snapMap[snapID]
    

# put(k1,v1)
# put(k2,v2)
# put(k3,v3)
# takeSnapshot() → snap1
# get(snap1, k1) → v1
# put(k1,v4)
# delete(k3)
# takeSnapshot() → snap2
# get(snap2, k1) → v4
# get(snap1, k1) → v1
# get(snap2, k3) → Error: Key k3 does not exist.
# get(snap1, k3) → v3
# deleteSnapshot(snap1)
# get(snap1, k1) → Error: Snapshot snap1 does not exist.

# want space efficiecy, comparably slow speed ok 
# space > speed

# #######################################################
# Rubrik 第三轮    implement 一个Trie的改进版本 加number
#   寒暄 5min     解释题目和idea 10min     implement Trie 15min
#   外加BFS   20min  因为BFS中case比较难搞  对于BFS on Tree不够熟悉花了点时间最后testcase没时间跑    
#   最后十分钟左右简单过了下complexity 外加 wrap up

#   每次面完问我还有啥问题我总是很尴尬，尤其如果面的不好那就很难受了
#   结果不好说
# #######################################################
# file.txt, fil...
# d = ["foo", "bar", "promise", "food"]

# d.query("fo1") -> True (matches "foo")
# d.query("f1") -> False

# "f2f", [a-z]+[0-9]+

'''
Time    insert    O(n)    where n is the number of words
        query     O(d)    where d is the (len(prefix)+number)
            BFS  O(n) in worst case
Space    O(n)    all words we stored 
'''


# idea: 
#    1    implement a insert of all words into the Trie
#    2    extract     prefix     +     number
#            if prefix match, reach a node, 
    #            try to match number    run BFS, if found any exsited, return True 
    #                end of leaf?    
    #        else    return False

from collection import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word = False
    
class Trie:
    def __init__(self, d):
        self.root = Node()
        for word in d:            
            self.insert(word)
            
    def insert(self, word): 
        curr = self.root
        for c in word:
            curr = curr.children[c]
        curr.is_word = True
        
    def query(self, comb):    # return Boolean
        # 1   extract     prefix     +     number
        prefix = ""
        number = None
        for i, c in enumerate(comb):
            if not c.isdigit():
                prefix += c
            else:
                number = comb[i:]
                break
        
        # 2    traverse the Trie and reach the prefix matching node 
        curr = self.root
        for c in prefix:
            curr = curr.children.get(c)
            if curr == None:    # leaf
                return False
        
        def BFS(curr, number):
            queue = []    # store Node 
            queue.append(curr)
            while queue:
                top = queue.pop(0)
                
                if top == "#":
                    # reaching the number level
                    if number == 0:
                        # node in the queue are all in the number level
                        for node in queue:
                            if node == "#":
                                break
                            if node and node.is_word == True:
                                return True    # found one
                        return False
                    number -= 1
                else:
                    queue.append("#")
                    # explore its children 
                    for child in top.children:
                        queue.append(child)
                    
        
        # a -> (b, c, d) -> (ek, f, g)
        # queue = [a], number is n
        # queue = [b, c, d], number is n-1
        # queue = [c, d, #, e, k], number is n-2
        
        
        # valid  prefix, check number runnning BFS
        return BFS(curr, number)
    # if found any match: curr.is_word at number level, return True imm. 
    # If not found at the end, return False



