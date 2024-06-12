####################################################
'''
    Apple CF on campus 10月初     之后收到拒信
    # 题目虽然很简单，但是开始浪费了时间在想其他的solution
    # Edge case 处理的很糟糕， 比如正负相除如何handle，divice by 0
    # 细节还是要注意： edge case，代码干净整洁，步骤清晰， 走testcase  
'''
####################################################

# Do not use "/" "+" "%" to calc division 
# only calc the exact division
# EX  -8 / -3 = 2
#   8 / 3 = 2
#   8 / -3 = -2
#   8 / 0 = 2

def divide(denominator, numerator):

    # edge case check 
    if numerator == 0:
        print(" error, divide by 0")
        return -1

    # convert to positive 
    is_neg1 =  True if denominator < 0 else False
    is_neg2 =  True if numerator < 0 else False
    numerator, denominator = abs(numerator), abs(denominator)

    if numerator > denominator:
        return 0

    division = 0
    running_sum = numerator
    while running_sum < denominator:
        running_sum +=  numerator
        division += 1

    if (is_neg1 and is_neg2) or (not is_neg1 and not is_neg2):
        return division
    else:
        return -division

print(divide(8, 3))     # 2
print(divide(8, -3))    # -2
print(divide(-8, 3))    # -2
print(divide(-8, 0))    # error






####################################################
'''
#  Winter Careerfair拿到面试电面过程    Icloud组

# 面我的居然是个iphoto 16才本科毕业工作三年的小姑娘，好像表现的还比较热情聊天
# 聊简历，扯 分布式文件系统 很match他们的iphoto 开始聊的还ok

# LRU cache，妈蛋不给用python的库OrderDict，因为小姑娘用java估计解法也是java版本
# 看来这道超热题目一定要准备 Double LL + Hashmap的通解 ！！！ 

# 于是乎只能现搜LC解法还不能用答案的容易曝光，瞎几把边读代码边理解边写，很怕穿帮
其实店面最容易穿帮的还是开始聊解题思路，之后写代码其实面试官都不一定跟得上我的思路，就是瞎点头
故意拖延思考一步步还是连理解带写把代码敲完了  先implement LL的methods，然后put，最后get
稍微handle一下put  reach capacity 的edge case就好

最后五分钟尬聊iphoto干啥，后端服务主要是分布式，不涉及用户前端photo的人脸识别啥的，结果不好说。。。
但是至少比上次on campus还是好很多了的，题目也准备了LC高频的LRU

过了一周通知过了第一轮，哈哈
'''

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

"""
cacacity = 3
cache.put(1,-1)
cache.put(2,-2)
cache.put(3,-3)

cache.get(2) --> -2 

cache.put(4,-4) 

# cache should hold 2,-2; 3,-3; and 4,-4

https://leetcode.com/problems/lru-cache/solution/
"""

from collections import OrderDict    # == hash + PQ

class  Node:
    def __init__(self):
        self.key = 0 
        self.value = 0 
        self.prev = None
        self.next = None
        
class LRUCache(object): #least recently used cache 
    
    def addNode(self, node):
        # add new node right after curr node
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = None
    
    def removeNode(self, node):
        # remove a node if reach out capacity 
        prev = node.prev
        theNext =  node.next
        prev.next = theNext
        theNext.prev = prev
    
    def moveToHead(self, node):
        # call get / put, move to head 
        self.removeNode(node)
        self.addNode(node)
        
    def removeTailNode(self)
        # rm the node when it reach capacity
        res = self.tail.prev
        self.removeNode(res)
    
    # least recent use, get put to access, prioritize 
    # PQ + HM      front     array/list
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}    # key val pair
        self.capacity = capacity
        self.size = 0
        
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key)
        # check if key existed
        if not node:
            raise "not existed"
        
        # prioritize to front 
        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.cache.get(key)
        
        # key exist OR not
        if not node:
            # add new node
            newNode = Node()
            newNode.key = key
            newNode.value = value
            
            # update map and LL 
            self.size += 1
            self.cache[key] = newNode
            self.addNode(newNode)
            
            # check reach capacity 
            if self.size > self.capacity:
                # pop the tail node
                removedtail = self.removeTailNode()
                del self.cache[removedtail.key]
                self.size -= 1
        else:
            # update it 
            node.value = value
            # prioritize to front LL
            self.moveToHead(node)


####################################################
# 第二轮 coding不够思路清晰
# 没有过 

'''
    create a buffer class

    new buffer(1000000000000000); > lst('0','0', ... )

    write(data, offset) > lst()
       generate data into map 
    
    read(offset, length)
       buf = []
       reconstruct data    
    
    ['0', '0', '0', '0', '0']
    write(['a','b'], 2) 
    
    <O(N)
    
    1024    block size 
    calc block      
    start = offset//block size
            length//block size
    
    Q Where To store the block? in memory, but only store the part required
        map     blockNumber => data    # use metadata for distributed sys
    EX
        [000 | 0092139 | 210000]
        10, 3456 -> [...000010000..]        3456 // 1024 =  3  .... a       # 1024-a-2
'''

class buffer():
    def __init__(self, size):
        self.size = size
        self.map = {}    # map block# to list
        self.blockSize = 1024
        
    def read(self, offset, length):
        blockStart = offset//self.blockSize
        blockStartOffset = offset-blockStart*self.blockSize
        blockEnd = (offset+length)//self.blockSize
        blockEndOffset = (offset+length) - blockEnd*self.blockSize
        
        buf = []*length
        
        # check 
        if (offset<0 or offset>self.size*self.blockSize):
            throw 
        # single block 
        if 
            buf += [blockStartOffset:blockEndOffset]
            
        for index,block in enumerate(blockStart,blockEnd+1):
            if index == 0:
                if block in self.map:
                    buf += self.map[block][blockStartOffset:]
                else:
                    buf += [0]* blockStartOffset
            elif index == (blockEnd-blockStart):
                if block in self.map:
                    buf += self.map[block][:blockEndOffset]
                else:
                    buf += [0]* blockEndOffset
            else:
                if block in self.map:
                    buf += self.map[block]
                else:
                    buf += [0]* self.blockSize
        
        return buf


