
#############################################################################
# 7/22  HR chat
# 2021 收购了Uber ATG, perception 组主要用 Python 和C++， Nuro 和 Aurora 都是Waymo
# Position： perception 底下的platform，support 其他组的ML算法
# 不支持fully remote，希望员工住在office附近


#############################################################################
# 7/30  烙印店面

#   nums of island
    #   3min讲清楚思路 太简单了
    #   5min 写清楚 dfs（recursive/ stack 优劣） bfs 
    #   10min coding + 10 min fix bug， 用visited省space和直接改input的解法都写一下

# non tech and tech challenge and how to overcome  这个没准备好 !!!
#   这个好难回答。回答重点要落在 WHAT DID YOU LEARN???
#   实事求是说了严重的腿伤以为不能走路，到漫长的康复，归根结底是要keep hope，永远对生保持希望。
#   tech的话说工作过程中发现和学校project的gap，强调需要很多cooperation和主动reach out resouce

#############################################################################
'''
# VO
1 resume deep dive + 2 coding + 1 mgr chat(system) + HR chat 
    10:00AM (PDT) - 11:00AM (PDT): Claudio Santana Saldana (Senior Software Engineer)
    11:00AM (PDT) - 12:00PM (PDT): Rachel Gardner (Software Engineer II), Philip Yang (Senior TL, Perception - ML Platform)

    1:30PM (PDT) - 2:30PM (PDT): Thang Dinh (Senior Software Engineer)

    2:45PM (PDT) - 3:30PM (PDT): Alvin Auyoung (Staff TLM, Perception - Datasets)
    3:30PM (PDT) - 3:45PM (PDT): Mukta Goel (Staff Recruiter) VC Walkout / Questions
'''
#############################################################################
# 第一轮：  Deep dive into resume, backend general +  System Design

#     Redis? How to improve reliability

#     how to improve system reliability

#     Zookeeper

#     message-based interaction
    
#     What is RPC(Remote procedure call)?

#     message queue sprintboot
    
#     how to handle async task

#     What is SDDC?
    # marketing term that extends virtualization concepts such as abstraction, pooling, and automation to all data center resources 
    # and services to achieve IT as a service (ITaaS).[1] In a software-defined data center, 
    # "all elements of the infrastructure — networking, storage, CPU and security – are virtualized and delivered as a service.

#  Core architectural components that comprise the software-defined data center[5] include the following:
    # computer virtualization,[6] - a software implementation of a computer
    # software-defined networking (SDN), which includes network virtualization - the process of merging hardware and software resources and networking functionality into a software-based virtual network[5]
    # software-defined storage (SDS), which includes storage virtualization, suggests a service interface to provision capacity and SLAs (Service Level Agreements) for storage, including performance and durability
    # management and automation software, enabling an administrator to provision, control, and manage all software-defined data-center components[7]

#############################################################################
# 第二轮: 港科大 PHD   Coding 
'''
Aurora Coding 2

// Robust min: second smallest number of a collection
// E.g.: [2,2,2,3,4] -> RobustMin = 2

#// Example: The robust min for a window of 3 in a sequence 15, 8, 7, 10, 9 is 9.
// it is not 8 because that's outside of the window.
// it is not 7 because that's the minimum, not the robust min.

// window_size = 3
// add(15) | [15] -> 15
// add(8)   | [15, 8] -> 15
// add(7)   | [15, 8, 7] -> 8
// add(10) | [8, 7, 10] -> 8
// add(9)   | [7, 10, 9] -> 9
'''

class RobustMinFinder:
    """
    Compute the robust minimum (second-smallest value) for
    a sliding window over the input.
    """

    def __init__(self, window_size):
        self.list = []
        self.window_size = window_size
        
    def add(self, y):
        """Adds the next sample value and returns the robust min in the current
        window. When the total number of samples is less than the window size, this
        returns the robust min of all samples seen so far.

        Args:f
            y (int): the next sample value
        Returns:
            The robust minimum of the most recent `window_size` samples, including
            the new sample.
        """
        def findSecMin(arr):
            smallest = second = float('inf')
            for i in range(len(arr)):
                smallest = min(smallest, arr[i])
            # Find the second largest element
            for i in range(len(arr)):
                if (arr[i] != smallest):
                    second = min(second, arr[i])
            return second
        
        self.list.append(y)

        if len(self.list) == 1:
            return self.list[0]

        if len(self.list) > self.window_size:
            self.list.pop(0)
        
        return findSecMin(self.list)      # O(K) * N     k=window_size       ==> O(1) ???   

        # return -heapq.nlargest(2, self.list)[1]     # O(K + Klog2) * N     k=window_size
        
        # return sorted(self.list)[1]     # O(KlogK * N)   k=window_size


finder = RobustMinFinder(3)
print(finder.add(15))
print(finder.add(8))
print(finder.add(7))
print(finder.add(10))
print(finder.add(9))


