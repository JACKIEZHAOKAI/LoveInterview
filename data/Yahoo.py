
############################################################
#   10/24   一面
'''
华人manager聊了半个钟简历project 还是解释failure testing怎么测availibility，project的impact是什么
问了uber 实习，深入问了failure test 的例子（没讲好？fail a jobmgr, reconnect）zookeeper
问了腾讯实习，代码高亮project  难点是setup js runtime 环境，而不是 高亮解析， 用highlight.js 外部库做
问了 tcp udp   区别是什么？     security：  tcp>udp and       speed udp>tcp         and why?
    example of udp applied on streaming?

FollowUp  Python String     s += c 是重新开创了空间 如何避免？
Solution:      use a list to store new char  and finally convert the  list to string 
    s = [ ]      
    Loop     s.append(c)
    s = ‘’.join(s)        # convert the  list to string

然后一道easy题目，但是细节没有处理好，edege case还有string concatenation。暴露了Python不扎实。。。
过了一天通知二面
https://leetcode.com/problems/string-compression/description/
'''
############################################################
# aaabbbcc => a3b3c2
# bbaabb => b2a2b2
# abc => a1b1c1
# aaa => a3
# a   => a1
# ""  => ""

def StringCompression(s):

    if s == "":
        return ""
    
    res = []
    counter = 1
    # traverse s and check number of each char 
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            counter += 1
        else:
            # append count to res and refresh counter 
            res.append(s[i]+str(counter))
            # # <==>
            # temp = str(s[i] + str(counter))
            # res = str(res + temp)
            
            counter = 1


    res.append(s[i]+str(counter))
    res.reverse()
    return "".join(res)


# print(StringCompression("aaabbbcc"))
# print(StringCompression("bbaabb"))
# print(StringCompression("abc"))
# print(StringCompression("aaa"))
# print(StringCompression(""))


############################################################
#   10/30   面经
'''
    5 min 自我介绍，
    Uber infra的简历讲的比较具体，也讲了failure test 对不同component和compute system 的架构吹一波

    5min 介绍题目并且分析
    对array 进行操作，很自然想到了DP 有O（n）解，于是说dp并且解释为什么不用time cost高的loop或者divide conquer
    其实也并不会loop和 DQ的解法
    
    5 min 打完思路
    先comment打了一波思路，思路很清晰，问是否可以implement，OK

    10min 写完代码并且主动跑完了test都过了    简单分析time space cost

    30min 真的蛋疼死了，follow up是把加进去的元素存下来并且return，我直接把元素加到dp list里面
    思路没问题，死活没想到python的list 是reference，必须创建新的copy不然整个list乱七八糟
    和面试官一起30min都没有debug出来，时间到了面试官说直接email给他debug的结果。

    面试过后，又花了30min把dp list 每次loop都打出来就发现了问题

    反思：
        1   题目思路先要讲清楚，再动手code，这是通过面试的必要条件！这一点要保持！
        2   follow up平时也要多练习！ 包括优化？ 任何题目可以问的follow up？
        2   debug 的能力还是要狠抓！   光是implement出框架还不够，还要在限时情况下也能冷静debug。
        
'''
############################################################

# Your previous Plain Text content is preserved below:
# 
# /* 
# Given an array of positive values, find the "maximally independent set", where
# an independent set is defined as a set of index elements such that no two elements are adjacent.
# 
# Maximally independent set is the set that has the maximum sum (of the elements).
# 
# [ 1, 4, 5, 4 ] ==> maximally independent set is [ 4, 4 ] . (indices 1 and 3)
# [ 1, 4, 5, 4, 6, 2 ] ==> maximally independent set is [ 1, 5, 6 ] (indices 0, 2 and 4)
# [ 10 ] => maximally independent set is [ 0 ] ==> value of 10
# [ 5, 8 ] => choose element [ 1 ] ===> value 8 
# */
# 
'''
  A: [ 1, 4, 5, 4, 6, 2 ] 
     
 dp [ [value] ...]
 
    [1],[4,],[6]]
 
 travere the A and expand dp 
 
    after index 1, at index i, array dp
    compare dp[i-2]+ A[i] and  dp[i-1] 
     1   update dp[i] = dp[i-1] 
     2   update dp[i] = dp[i-2]+ A[i] 
    
'''

def findMaxIndependenstSet(A):
    '''
    Time     O(n)    travere the array once 
    Space    O(n)    use a same size array dp to store info
    '''
    # check edge case 
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return A[0]
    if len(A) == 2:
        return A[0] if A[0] > A[1] else A[1]
    
    dp = [ A[0], A[1] ]

    for i in range(2, len(A)):
        
        if (A[i] + dp[i-2]) > dp[i-1]:
            dp.append( (A[i] + dp[i-2]) )
        else:
            dp.append( dp[i-1] )
    
    return dp[-1]

                           # dp  1  4  6  8  8  8  8  16 20  20
# print(findMaxIndependenstSet([ 1, 4, 5, 4, 0, 0, 0, 8, 12, 1 ]))
# print(findMaxIndependenstSet([ 1, 4, 5, 4 ]))            # 8
# print(findMaxIndependenstSet([ 1, 4, 5, 4, 6, 2 ]))      # 12
# print(findMaxIndependenstSet([ 10 ]))                    # 10
# print(findMaxIndependenstSet([ 5, 8 ]))                  # 8


def printEntries(A):
    # check edge case 
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return A[0]
    if len(A) == 2:
        return A[0] if A[0] > A[1] else A[1]
    
    dp = [ (A[0],[A[0]]), (A[1],[A[1]]) ]
    # res = []
    
    for i in range(2, len(A)):

        pp_val, pp_list = dp[i-2]
        p_val, p_list =  dp[i-1]
    
        if (A[i] + pp_val) > p_val:
            '''
            The bug is caused here by Python list:

            pp_val, pp_list = dp[i-2] only obtain a ref to the pp_list in dp[i-2]   insteaf of creating a new list instance,            which cause problem is updating the list.

            To solve the problem, I need to create a new list instance of pp_list
            '''
            new_pp_list = pp_list[:]          # create a new list instance !!!
            new_pp_list.append(A[i])       # append to the new list
            dp.append( (A[i] + pp_val, new_pp_list) )
        else:
            dp.append( (p_val, p_list))

    return dp[-1][1]

               # dp  1  4  6  8  8  8  8 15  20  20
print(printEntries([ 1, 4, 5, 4, 0, 0, 0, 7, 12, 1 ]))  # 4,4,12
print(printEntries([ 1, 4, 5, 4 ]))            # 4,4
print(printEntries([ 1, 4, 5, 4, 6, 2 ]))      # 1,5,6
print(printEntries([ 10 ]))                    # 10
print(printEntries([ 5, 8 ]))                  # 8
# paased





