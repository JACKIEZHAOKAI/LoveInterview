#############################################################################
# 11/1  BB 全职第一轮面经
'''
    今天的面试也是完全无准备，睡到面试前20min才起来

    电话面试+ codepad 不用视频，听声音一听就是国人，是交易平台的组。
    BB 最大的四个组大概就是data, terminal, tras platform 还有一个啥，一共5000 engineer
    new grad都招去纽约， SF只收senior

    上来一道linked list 索性在LC BB高频题上搜了下，找到了一模一样的，但是短时间理解还需要时间。
    对linkedlist不够熟，看了下解答最优解是 two pointer，但是没有implementation
    于是直接用了别人的post， 但是，这个傻逼post的有问题的，没有考虑两个分开的linkedlist等长度，永远找不到intersection。
    EX Corner case
        (head1)1->2->3
        (head2)4->5->6
    
    搞了半天自己都没看懂写的逻辑，我也很尴尬怕穿帮。。。
    于是面试官说step back 可以开space，hint用一个data structure 去存，于是用hashset，但是我说用两个。
    其实只需要一个hashset先把第一个link扫一遍然后存入hashset，不存value，存unique address,这个也是提示才想出来的。
    然后再用traverse去扫，看有没有遇到之前存入hashset的原素。
    
    总的来说，第一轮面了25min，easy题目做的磕磕碰碰，非常糟。


    本来想着没戏了，硬着头皮来了第二道，但是之前做过印象非常深刻，就是topo排序，而且graph怎么建也比较熟练。
    于是很快说了用dict of set去存graph，然后run dfs改完的拓扑排序加入res list。
    这个15min打完了讲完了，沟通过程中还是有点着急，担心时间不够用，这一题做的还可以。


反思：
    1   还是要避免背题！！！ 
        专注当下的题目，专心思考，主动和面试官沟通思路，沟通一定要清晰而且要detail，再去implement。
    2   面试过程一定是一步步完成的，千万不能催面试官去drive这个conversation。
    3   思路还是不够清晰，需要加大练习的题型覆盖和思维训练！！！

'''
#######################################################
# 第一题 LC 160. Intersection of Two Linked Lists
#######################################################
'''
Give two linked list heads, they might intersection with each other.

1->2->3
       \
        5->6
       /
      4

Corner case
(head1)1->2->3
(head2)4->5->6

head1 -> 1;
head2 -> 4;
Intersect at 5.

Return first node where two linked lists intersect.

Hint: Can you think about using a Linear data structure to track something?
'''
##########################################################
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        '''
            two pointers, 假设长的LL长度为m，短的长度为n。当短的走完了之后到头，长的剩下m-n。
            然后短的pointer换到长的node的开头走m-n，长的pointer走完剩下的m-n在换到短的LL。
            接下来他们一定走剩余相同的步数到intersection!!!           Time    O(n)

            Space   O(n)
            Time    O(1)
        '''
        if not headA or not headB:
            return None 
        
        pA = headA
        pB = headB
        count =  0  # number of times traversing the linkedlist
        
        while pA != pB and count<3:
            if pA.next:    
                pA = pA.next
            else:   # reaching the end 
                pA = headB  # swap to traverse from the head of the other linkedlist
                count += 1           
            if pB.next:    
                pB = pB.next
            else:    # reaching the end 
                pB = headA
                count += 1
        # check if has intersection
        if pA == pB:
            return pA
        else:   # unable to find 
            return None
    
    def getIntersectionNode(self, headA, headB):
        """
            Use s set to store all node ref while traversing headA, 
            then traverse headB and check if curr node ref is in the set at each time
            Time    O(n)
            Space   O(n)    store the node unique address!
        """
        if not headA or not headB:
            return None

        hash_set = set([id(headA)])   # id(obj) to obtain address of the object
        cursorA = headA
        cursorB = headB

        # traverse headA and add all node addr to the set
        while cursorA:
            hash_set.add(id(cursorA))
            cursorA = cursorA.next

        while cursorB and id(cursorB) not in hash_set:
            cursorB = cursorB.next

        return cursorB

      
        

#######################################################
# 第二题 LC 207. Course Schedule
#######################################################
'''
C++ ('c') -> Data Structure ('ds')
Data Structure ('ds') -> Operating Systems ('os')
Calculus, Data Structure -> Machine Learning ('ml')
Data Structure, Operating Systems -> Database ('db')

We need to know about course orders.
(1) Can you first define a graph?
(2) Write a function return schedule of courses in an array.
'''
from collections import defaultdict

def getTopopOrder(prereq_graph):
    
    graph = defaultdict(set)

    # rebuild the graph in dependency order
    # !!! 确保所有node都被加入新的graph，否则sink不会被访问 !!!
    for key,_ in prereq_graph.items():
        graph[key] = set()

    for key, prerequisites in prereq_graph.items():
        for pre in prerequisites:    
            graph[pre].add(key)
 
    visited = set()
    stack = []  # store the topo order
    
    # modified dfs to add the topo order into stack 
    def dfs(key):
        visited.add(key)
        
        for nei in graph[key]:
            if nei not in visited:
                dfs(nei)
        
        stack.insert(0, key)
    
    # run topo sort dfs on each node
    for key,_ in graph.items():
        if key not in visited:
            dfs(key)
    
    return stack


prereq_graph = {
    "os": {"ds"},
    "ml": {"cac", "ds"},
    "db": {"ds", "os"}
}
# graph = {
#     ds:  {os, ml, db}
#     cac: {ml}
#     os:  {db}
#     ml:  { }
#     db:  { }
# }
print(getTopopOrder(prereq_graph))        # cac-> ds -> ml -> os, db





