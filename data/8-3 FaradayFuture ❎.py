# Faraday Future (练手)	– interviewing
# 4 rounds tech (2 coding + 2 BQ)  实际上面试乱七八糟，基本就是随便聊简历
'''
  7/5  非常不专业的   HR chat
  Background
    H1b transfer (working with VMware; back in August; wait for 1 month for H1b transfer, so at earliest in Sep)
  Position
    Junior SDE 2 in the simulation and test team	 小公司级别会拉高一级
    position San Jose (on-site)
  Compensation:
    115K + 115K/4 years	==》 13W	想都不用想了不去
  Interview process


  7/19 	Manager interview 	@Jerry Cao 	一面
  自动驾驶团队 20+  Silicon Vally Software engineer 不需要经常出差
  说目前走上正轨 HAHAHA, 准备10月份, 豪华车发布，笑死
  Now manager simulation project
    sensor model simulate量产车的加速度、转弯半径、大小等
    simulation 目前只是测试 ADAS算法。还只是辅助工具。可以再去开发perception的东西 就是目前没有，说明现在这个自动驾驶团队啥也没有！！！
    后期开发算法  perception: yolo => objection detection ; unsupervised learning
  
  7/22 	BQ interview
  随便聊了下  700 +   3 层
    machenical engineers 车厂 in LA
    一小部分人在北京 cloud/ infra
     Software in Silican valley, calibration;  
    FF is US based.	Tiktok, AutoX, Didi based China 会比较累
 
  恒大资金链断裂导致股价暴跌
  SLAM / motion planning control 真车上的闭环测试
  9am — 5 pm 	7-8hr a day

  7/22 	Tech interview
  Simulation + Embeded system  做real time 计算
    work with PnC; perception数据量大;  hardware 接口调用 
    C++ 80%
    “Real time system” 和计算机的系统不太一样。
        ROS based: 国防部开发的通信机制，不用protobuf。ros节点。
        DDS (data distributed service): https://www.rti.com/products/dds-standard
        ROS 2 integrate ROS and DDS
    不跨组调用，基于RosToMessage 应用层，不涉及模块调用。以后可能会更改middleware， DDS
  硬件供应商, 数据格式和通信都是和硬件打交道。
  Interview
    Namespace: https://docs.microsoft.com/en-us/cpp/cpp/namespaces-cpp?view=msvc-170
    Shared pointer: https://01io.tech/unique_ptr-vs-shared_ptr-vs-weak_ptr/

  7/26 	Tech interview
    Leetcode: Same Tree: https://leetcode.com/problems/same-tree/
    Cloud team (hiring freeze)  @ Santa Clara 
    招聘比较迷，非常不正规，这个人聊天生无可恋。。。
    他说 ADAS 自动驾驶 待遇可能还好一些。。。Simulation C++ / scripting。
    工具类的东西能覆盖到，PnC 和算法用的也不是自己写的，都是买的解决方案（包括PnC的程序都有，只需要调参和修改）。。。很少自己设计算法。

  # 8/4 	Tech interview
  # 这傻逼缺乏面试经验 也不会引导，就扔一个题上来做 花了太久时间理解题目，以为是graph的题。。。
  # Greedy + Binary search :Google - Optimally utilized travel distance
  # 2-3 weeks pick up C++  确实 tech C++面的不太好，表现得完全生疏！！！

'''

def find_opt_route(forwardList, backwardList, maxDistance):

  dis = 0
  ids = [0, 0]

  if forwardList == [] or backwardList == []:
    return [0, 0]  

  if len(forwardList) == 1 or len(backwardList) == 1:
    return [0, 0] 
    
  forwardList = sorted(forwardList, key = lambda x: x[1])
  # print("forwardList", forwardList)
  
  def find_cloest_index(forwardList, target):
    low, high = 0, len(forwardList)-1
    while low < high:
      mid = (low+high) //2
      if target < forwardList[mid][1]:
        high = mid - 1
      elif target > forwardList[mid][1]:
        low = mid + 1
      else:
        return mid
    if forwardList[high][1] <= target:
      return high
    return high - 1 
       
  for (bid, route) in backwardList:
    i = find_cloest_index(forwardList, maxDistance - route)
    # print("bid, route", bid, route)
    # print("index", i)
    if dis < route + forwardList[i][1] <= maxDistance:
      dis = route + forwardList[i][1]
      ids = [forwardList[i][0], bid]
  
  return ids


# # empty list
print(find_opt_route([[]],[[]], 100))
print(find_opt_route([[1,100]], [[]] , 100))
print(find_opt_route([[]],[[1, 100]], 100))

# # # sum overflow 
print(find_opt_route([[1,200]],[[1,100],[2,200]], 200))

# change of original list
print(find_opt_route([[1,3000],[2,5000],[3,4000],[4,10000]],[[1,2000],[2,3000],[3,4000]], 10000))
print(find_opt_route([[1,3000],[2,5000],[3,4000],[4,10000]],[[1,2000],[2,3000],[3,4000]], 8000))
print(find_opt_route([[1,3000],[2,5000],[3,4000],[4,10000]],[[1,2000],[2,3000],[3,4000]], 2000))
print(find_opt_route([[1,3000],[2,5000],[3,4000],[4,10000]],[[1,2000],[2,3000],[3,4000]], 3000))


# n: length of forwardList
# m: length of backwardList

# O(nlog n) in sorting forwardList
# O(mlog n ) in traversing backwardList and binary search for forwardList
# Time complexity: O(n log n + m log n) = O( (m+n) log n)

# Space O(1) if can modify forwardList, otherwise O(n) for storing forwardList





