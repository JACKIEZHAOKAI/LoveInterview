'''
2021面经    Simulation 

infra 招人

基础知识
比较满意的项目的一些相关技术?
    rpc call需要注意的问题？ 
        同步：微服务架构下，很容易产生雪崩效应。若 C 服务挂住了，会导致前面的服务全部都因为等待超时而占用大量不必要的线程资源。内部主服务链之间的 RPC 调用需要异步化，服务之间的调用请求和等待结果相互之间解耦
        异步：RPC 的同步调用确保请求送达对方并收到对方响应，若没有收到响应，框架则抛出 Timeout 异常。这种情况下调用方是无法确定调用是成功还是失败的，需要根据业务场景（是否可重入，幂等）选择重试和补偿策略。
    异步操作可能存在什么问题？
      1：并不是所有的服务都需要异步调用。
      2：服务的异步调用并不会缩短服务的执行时间，它的优势在于可以和其它请求并行运算。
      3：不适合的异步调用非担不会增加系统的吞吐量，反而会使系统性能下降。
      4：服务的异步调用会增加客户端程序的复杂性。


C++相关比如
	ref  vs pointer
        pointer有自己的記憶體空間，且pointer可以只declare不initialize
        且pointer可以更改指到別的變數，reference不行
	虚函数？
        虚函数，是指被virtual关键字修饰的成员函数。 在某基类中声明为virtual 并在一个或多个派生类中被重新定义的成员函数，
        用法格式为：virtual 函数返回类型函数名（参数表） {函数体}；
        实现多态性，通过指向派生类的基类指针或引用，访问派生类中同名覆盖成员函数
	template 是什么？优劣？

ML相关
    L1vsL2
    Precision vs Recall
    regularization有哪些方法
    如何处理imbalanced data…
'''



# 早上起晚了刚刚睡到面试时间太紧张。。。
#   开始问了我觉得比较满意的项目的一些相关技术。比如rpc call需要注意的问题？ 异步操作可能存在

# 然后问C++相关比如
# 	ref  vs pointer
# 	虚函数？
# 	template 是什么？优劣？

# 看我实在都不太会也没什么好问的就直接上题目，结果第一题都没看懂还是换题了。。。
#   Json格式的string转C++自定义的数据结构，需要处理嵌套{ key:value, {key: value}}，完全没做过类似的不太行。

# 反转从位置m到n的链表
# struct LinkedList {
#     LinkedList * next;
#     int value;
# };

# 1->2->3->4	(2,3)	=> 1->3->2->4	=>	head=1
# LinkedList * reverse(LinkedList * head, int start_pos, int last_pos){
# }
    
def reverse(head, start_pos, last_pos):
    # swap two nodes each time until reading the end 
    # Time O(n)	Space O(1)

    prev = None
    curr = head
        
    if not head or not head.next:
        return head
    
    # 1 skip first start_pos-1 nodes
    i = 1
    while curr is not None and i < start_pos:
        prev = curr
        curr = curr.next
        i = i+1
    
    # prev points start_pos-1, curr points to start_pos
    
    # 2 start reversing the linkedlist
    start = curr
    end = None
    
    while curr != None and i<=last_pos:
        nxt = curr.next
        curr.next = end
        end = curr
        curr = nxt
        i = i + 1
    
    # start points start_pos-1, end points to last_pos，curr points to last_pos+1
    
    # 3 fix the pointer and return the head
    start.next = curr
    if prev is None:
        head = end
    else:
        prev.next = end
      
    return head
    
