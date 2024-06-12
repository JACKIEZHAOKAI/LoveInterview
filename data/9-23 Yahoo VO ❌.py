'''
9/23 VO
    (11:30 PM PST - 12:30 PM PST) - Amar Ramesh Kamat       Coding?
    (1:00 PM PST - 2:00 PM PST) - Andrey Ter-Zakhariants    Coding?
    (2:30 PM PST - 3:30 PM PST) - Atish Datta Chowdhury     Manage BQ

    Yahoo喜欢考Array String处理的简单题目, 一般两道题
'''

##########################################################
'''
Basic Question

    1. what happens when click URL?

    2. How to ensure security?

    3. Thread 	VS	Process
        A process, in the simplest terms, is an executing program. One or more threads run in the context of the process.
        A thread is the basic unit to which the operating system allocates processor time. A thread can execute any part of the process code, 
        including parts currently being executed by another thread

    Question : Write a program that takes 2 strings as inputs and prints all possible common substrings within those strings.


Q1  Examples: 
"abcd", "a" -> ["a"]
"abcd", "axyz" -> ["a"]

"abcd", "ab" -> ["a", "ab", "b"]
"abcd", "xbcy" -> ["b", "bc", "c"]
"abcdabxy", "ab" -> ["a", "ab", "b"]
"abxyabcmnabcd", "abcd" -> ["ab", "abc", abcd"]


Q2  Write a function to compute string similarity.
input: 2 strings
output: [0,1]

abcd, abcd => 1.0 < highest
abcd, abce => 0.75 < high
abcd, wxyz => 0.0 < lowest
abcd, zabc => 0.75
zabc, abcd => 0.75
abcd, axyz => 0.25 < low
abcd, dcba => 0.25
a, abcd    => 0.25

ac, abcd    => 0.25 ?


highest > high > low > lowest


string1
 
string2
 
1 compare length, longer string as base string
	a, abcd    => 0.25

2 traverse shorter on on the longer one, 
find the Longest common substring using Dymamic programming
compute the percentage over the base string
	
	len(ab), len(abcd)    => 0.5
'''
def lengthOfLongestSubstring(x, y):
 
   longestLen = 0
   longestSubstring = ""
   dp = [[0] * (len(y)+1) for _ in range(len(x)+1)]
   print(dp)
   for i in range(len(x)):
       for j in range(len(y)):
           if x[i] ==  y[j]:
               dp[i+1][j+1] = 1 + max(dp[i][j], dp[i+1][j], dp[i][j+1])
               if longestLen < dp[i+1][j+1]:
                   longestLen = dp[i+1][j+1]
                   longestSubstring = x[i+1-longestLen: i+1]
           else: 
                dp[i+1][j+1] = 0
 
   return longestSubstring
 

print(lengthOfLongestSubstring("abcdebb", "acdeab"))    # cde


##########################################################
'''
墨西哥老头？
    1.    C++ Coding

    2.    Desing

'''








##################################################################################################
'''
8/30 店面	PASS
    Counting Anagrm 很简单

    followup问 
        怎么做hashing    MD5
        如果input很长怎么做scaling
        Aws knowledge, AWS具体会什么
        Java
'''
# phone interview 

# 49. Group Anagrams
# Input: strs = ["eat","tea","tan","ate","nat", "bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupingAnagram(strs):
    hash_map = {}   # map key to the anagrams
    res = []

    if strs == None or strs == []:
        return []

    for s in strs:
        if s == None:
            continue
        key = ''.join(sorted(list(s)))
        if key not in hash_map:
            hash_map[key] = [s]
        else:
            hash_map[key].append(s)
    
    # construct the result list
    for key, s_list in hash_map.items():
        res.append(s_list)
    return res

# print(groupingAnagram(["eat","tea","tan","ate","nat", "bat"]))
# print(groupingAnagram(["01", "10", "00"]))
# print(groupingAnagram(["a", "", "aa", "bb"]))
# print(groupingAnagram([]))
# print(groupingAnagram(None))

'''
    Follow Up

    1. desing hashing fucntion? MD5
    cache:
    md5(strs) : {res: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]}

    Standard java practise, is to simply write
        final int prime = 31;
        int result = 1;
        for( String s : strings )
        {
            result = result * prime + s.hashCode();
        }

    2. how to do scaling to handle large data input?
    strs =["aaa", ........ 40 millions.....["aa"]]
    blocking and send to many services 

        2.1 potentional problem
        1, storing 
        2. compute
        3. network

    Q&A
    provide APIs, platform team. Own cloud moving to AWS

    Image Classifier

    Scalbility

    Java Spring, Python flask--Tensorflow, Gunicorn, , protobuf

    Multi-stage Docker: 
        A multistage build allows you to use multiple images to build a final product.
        In a multistage build, you have a single Dockerfile, but can define multiple images inside it to help build the final image.
'''


################################################################################################
# Virtual Onsite:
# 1. coding -> two sum,
#                 -> remove same two neighbors : "abbcccbbc" == "a"

# 2. coding -> count ways to concatenate two strings which equals target : ["ABC", "23", "777", "7", "77", "77"], target = "7777", output = 4
#                 -> optimize to O(n) time, optimize to O(k) space, k <= n, optimize to ..., optimize to ...

# 3. coding -> call GET API to an endpoint, retrive a JSON object, process it, POST the result to another endpoint

# 4. bq -> disagree with coworker?
#          -> walk through your resume
#          -> ideal team?
#          -> biggest su‍‌‍‌‌‍‍‍‍‌‌‌‍‌‍‌‌‍‍ccess yet to date
#          -> ...