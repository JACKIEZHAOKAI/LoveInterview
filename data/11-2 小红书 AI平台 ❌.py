'''
介绍下项目经历，主要的挑战是什么？

inventory service 跨多个云基础架构的服务管理，需要解决的缓存等问题怎么处理？
    1。读写分离，硬写入和软写入, 资源库存管理 Read-only 	== database service
    2. Ascyn Job 异步操作不需要wait。、

    多云环境的支持：
    考虑在 Inventory Service 中实现多云环境的支持。这可能涉及到在不同云提供商的基础上构建适应性层，以处理各个云提供商的特定要求。这可以通过使用云相关的SDK、API、标准化的虚拟化技术或容器化来实现。

    缓存策略：
    实施缓存策略以加速库存数据的访问。考虑使用内存缓存（如Redis、Memcached）来存储常用数据，减少对后端存储的频繁请求。这可以显著提高服务的响应时间和可伸缩性。

    数据同步与一致性：
    跨多个云提供商时，确保实现数据同步和一致性。使用适当的数据复制和同步机制，以确保库存数据在不同云环境之间保持一致，避免潜在的数据不一致问题。

Java？

线程池
    参数有哪些？
    
    创建工作原理？


JVM虚拟机 讲一下？

指令重排？

redis单机还是集群？

单机为什么这么快？？？

    内存存储： Redis主要将数据存储在内存中，内存访问速度非常快，远远快于磁盘访问。因此，读写操作都可以在内存中完成，从而实现了高速的数据访问。

    单线程模型： Redis采用单线程事件循环模型，这意味着它使用一个主线程来处理所有客户端请求。虽然是单线程，但Redis通过非阻塞I/O、事件轮询和多路复用等技术，可以高效地处理并发请求。单线程模型避免了多线程并发竞争和线程切换的开销，减少了锁竞争的可能性。

        非阻塞I/O： Redis采用非阻塞I/O操作，这意味着它可以在等待I/O操作完成的同时处理其他任务。单线程可以轻松实现非阻塞I/O，因为它无需等待多个线程之间的上下文切换。

        事件驱动： Redis采用事件驱动的方式来处理客户端请求。它使用事件轮询机制，等待各种事件的发生，包括新的客户端连接、数据接收、定时器事件等。这种方式能够高效地管理多个并发事件。

        避免锁竞争： 多线程模型通常需要使用锁来保护共享数据，而锁会引入竞争和上下文切换开销。Redis的单线程模型避免了多线程之间的锁竞争，减少了上下文切换的开销。

    持久性选项： Redis提供多种持久性选项，包括快照（snapshot）和日志文件（append-only file）方式。这些选项允许将内存中的数据定期或实时保存到磁盘，以便在重启后恢复数据。这可以确保数据的安全性同时保持较高的性能。

    高效的命令： Redis提供了丰富的高效命令，如原子性操作、批量操作、自动过期、发布订阅等，这些命令可以帮助开发人员快速实现常见任务，而无需复杂的应用逻辑。

    多级缓存： Redis通常可以配置为将内存用作主存储，但也可以在需要时将数据持久化到磁盘。这使得Redis可以在内存存储和磁盘存储之间取得平衡，以满足不同的需求。

'''


# 1. 抄代码抄的都心虚啊，思路也不清楚。。。
# 2. 左右分屏的时候抄的太明显了，这个还是需要外接摄像头。。。

# LRU least recent used
#    hashmap实现 O(1) 的读取
#    double linkedlist 实现 O(1)的更新？？？如何
#       
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # hashmap, key to node in linkedList
        self.linkedList = DoubleLinkList() # mantain the order
       
    def get(self, key):
    	if key in self.cache:
        	# move to front
            node = self.cache[key]
			self.linkedList.move_to_front(node)
			return node.value
		return -1

    def put(self, key, value):
   		# if found in cache, update the value
    	if key in self.cache
			node = self.cache[key]
			node.value = value
			self.linkedList.move_to_front(node)
		else:
        	# check if overflow 
            if len(self.cache) >= self.capacity:
            	node = self.linkedList.pop_back()
				# remove the node 
                del self.cache[node.key]
			new_node = Node(key, value)
			self.cache[key] = new_node
			self.linkedList.add_to_front(new_node)
        
        
class DoubleLinkList:
	def __init__(self, key, value):
    	self.key = key
		self.value = value
		self.front = None
		self.next = None

    def move_to_front(self, node):
    	# move curr node to front
        self.remove(node)
		self.add_to_front(node)

    def add_to_front(node):
    	# add curr node to front
                
    def pop_back(self):
    	# move back node to front
    
    def remove(self, node):
    	# remove curr node
    
   	