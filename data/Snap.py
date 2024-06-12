
# 第一轮过了第二轮是其他HR约的面试，我还以为是约错了，
# 没有太认真对待，非常坑。结果是两轮面试第二轮failed

################################################
'''
    Snap  11/15   店面  国人大哥

    开始10min自我介绍 15分的时候才开始做题
    30min coding 将思路 + 测试，还是在string index的迭代过程中卡壳了一下，debuging
    最后15min聊优化，死活没听懂他的解法，从两个map reduce到一个map，检测map是不是空，有点巧，听了好久再举例子才弄懂。
  
    题目是从一个string找另一个string的 permutation
    开始一看permutation我就有点慌了，string的permutation是我的弱项，于是有点紧张开始搜

    不过想了下这不就是个整一个freq map吗？这种substring的题目都是hashmap可以解，于是直接说思路开搞。   
'''
################################################
# given 2 strings, find permutations of a string in the other one.
# findPermutations("abcdecbac", "abc") => ["abc", "cba", "bac"]
################################################
'''
freq_map1
 a 1
 b 1
 c 1

freq_map2
 c 1
 b 1
 a 1
 
 update map2    if key == 0, delete

freq_map2
    a 1 -> 0 del         a 1     a 1    a 1
    b 1 -> 0 del -> ! -> d -1 -> b 1 -> b 1
    c 1 -> 0 del                 d -1   d -1
                                 e -1   e -1 
Optimization: 
 "abcdecbac"    abc
    
    abc {}      O(1) time to check  =>O(n)
    bcd {d-1 a1}    old char +1     new  -1
    cde {b1 d-1 a1 e-1}
    dec
 
'''

from collections import Counter
def findPermutation(string1, string2):
    '''
        Time O(n)   where n is the len of the 1st string 
        Space O(m)  where m is the len of the 2nd string, use hash map to store
    '''
    if not string1 or not string2 or len(string1) < len(string2):
        return []
    
    # freq_map1 = Counter(string2)
    length = len(string2)
    freq_map2 = Counter(string1[:length])
    res = []
    
    for i in range(len(string1)-length+1):
        
        # print(string1[i:length+i], freq_map1, freq_map2)
        
        # compare two map
        if freq_map1 == freq_map2:
        
            res.append(string1[i:length+i])
        
        # update freq map2 by adding a new char and removing an old char
        if freq_map2[string1[i]] == 1:
            del freq_map2[string1[i]]
        else:
            freq_map2[string1[i]] -= 1
        
        if i != len(string1)-length: 
            if string1[i+length] in freq_map2:
                freq_map2[string1[i+length]] += 1
            else:
                freq_map2[string1[i+length]] = 1
                
    return res
    

print(findPermutation("","abc"))        #[]
print(findPermutation("abcdecbac","")) # []
print(findPermutation("de","abc"))   # []
    
print(findPermutation("abcdecbac","abc"))  #['abc', 'cba', 'bac']
print(findPermutation("abcbacabca","abc"))  #
print(findPermutation("aaabaabaaaa","aaa"))  #
print(findPermutation("ababababaaaa","aba"))  #
    

################################################
'''
    Snap  11/19     印度小子

    开始10min自我介绍
    
    一道tree的题目，加上tree height 就变得很难，一时间没太多思路， BFS？ 写了快十分钟发现不行
    提示用 preorder traversal，然后想用什么internal structure 来存
    最后走了一遍自己的testcase 跑出来的结果还不对 九成挂的
'''
################################################
'''
Given n-ary tree with following node structure:

class Node {
  // Id of given node
  String id;

  // List of children
  List<Node> children;

  // Depth of given node when seen visually
  int depth;
}

Depth on a path are always increasing but not necessarily continuous.
Print the tree from left to right in increasing order of visual depth.

Example 1:

        N1 (depth = 0)
        /        |     \
       /         |       \
      N2 (d = 1) |       N3 (d = 1)
      /          |        /      |  \
     /           |       /       |    \
  N4 (d = 2)     |   N5( d = 2)  |    N6 ( d = 2)
                 |               |
              N8( d = 3 )      N7( d = 3)



         N1 (depth = 0)
        /        |     \
       /         |       \
                 |   N3 (d = 1
     /           |          \
N2 (d = 2) 1     |          N5 (d = 2) 31
                 |
            N4 (d = 3)
               21

Expected Output:
N1,N2,N3,N4,N5,N6,N8,N7
'''

import heapq

class Node:
    
    def __init__(self,id,children,depth):
#   // Id of given node
      self.id = id
    
    #   // List of children
      self.children = children
    
    #   // Depth of given node when seen visually
      self.depth = depth



def printByHeight(head):
    
    
    def preOrder(node, depth):
        
        if node != None:
            print(node.id)
            
            sorted_children = []   # (depth,branch,Node) (1,2,N6) (1,3,N3) (2,1,N2) (2,3,N5)  (3,2,N4)
            for branch, child in enumerate(node.children):
                heapq.heappush(sorted_children, (child.depth, branch, child))
            
            for (depth, branch, child) in sorted_children:
                # print(child,id, "height",depth)
                preOrder(child, depth)

    preOrder(head, 0)
    


N1 = Node("N1",[Node("N2",[],2),Node("N4",[],3),Node("N3",[Node("N5",[],2)],1)],0)
'''
EX
        N1 (depth = 0)
        /        |     \
       /         |       \
                 |   N3 (d = 1）
     /           |          \
N2 (d = 2)      |          N5 (d = 2) 
                 |
            N4 (d = 3)             
'''
print(printByHeight(N1))        

