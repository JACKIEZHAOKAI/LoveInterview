# 字节一面
##################################################################
# 深圳：电商 游戏 教育 lark/飞书
# 支持中台服务
# 技术栈：工程 golang，java少，算法组C++ python

# 牛客网很糟糕，网络断断续续卡了很久，稳了三四十分钟的基础概念。
# 面的不好MySQL都不会写query 而且最后开放问题求中位数也没说出来，
# 但可能因为基本的OS概念还能回答，而且算法第一题实现的也很快，最后通知过了。

# 收获:
# 遇到不会的千万不要紧张，有点印象的概念先圆场说自己的理解，快速查询理解再补充说明。
# 实在没印象的概念先说思考下，快速查询还是看不懂可以猜，或者放弃。

# OS:
# 	守护进程 孤儿进程 僵尸进程 
# 		Ref:	https://blog.csdn.net/yuwenliang/article/details/6770750
# 		僵尸进程是当子进程比父进程先结束，而父进程又没有回收子进程，释放子进程占用的资源，
# 		此时子进程将成为一个僵尸进程。如果父进程先退出 ，子进程被init接管，子进程退出后init会回收其占用的相关资源

# 	虚拟内存？
# 		虚拟内存是计算机系统内存管理的一种技术。它使得应用程序认为它拥有连续的可用的内存（一个连续完整的地址空间），而实际上，它通常是被分隔成多个物理内存碎片，还有部分暂时存储在外部磁盘存储器上，在需要时进行数据交换。目前，大多数操作系统都使用了虚拟内存，如Windows家族的“虚拟内存”；Linux的“交换空间”等
# 		物理内存分配算法？
# 		如何处理碎片问题？	 paging


# Database:
# 	乐观锁 悲观锁？
# 	PCC:	当要对数据库中的一条数据进行修改的时候，为了避免同时被其他人修改，最好的办法就是直接对该数据进行加锁以防止并发。
# 			这种借助数据库锁机制，在修改数据之前先锁定，再修改的方式被称之为悲观并发控制【Pessimistic Concurrency Control，缩写“PCC”，又名“悲观锁”】。
# 	OCC:	乐观锁是相对悲观锁而言的，乐观锁假设数据一般情况下不会造成冲突，所以在数据进行提交更新的时候，才会正式对数据的冲突与否进行检测，
# 			如果发现冲突了，则返回给用户错误的信息，让用户决定如何去做。乐观锁适用于读操作多的场景，这样可以提高程序的吞吐量。

# 	数据库并发控制:
# 		悲观锁(PCC):先取再访问，保证数据安全。 
# 		乐观锁(OCC):假设用户处理的并发事物之间不会产生相互影响，在事务提交以前，每个事务 检查该事物读取数据后，有没有其他事务又修改了数据。
# 		如果有其他事务更新的话，正在提交的 事务会进行回滚。一般实现乐观锁的方式是记录数据版本。

# 	MySQL 底层实现? 
# 		B+ tree
# 			B+树是B树的一个升级版，数据只能存储在叶子节点。
# 			相对于B树来说B+树更充分的利用了节点的空间，让查询速度更加稳定，其速度完全接近于二分法查找。
# 			https://www.jianshu.com/p/4dbbaaa200c4		#数据库索引为什么使用B+树？
# 			https://zhuanlan.zhihu.com/p/27700617		#平衡二叉树、B树、B+树、B*树 理解其中一种你就都明白了
# 		时间复杂度 logN
# 		可否用红黑树代替?
# 		补充：各种树的应用场景
# 			AVL树： 平衡树 windows的地址空间管理
# 			红黑树：C++ STL map和set的实现
# 			B/B+树：磁盘文件，数据库索引
# 			Tries：统计和排序大量字符串，自动机。

# 	怎么设计索引:
# 	select name from table where city = xx and age > 50		
# 	#	name city age	联合索引
# 	#	CREATE INDEX indexName ON tableName(column1,column2,...,columnN);
# 	#	CREATE name ON tableName(name, city, age)
# 	ref:	https://draveness.me/sql-index-intro/

# 语言特性：
# 	Java violate?
	
# 	Java锁的底层实现？如何保证原子性atomic？

# 	分布式锁？


# 题目
# 1.	num of island 

# 2.	只要思路：一个如果在无序超大数组求中位数？	Bubble sort



# 字节二面
##################################################################
# 一个胖子有点节奏比较快，不懂得内容现查消化不来有些紧张，面到后边沟通不顺利。

# 收获:
# 1.简历自我介绍和项目介绍还是需要下功夫好好准备（最感兴趣的项目的内容？难点？）
# 2.对于基础概念还是需要有比较充分的准备（常考OS概念的归类总结）

# 项目介绍太长时间了，根据项目相关技术的followup回答吃力
# 	动态库的原理？
# 	静态库vs动态库？
# 		DLL(Dynamic Linkable Library)的概念，你可以简单的把DLL看成一种仓库，提供给你一些可以直接拿来用的变量、函数或类。 
# 		静态链接库与动态链接库都是共享代码的方式，
# 			如果采用静态链接库，则无论你愿不愿意，lib中 的指令都被直接包含在最终生成的EXE文件中了。
# 			若使用DLL，该DLL不必被包含在最终的 EXE文件中，EXE文件执行时可以“动态”地引用和卸载这个与EXE独立的DLL文件。
# 		采用动态链接库的优点:
# 			(1)更加节省内存;
# 			(2)DLL文件与EXE文件独立，只要输出接口不变，更换DLL文件不会对EXE文件造成任何影响，因而极大地提高了可维护性和可扩展性。

# OS：
# 	fork 父子进程的资源访问？
# 		之后才反应过来时共享内存，followup应该就是问锁

# 	虚拟内存的主要作用？	可以再提炼下

# 	文件系统的底层实现？	忘了

# 语言特性：
# 	垃圾回收机制？			表达不出来


# 智力题目
# logic:   
#     (blk, white)
#     blk 100  + white 100
#     pick 2  (wb, bb, ww) 3 cases
#         if wb   (-1,-1)+ (0,1) =  (-1,0)        => 99,100
#         if bb   (-2,0) + (1,0) = （-1,0）           99,100 
#         if ww   (0,-2) + (1,0) =  (1,-2)           101,98
# final 1 blk => 100%


# 100 stone
# A 1-2        
# B 1-2        
        
# 100%3=1
# A take 1
#     if B take 1 then A take 2    => 3
#     if B take 2 then B take 1    => 3


# Lc 43
# Given two non-negative integers num1 and num2 represented as strings, 
# return the product of num1 and num2

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"

def multiply(self, num1: str, num2: str) -> str:
    val1, val2 = 0, 0
    n1 = len(num1)-1
    n2 = len(num2)-1
    c = 0

    # two pointer n1 and n2 traversing from left to right!
    while n1>=0 or n2>=0:
        # use ASCII to convert char to int
        if n1>=0:
            val1 += ((ord(num1[c])-ord('0'))*(10**n1))
        if n2>=0:
            val2 += ((ord(num2[c])-ord('0'))*(10**n2))
        n1-=1
        n2-=1
        c+=1

    return (str(val1*val2))