#############################################################################
# 第三轮: 越南 USC PHD  Coding 

# The Aurora Atlas is our HD Map system which contains information about the world. From a birds-eye-view perspective, 
# we know the height of the road at every x,y point. We want an algorithm which can detect potholes in the road.
#
# Consider a flat region of the world where the normal road is at height 0 and every pothole is at height -1. 
# We have a 5m X 5m grid of heights with cells of size 1m. Write a function to find the distance to the nearest pothole in the road.
#
# EXAMPLE
#  INPUT
# [ 0, 0, 0, 0, 0]
# [-1,-1, 0, 0, 0]
# [-1, 0, 0,-1, 0]
# [ 0, 0,-1, 0, 0]
# [ 0,-1,-1, 0, 0]
# 
#  OUTPUT: 
# [1,1,2,2,3]
# [0,0,1,1,2]
# [0,1,1,0,1]
# [1,1,0,1,2]
# [1,0,0,1,2]

def potholesDistance(HDmap):

    def BFSDrawDistance(HDmap):
        n = len(HDmap)
        queue = []
        visited = set()                    # (x,y)
        queue.append([HDmap[0][0], 0, 0])    # (x,y,value)   => pothole?
        print(queue)
        while queue:
            x,y,val = queue.pop(0)
            print(queue)
            if (x,y) not in visited:
                visited.add((x,y))
                for (X, Y) in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                    if 0<= X < n and 0<= Y < n:
                        if HDmap[X][Y] == -1: 
                            queue.append((0, X, Y))
                            visited.pop(X, Y)
                        if HDmap[X][Y] != -1:
                            queue.append((HDmap[X][Y]+1, X, Y))
    return HDmap

print(potholesDistance([[0,0],[-1,0]]))


# 542. 01 Matrix
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.

# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Input: mat = [[0,0,0],
#               [0,1,0],
#               [1,1,1]]
# Output: [ [0,0,0],
#           [0,1,0],
#           [1,2,1]]




#############################################################################
# 第四轮:  UCSD PHD     Hiring Manager
# 这一轮就是纯扯淡 深挖对系统的理解

# Non-Tech
# 1. what you are looking for in your next role?

# 2. why Aurora?   


# Tech
# 1.随便问简历的项目。what at Uber ATG?
#   Peloton -- workload     ==> Deep dive
#       aggregates compute resources from a collection of physical hosts into a shared resource pool, 
#       amplifying compute power and allowing for the flexible use of data center hardware.
#       https://www.uber.com/blog/resource-scheduler-cluster-management-peloton/

#   What problem does Peloton solve?    
#       N job manger => resouces manager <= N cluster manager -- Meso cluster

#   what is a job?

#       Stateless jobs are long-running services without persistent states. 处理请求的服务  EX UDP , DNS , HTTP 

#       Stateful jobs are long-running services, such as those from Cassandra, MySQL, and Redis, that have persistent state on local disks. 需要数据库的服务 FTTP , Telnet , etc.

#       Batch jobs typically take a few minutes to a few days to run to completion. There is a broad category of batch jobs for data analytics,
#        machine learning, maps, and autonomous vehicles-related processing, emanating from software such as Hadoop, Spark, and TensorFlow. 
#       These jobs are preemptible by nature and less sensitive to short-term performance fluctuations due to cluster resource shortages.  批处理的工作  no other interaction by the user is required to process the batch


# 2.深挖一个近期的项目VMware

#   Alert processor 简单好理解，但是没有技术深度，就是普通的后端服务处理JSON请求

#   2.1. What can be a good future improvement? pros and cons?
#           cache the SDDC infoamtion
#               pros: save time in querying the SDDC   

#               cons: cached SDDC info may not be updated

# 本地缓存与分布式缓存的优缺点、适用场景与实现分析
# https://ost.51cto.com/posts/1002
    # 1. 访问速度快，但无法进行大数据存储
    # 本地缓存相对于分布式缓存的好处是，由于数据不需要跨网络传输，故性能更好，但是由于占用了应用进程的内存空间，如 Java 进程的 JVM 内存空间，故不能进行大数据量的数据存储。

    # 2. 集群的数据更新问题
    # 与此同时，本地缓存只支持被该应用进程访问，一般无法被其他应用进程访问，故在应用进程的集群部署当中，如果对应的数据库数据，存在数据更新，则需要同步更新不同部署节点的本地缓存的数据来包保证数据一致性，复杂度较高并且容易出错，如基于 Redis 的发布订阅机制来同步更新各个部署节点。

    # 3. 数据随应用进程的重启而丢失
    # 由于本地缓存的数据是存储在应用进程的内存空间的，所以当应用进程重启时，本地缓存的数据会丢失。所以对于需要持久化的数据，需要注意及时保存，否则可能会造成数据丢失

#   2.2. what is the most challenging part of the project?

#  3. cooperation and how to solve it?
#   technical disagreement with colleage? and how to solve it?  



