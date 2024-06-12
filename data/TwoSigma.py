#########################################
# 10/7     店面
# #########################################
# 今年第一场实习面试，不太顺利。

# 没想到，准备的的都没考, 唯一没准备的这题考了。

#     开始电话他打不通，之后那人讲的题目我知道是面经题目，于是也没认真听光顾着想面经，之后我也没听懂。而且没给很具体的题目，像其他面试官会copy paste一段题目，只给了两个简单地例子，而且属于design加coding，design方面确实比较薄弱，需要加强！

#     经过反思, 面试的准备尽力就好，面试的时候一定是要平常心！！！

#     首先, 要放下包袱，面试过于不过，都是成事在人，谋事在天，尽力就好。
#     不应该想着志在必得，也不应该者恐惧害怕。
#     面试很多客观环境的因素，比如面试官的气场聊不聊的来，面试题目的难易程度和自己对这类题型的数量程度，还有当时情绪状态等都相关。

#     其次, 是对于押题也应该是平常心，就算没压中也要拿得起放得下，紧跟面试官思路，专心思考当前的题目。    
#     还是应该先讲清楚思路，和准备用的数据结构和算法，非常忌讳上来就coding。面试官认可了之后再coding，不然会给人一种草率的印象，还是要复习下去年的宝贵经验。


# ########################################
# Generate a random number without Repeat 

#     给定min和max，每次call generate()都会生成一个在(min, max)范围内的随机数，
#     但是每个数字最多return一次。所有数字都用尽后重置。

# follow up是增加一个update(min, max)方法可以更新min和max，
#     但即使更新了之后也‍‌‍‌‌‍‍‍‍‌‌‌‍‌‍‌‌‍‍不能return已经return过的数。
#     还问了这个generator是不是thread safe，如果不用数组做怎么做



# # leetcode 380  基本就是维护一个数组和一个hash table。
# # 数组中是available的number，
# # hash table中记录每个数的index。
# # 每次random出一个数就 把这个数和数组最后一个数对换位置然后 pop from the end of array。

# 都用过之后reset一次，用过的顺序不再重复。
# EX        [2,6)    => 3, 4, 2, 5  => (reset) => 3, 2, 4, 5  => (reset)    ……..
# EX        [0,1)    => 0  => (reset) => 0 …….. 

# https://leetcode.com/problems/insert-delete-getrandom-o1/description/



#############################################################
# Random Number Generator without repeat
# 给定min和max，每次call generate()都会生成一个在(min, max)范围内的随机数，
# 但是每个数字最多return一次。所有数字都用尽后重置。

# follow up是增加一个update(min, max)方法可以更新min和max，
# 但即使更新了之后也‍‌‍‌‌‍‍‍‍‌‌‌‍‌‍‌‌‍‍不能return已经return过的数。
# 还问了这个generator是不是thread safe，如果不用数组做怎么做


# leetcode 380  基本就是维护一个数组和一个hash table。
# 数组中是available的number，
# hash table中记录每个数的index。
# 每次random出一个数就 把这个数和数组最后一个数对换位置然后 pop from the end of array。


import random

