####################################################################
# valid square 
# 最优解    for循环 套一个for循环    
#     找两个点假设为对角线    计算预期两个点
# method 1:
#     暴力解决        可以跳过
#     判断四个点是否重合 return false 
#       排序 1*2*3*4 == 24 种排列全部计算
#       只要其中一种满足  4个边长向量 互相垂直且相等    a-b  b-c c-d  d-a 即是正方形
#          加一个函数算垂直： 点积==0     a1*b1 + a2* b2  == 0       《===》   a*b*cos theta ==0

# method 2: 
#     判断四个点是否重合 return false 
#     加一个计算 两点距离的函数        d(x, y )
#     任意取一个点 比如说 a    算三个距离    取最长假设为对角线    
#             max ( d（a,b）,d（a,c）,d（a,d）   ) 
#     在计算    四个边向量    

# method 3
#                 判断四个点是否重合 return false 
#                 四点相加除以4 找到圆心    
#                 check圆心到四点距离相等     else  return false 
#                 check 对角线       max ( d（a,b）,d（a,c）,d（a,d）   )  求对角线长度      假定为a c    
#                 再计算  b d长度    如果垂直 

# method 4  最优解:     只有正放形 六个距离有两个重叠     对角线相等， 每条边相等    利用这个特性


####################################################################
########    follow up是给n个点，问可以组成多少个valid square，
# 要求先O(n^4)，再改进到O(n^3)，    最后改进到 O(n^2)

# O(n^4)        四个for循环    loop

# O(n^3)        三个for循环    判断第四个预期点的位置    O1时间查询在不在set    

# O(n^2)        两个for循环    假定两个点是对角线上的点    O1算出另外两点距离    
# 两个for循环    O(n^2) 找两个点    算中点        全等三角形计算预期的两个点        

####################################################################
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        '''
            count dist of any two points 
            Time    O(1)
            Space   O(1)
        '''
        def dist(p1, p2): 
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        dist_set = set()
        for p,q in (p1, p2), (p1, p3), (p1, p4), (p2, p3), (p2, p4), (p3, p4):
            dist_set.add(dist(p,q))
        
        # avoild concurrent共点 and collineation共线 and set has size 2 
        return 0 not in dist_set and len(dist_set) == 2


    def numValidSquares(p_list):

        p_set = set(p_list)
        count = 0

        for p in p_set:
            for q in p_set:
                if p != q:
                    m,n = find_3rd_and_4th(p,q)
                    if m in p_set and n in p_set:
                        count += 1


####################################################################
# 题库
####################################################################
# key:     multi-threading     +     race condition    
# Given 
# void  register_cb (function* callback)        // add to queue if NOT fired, else just callback immediately 
# int   event_fire  ( )                         // only called once in a timeline 

# 1    call back 不要被锁住     因为不晓得callback里面的函数调用
# call back 可能调用其他callback，造成deadlock    

# 2    出现线程错误    同时修改queue里面的东西的情况：
#        register_call back （）        
#         进入的时候    context switching 进入event_fire（）
#         把fire 设置成true    then context switch 回来 if statement 判断 跳入 else 
#         于是 register的callback就丢失了
        
# 3    python  self.lock.acquire()    self.lock.release()
#      C++            mutex m;    m.lock();     m.unlock()

# ##############    pure storage 面试收获    ####### #######
# 面试官： first engineer         Wang Feng     
# 多线程设计原则：    
#     1    lock的设计原则：    同一个函数用一个lock，只锁critical section
#         Lock 只锁非原子性#   尤其不要锁 passed in 不知名的 function call 造成 deadlock 

#         threads 之间    share memo    
#         比如共享的var  , data structures 要防止多线程同时改动出错
      
