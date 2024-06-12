#########################################################################
#  1    说自己是韩国长大的中国人面，年轻人还算比较好聊天，题目也做得不错，
#   最后说我是best of the all interviewers, hhh，代码很consice，尼玛背下来的最优解怎么能不consice
#########################################################################
# 1.1 topK  and API implementation of min heap
####################################################

####################################################
# 1.2 linked list find interaction  
#   Vmeware 也面了，可以作为重点题
####################################################
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

####################################################
# 1.3 graph find all shortest path from src to dst
#   n* BFS => O(n^2)
#   idea improve Time, Topo sort + traversal in hashmao, 可能就是瞎扯淡
####################################################






#########################################################################
#  2    傻逼光头面，还是要思考一条对付这种senior的对策，还是要题目和技术硬钢。。。
#       看来所有的面试者都被这个傻逼光头搞了
'''
    Hashtable 可以深挖， vmware 也面到了，可以作为重点准备
    HT 可以考的点： 
        hash function 如何define  x % HT_size
        rehash？ 什么时候需要，如何rehash？ build new HT
        proof of inser/find == O(1)     math  1 + 1/2 + 1/4 + .... 1/2^m  ==> 1
        user input insert(x), then rehash, then find(x), find(y) ... rehash需要O(n), 如何让用户体验O(1)
            batch range? 啥玩意瞎逼逼

    一道题 rm duplication in array, in place modify. 
        如果不用hashmap存 val =》 index，就要 O(n^2), 扫一遍prev subarray找，真傻比的followup        
'''

#########################################################################
#  3    Vp 讲产品，啥图数据库比SQL的好处有啥，无非就是graph来做存储，然后所谓的降低IO cost
#       听听就好了，挺无聊。。。
#########################################################################


#########################################################################
#  4    check a list of subtree, if a subtree of the given main tree
#       => [T F T T....]
#########################################################################



#########################################################################
#  5    optimize syntax tree for Join 
#   define了一堆晦涩难懂的结构，什么node input list output list
#   差不多花了40min才理解题目， code写的很随意，面的不好，题目太难了
#########################################################################


#########################################################################
#   5   implement a mergesort
#########################################################################



####################################################
# KNN    店面
####################################################
import heapq
from math import sqrt

def findKthDist(D_List, K):
    '''
        run KNN on each point and upate largest_KNN

        Time:   O( n * nlogK  + nlogn)   where nlogK for findKthLargest() for each point
                and nlogn for the sorting part 
        Space:  O(k)    for maintaining a heap
    '''
    def dist(p1,p2):
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

    def findKNN(D_List, point, K, largest_KNN):
        '''
            update the largest_KNN and return True if can update 

            if can find more than k points that has dist smaller than largest_KNN, then do not update largest_KNN
            otherwise, update largest_KNN
        '''
        # for all the non-first point
        if point != D_List[0]:
            count = 0 
            for p in D_List:
                if p != point and dist(point,p) < largest_KNN:
                    count += 1
                    if count == K:  
                        # found at least k peers with dist(point,peers) smaller than largest_KNN
                        # so that this point will not be used to update largest_KNN
                        return False, largest_KNN
        
        # otherwise, will udpate largest_KNN with this point
        dist_list = [dist(point,p) for p in D_List if p!=point]
        largest_KNN = heapq.nsmallest(K, dist_list)[-1]
        return True, largest_KNN

    if len(D_List) <= K:
        return (0,0)    

    # run KNN on each point and update largest_KNN
    largest_KNN = 0
    point_with_largest_KNN = None
    
    for point in D_List:
        found, largest_KNN = findKNN(D_List, point, K, largest_KNN)
        if found:
            point_with_largest_KNN = point
        
    return point_with_largest_KNN

