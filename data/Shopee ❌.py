# 简历 项目 挑战？
# debug最困难的部分？

# TCP 三次握手和四次分手？

# dirty read SQL 给例子？

# Python favorite lib？

# 主要用Private cloud？历史遗留问题。

# 主要工作方向？
#     缺人，只能做出来基本问题，没有人力做优化。
#     自己实现的 资源调度器 orchastrator 统一集中 container
#     cache storage  单机存储基于rest，distributed基于poxy
#     midware     log library 中心化storage 分类检索查询，定位问题。

# f(IP: str) => int32
# f("192.168.1.100") => 11000000101010000000000101100100 => 3232235876
#    192 => 11000000
#    168 => 10101000
#    1 =>   00000001
#    100 => 01100100

def float_t(b):
    # b = b.replace(" ","")  # 去除空格，测试用方便
    x = bin(eval('0x'+b))[2:] # 直接不能转，加0x才认
    if (len(x)<32): # 简单的补0操作
        x =  '0'*(32-len(x)) + x
    else:
        x = x
    if int(x[0])==1: # 符号位判断
        sign = -1
    else:
        sign = 1
    mi = 2 ** (int(x[1:9], 2)-127) # 幂指数
    xiao = 1
    for num,i in enumerate(x[9:]): # 小数部分，是1的位做2的-n次方全部累加
        if i == '1':
            xiao = 2**(-(num+1)) + xiao
    return sign * mi * xiao


    
def f(IP):
    
    arr = []
    start = 0
    end = 0
    for c in IP:        
        end += 1
        if c == ".":
            arr.append(IP[start:end-1])
            start = end
    arr.append(IP[start:])
    print(arr)
    binRes = ""
    for bucket in arr:
        # print(bin(int(bucket))[2:])
        binRes += str(bin(int(bucket))[2:])
    print(binRes)
    ln = 1
    dec = 0
    # binRes = int(binRes)
    # print(int(binRes)) 
    print(float_t(binRes))
    # while(binRes != 0):
    #     ln*=2
    #     dec += binRes%10 * ln
    #     binRes/=10
    # print(dec)
    # pos = 31
    # res = 0.0
    # for bucket in arr:
    #     for c in str(bin(int(bucket))):
    #         if c == "1":
    #             res += 2**(pos)
    #         pos -= 1
    # return res
       
print("res: ", f("192.168.1.100"))


# #######################################################
# # OS

# # 一、什么叫同步、异步：
# # 1、同步：同步操作没有结束之前，后面的代码是无法执行的。
# # 2、异步：异步操作没有结束之前，后面的代码是可以执行的。

# # 同步阻塞：打一个电话一直到有人接为止

# # 异步：打一个电话没人接，转到语音邮箱留言（注册），然后等待对方回电（call back)
# # 非阻塞：打一个电话没人接，每隔10分钟再打一次，直到有人接为止

# # 二、哪些是异步问题：
# # 1、计时函数：setTimeout()、setInterval()。
# # 2、资源加载（I/O操作）：在JavaScript脚本代码中动态加载资源。
# # 3、XHR请求：利用Ajax技术向服务器发出请求。


# #######################################################

# # 1   hash table 

# # key =>  hashing algorithm   =>  assiging to a bucket

#     # load factor =  n/k  if > 0.75 then rehashing 
#     #     n is the number of entries occupied in the hash table.
#     #     k is the number of buckets.

#     # Dynamic resizing ?
#     #     When an insert is made such that the number of entries in a hash table exceeds the product of 
#     #     the load factor and the current capacity then the hash table will need to be rehashed.

#     #     Rehashing includes increasing the size of the underlying data structure and mapping existing items to new bucket locations.

#     # HOW to solve collision ?
#     # 1    Separate chaining
#     #         Each bucket is independent, and has some sort of list of entries with the same index.
#     #         The time for hash table operations is the time to find the bucket (which is constant) plus the time for the list operation.

#     # 2  open addressing ?
#     # all entry records are stored in the bucket array itself. When a new entry has to be inserted, 
#     # the buckets are examined, starting with the hashed-to slot and proceeding in some probe sequence, until an unoccupied slot is found.

# #######################################################
# # 2   
# #     How to implement a set?

# #     visit a URL, what happen?

#         # You enter a URL into a web browser    “https://google.com”
#         # The browser looks up the IP address for the domain name via DNS   "google.com"
#         # The browser sends a HTTP request to the server
#         # The server sends back a HTTP response
#         # The browser begins rendering the HTML
#         # The browser sends requests for additional objects embedded in HTML (images, css, JavaScript) and repeats steps 3-5.
#         # Once the page is loaded, the browser sends further async requests as needed.

# #     what is a long connection and a short connection?

# #     can we use DNS server anywhere?

# #     how to know user IP?

# #     sort the file of numbers?
#     #     chunk and merge sort


# #######################################################
# # 3
# # garbage collection in Java? How often GC clean up memory?  

# # GC: Java programs perform automatic memory management(deleting objects created on heap) for programs running on JVM.

# # The garbage collection implementation lives in the JVM. 
# # Most popular one is Oracle's HotSpot.
# #     multiple garbage collectors that are optimized for various use cases, all its 
# #     garbage collectors follow the same basic process. 
    
# #     first, unreferenced objects are marked as ready for garbage collection. 
    
# #     second, marked objects are deleted. 
    
# #     finally, memory can be compacted after the garbage collector deletes objects, so remaining objects are in a contiguous block at the start of the heap. 

# #     The compaction process makes it easier to allocate memory to new objects sequentially after the block of memory allocated to existing objects.

# # peer to peer payment system