#     2   concurrency issue 测试risk condition
#         traverse不同函数在不同线程跑  edge case会发生什么情况    
#######################################################
class event:
  # python constructor 
  def __init__(self): 
    self.queue = []     
    self.fired = False    
    self.lock = Lock()

  def register_cb(x):
      self.lock.acquire()
      if self.fired == false:     
          queue.append(x)
          self.lock.release()
      else:
        self.lock.release()
          cb(x) # key: 不能锁callback， deadlock 
  
  # 缺点是 lock acquire release 两次很危险, 可能造成cb进入其他callback
  # So  最好是只锁住 fired == True
  
  # ########### 加面： 如果先
  #   1 fired = True
  #   2 lock.acquire()
  #   3 lock.release()
  #   4 while loop
  # ANS:  这样不会有问题 travese一下考虑 risk condition
  # 因为fired就算fired ==Ture 然后 CS到了 register_cb（）也会call cb(x)
  
  # ########### 但是！！！！
  # 如果去处中间的   2 lock.acquire()  3 lock.release() 就会出问题
  # register_cb 之后fired判断为 False  准备append
  # 然后又 CS到了到了event_fire  跑了4 while loop把queue pop空了
  # 接下来append  x这个callback  到queue就不会被call了  
  # 因为 event_fire（） 之后被call 一遍，残留的callback x就丢失了

  # lock的设计原则：  同一个函数用一个lock，只锁critical section

  def event_fire(): 
      self.lock.acquire()
      self.fired = True
      while len(queue):
           x = queue.pop () # python pop will pop and take the front
           self.lock.release()
           cb(x)            # call back func called taking a para x
           self.lock.acquire()
      self.lock.release()    

  # 第二种写法 最优解
  def event_fire():
    self.lock.acquire()
    fired = True 
    self.lock.release()
    while len(queue):
      x = queue.pop() 
      cb(x)

  # # 第三种写法 类似第二种 只是用while（true）形式写
  # # set the fired to be true immediately if queue 
  # #   is empty so that fired == false does not come in between.
  # def event_fire():
  #   while(1):
  #     self.lock.acquire()
  #     if(len(queue) == 0):
  #       fired = True
  #       self.lock.release()
  #       break;
  #     else:
  #       self.lock.release()
  #       x = queue.pop()
  #       cb(x)

register_cb(x)
register_cb(x1)
register_cb(x2)
event_fire()


####################################################################
# 647. Palindromic Substrings
# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
####################################################################
class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Expand Around Center
            if [a, b] is a palindromic interval (meaning S[a], S[a+1], ..., S[b] is a palindrome), then [a+1, b-1] is one too. 
            For each possible palindrome center, let's expand our candidate palindrome on the interval [left, right] as long as we can.
            The condition for expanding is left >= 0 and right < N and S[left] == S[right]. 
            That means we want to count a new palindrome S[left], S[left+1], ..., S[right].
            
            Time    O(n^2)
            Space   O(1)
        '''
        left, right = 0, 0
        count = 0
    
        for center in range(0,len(s)*2 - 1):
            left = center//2
            right = left + center%2
            # try to expand left and right from the center    
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        
        return count

####################################################################
# 203. Remove Linked List Elements
# DescriptionHintsSubmissionsDiscussSolution
# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
####################################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        '''
            Use dummy/sentinel node to keep track of the linkedlist and delete nodes
            Edge case is the node to be deleted is at front 

            Time    O(n)
            Space   O(1)
        '''
        dummy = ListNode(0)
        dummy.next = head
        prev, curr =  dummy, head
        
        while curr != None:
            # print("prev ",prev.val,"curr ", curr.val)
            if curr.val == val:
                # In the values are equal, delete the current node, prev not changed 
                prev.next = curr.next  
            else:
                # otherwise, move prev 
                prev = prev.next
            curr = curr.next
        
        return dummy.next



####################################################################
# 202. Happy Number
# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example: 

# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
####################################################################
class Solution:
    def isHappy(self, n: int) -> bool:
        '''
            Cycle detection: keep computing and detect if found cycle using fast and slow pointers
                similar to linkedlist cycle detection
            Using a hash map to store all visited number has a higher space cost
            Time    O(n)
            Space   O(1)
        '''
        
        def digitSquareSum(n):
            the_sum = 0
            tmp = 0
            while n != 0:
                tmp = n % 10
                the_sum += tmp ** 2
                n = n//10
            return the_sum

        slow, fast = n, n
        
        while True:
            slow = digitSquareSum(slow)
            fast = digitSquareSum(fast)
            fast = digitSquareSum(fast)
            if slow == fast:
                break
        
        return True if slow == 1 else False



####################################################################
# Pure storage: Onsite
####################################################################
''' Bitmap
    Given a parameter r2, where the equation x^2+y^2=r2 holds.
    Return a list of points that 
        (1) x and y are both integers
        (2) fits the circle equation