class RandomizedSet(object):

    def __init__(self):[]
        self.nums = []
        self.pos = {}
        
    def insert(self, val):
        """
        Inserts a value to the set. 
        Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False
        
    def remove(self, val):
        """
        Removes a value from the set.
        Returns true if the set contained the specified element.
        """
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop(); self.pos.pop(val, 0)
            return True
        return False
        
    def getRandom(self):
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


###############################################################
# coding
###############################################################
# 918. Maximum Sum Circular Subarray
# 电面：听口音是国人小哥，自我介绍说是manager。没什么废话，直接Maximum Circular Subarray Sum。
# 写完之后两个人陷入了尴尬。。于是开始不停的测testcase。。。
# 这时候我看离结束还有二十分钟灵机一动说我再给你解释一遍吧，对面迅速确认过眼神表示好的好的that's great.
# 然后我就把一共没几行的代码又口述了一遍成功磨掉了十分钟宾主尽欢皆大欢喜。

def maxSubarraySumCircular(A):     
    '''
    subarrays of circular arrays can be classified as either as
        one-interval subarrays,         ans1 = kadane(A)
        or two-interval subarrays.      ans2 = sum(A) + kadane(A_2)
                                        ans3 = sum(A) + kadane(A_3)

    recurrence: dp[j+1] = A[j+1] + max(dp[j], 0)
    
    Time O(n)
    Space O(1)     Did not modify A
    '''
    def kadane(gen):
        # Maximum non-empty subarray sum
        ans = cur = -30000
        for x in gen:
            cur = x + max(cur, 0)
            ans = max(ans, cur)
        return ans
    
    # If one-interval subarrays  (Ai + ... + Aj)
    ans1 = kadane(A)

    # IF two-interval subarrays, calc sum(A) - sum(B)   where B is (Ai+1 + ... + Aj+1)
    #   BUT if one of the two interval subarray [0, i] OR  [j, N-1] is empty.
    #   We can call Kadane twice: once on B with the first element removed, and once on B with the last element removed.
    ans2 = sum(A) + kadane(-A[i] for i in range(1, len(A)))
    ans3 = sum(A) + kadane(-A[i] for i in range(len(A) - 1))
    
    return max(ans1, ans2, ans3)


print(maxSubarraySumCircular([1,-2,3,-2]))      # single ele max        3
print(maxSubarraySumCircular([4,-2,3,-1]))      # one-interval subarrays    6
print(maxSubarraySumCircular([10,-3,5]))        # two-interval subarrays    15
print(maxSubarraySumCircular([4,-2,3,-3]))      # two-interval subarrays, B is the entire array     5
    




#######################################################
# 146. LRU Cache
from collections import OrderedDict  # == hashmap + PQ

class LRUCache():
    '''
        To maintain a LRU cache, want a PQ to maintain the priority of access
        and want a map to store the key-value pair.      
        !!! OrderedDict is a combine of the two !!!
    '''
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.orderedDict = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        
        get might not be true if key not existed in the map 
        """
        if key not in self.orderedDict:
            return - 1

        # if access this key once, want to move it to end
        self.orderedDict.move_to_end(key)
        
        return self.orderedDict[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        
        put is alwasy true, can always insert the key value pair
        """
        if key in self.orderedDict:
            # if access this key once, want to move it to end
            self.orderedDict.move_to_end(key)
        
        # Update the map: if key existed, then update, Else, just add a key-value pair
        self.orderedDict[key] = value
        
        # want to maintain the capacity, pop the most recently unused item iff over capacity
        if len(self.orderedDict) > self.capacity:
            self.orderedDict.popitem(last = False)  # The pairs are returned in LIFO order if last is true or FIFO order if false,

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



#######################################################
# 1048. Longest String Chain

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        '''
        !!! word1 is a predecessor of word2  IFF we can add Exactly ONE letter anywhere in word1 to make it equal to word2
        DP
        2   For each word, loop on all possible previous word with 1 letter missing.
                If we have seen this previous word, update the longest chain for the current word.
        3   Finally return the longest word chain.
        
        Time O(NlogNS)
        Space O(NS)
        '''
        dp = {} # map existed word TO the length of longest string chain
        
        # sort in alphebatic order
        words.sort(key=len)
        
        for w in words:
            # find the len of the longest string chain from its predecessor
            longest_chain_len = 0
            for i, c in enumerate(w):
                predecessor = w[:i] + w[(i+1):]
                
                # update the longest_chain_len ending with word w
                if predecessor not in dp:
                    longest_chain_len = max(1, longest_chain_len)
                else:
                    longest_chain_len = max(dp[predecessor] + 1, longest_chain_len)
                    
            dp[w] = longest_chain_len
                
        return max(dp.values())
    
    
    
    