'''
####################################################################
from sets import Set

import profile


def draw_circle(r2):
    result = Set([])
    x = 1
    y = 0
    while x*x <= r2:
        for y in range(x+1):
            if x*x+y*y == r2:
                result.update(Set([(x,y),(x,-y),(-x,-y),(-x,y),(y,x),(y,-x),(-y,-x),(-y,x)]))
        x+=1
    return result

def draw_circle_bi_search(r2):
    result = Set([])
    x = 1
    y = 0
    while x*x <= r2:
        y_start = 0
        y_end = x
        while y_start <= y_end:
            y_mid = y_start+(y_end-y_start)/2
            if x*x + y_mid*y_mid == r2:
                result.update(Set([(x,y_mid),(x,-y_mid),(-x,-y_mid),(-x,y_mid),(y_mid,x),(y_mid,-x),(-y_mid,-x),(-y_mid,x)]))
                break
            elif x*x + y_mid*y_mid < r2:
                y_start = y_mid+1
            else:
                y_end = y_mid-1
                
                 
        x+=1
    return result

def draw_circle_O_n(r2):
    result = Set([])
    r_sqr = r2**2
    while x<y:
        f = x**2+y**2
        if f == r_sqr:
           result.update(Set([(x,y),(x,-y),(-x,-y),(-x,y),(y,x),(y,-x),(-y,-x),(-y,x)]))
           #move 
            y-=1
            x+=1
        elif f < r_sqr:
            x+=1
        else:
            y-=1
    return result

'''
    follow UP   
    outside     check   itself and lower one 
    inside  check itself and upper one 
'''
profile.run('print draw_circle(10000)')
profile.run('print draw_circle_bi_search(10000)')



####################################################################
''' buddy system bitmap
   Given a complete binary tree with nodes of values of either 1 or 0, the following rules always hold:
   (1) a node's value is 1 if and only if all its subtree nodes' values are 1
   (2) a leaf node can have value either 1 or 0
   Implement the following 2 APIs:
   set_bit(offset, length), set the bits at range from offset to offset+length-1
   clear_bit(offset, length), clear the bits at range from offset to offset+length-1
'''
####################################################################

def setbit_down(A, x, n):
   if x>=n:
       return
   if 2*x+1<=n and A[2*x+1]==0:
       A[2*x+1]=1
       setbit_down(A,2*x+1,n)
   if 2*x+2<=n and A[2*x+2]==0:
       A[2*x+2]=1
       setbit_down(A,2*x+2,n)
   

def set_bit(A, pos, length):
   if not A or pos<0 or length<=0:
       return
   n = len(A)-1    #last index of A
   for x in range(pos, min(n+1,min(pos+length, 2*pos+1))):
       # set self
       if A[x] == 1:
           continue
       A[x]=1
       # set descendants
       setbit_down(A,x,n)
       # set ancestors
       while x>0:
           # make sure its sibling is 1, if its sibling is 0, cannot set ancestors
           if (x%2==0 and A[x-1]==1) or (x%2==1 and x<n and A[x+1]==1):
               A[(x-1)/2] = 1
           x = (x-1)/2

def clear_bit(A, pos, length):
   if not A or pos<0 or length<=0:
       return
   n = len(A)-1    #last index of A
   for x in range(pos, min(n+1, pos+length)):
       # clear self
       A[x]=0
       # clear descendants
       while 2*x+1<=n:
           A[2*x+1] = 0
           x=2*x+1
       # clear ancestors
       while x>0:
           if A[(x-1)/2]==0:
               break
           A[(x-1)/2] = 0
           x = (x-1)/2

A=[0,  0,1,  1,0,1,1,  1,1,1,0,1]
set_bit(A, 1, 4)
print 'after setting bit from ', 1, 'for ', 4,'A is: ', A
A=[0,  0,1,  1,0,1,1,  1,1,1,0,1]
clear_bit(A,1, 4)
print 'after clearing bit from ', 1, 'for ', 4,'A is: ', A





