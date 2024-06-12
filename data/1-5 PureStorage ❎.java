// PS 的面试从2022年底拖到现在
// 两轮面完了都答得不错，感觉就是对着答案演戏

// 现在存储的主流市场,没有新增产品。
// block storage(flashArray), file storage(flashBlade)

// # flashBlade  VS  flashArray
// #######################################################
// # 储存一面，老题都懒得编，主要看followup能不能写出来，还会穿插一些优劣分析考察
// # 一个马尾辫Tom Duan，感觉还挺健谈，但是很tech

// # //              d
// # //     c

// #      a
    
// #   b.    c  

// #      d
// # ab=bd=dc=ac=bc ad
// # determine if four points is a square?

// #     a
    
    
// #     b

    
// #  c.    d   
// #     a

// # relationship between diagonals and sides for a square? squrt root 
// #######################################################
class point:
    int x;
    int y;

def isSquare(a, b, c, d):
    def disSquare(x,y):
        return (x.a - x.b) ** 2 + (y.a - y.b) **2
    def isSquRoot(dist1, dist2):
        return dist2 == 2 * dist1 
    dist_map = {} # map dist to its count
    length = []   # dist length
    for p, q in (a, b), (a, c), (a, d), (b, c), (b, d), (c, d):
        dist = disSquare(p, q)
        if dist not in dist_map:
            dist_map.add(dist, 0)
            length.append[dist]
        else:
            dist_map[dist] += 1
    
    return len(dist_map) == 2 and \
    (dist_map[length[0]] == 2 and dist_map[length[1]] == 4 and isSquRoot(length[1], length[0])) or \
    (dist_map[length[1]] == 2 and dist_map[length[0]] == 4 and isSquRoot(length[0], length[1]))


def findNumSquare(pointList):   # N points in pointList
    '''
        time O(N**4) -> O(n**3)
    '''
    countSquare = 0
    pointMap = set(x for x in pointList)
    for i in len(pointList):        
        for j in i+1, len(pointList):
            for m in j+1, len(pointList):
                d = help(pointList[i], pointList[j], pointList[m])
                if d in pointMap:
                    countSquare += 1
                # for l in l+1, len(pointList):
                #     if isSquare(pointList[i], pointList[j], pointList[m], pointList[l]):
                #         countSquare += 1
    return countSquare
    

// #######################################################
// # 历来面经
// 马来人？lim 一直假笑想搞我，一点点都给他搞出来了，主要就是followup他期望我一点点跟进
'''
    1. 有两个函数 void reg_cb(callback_t cb) 和 void event_fired()
    2. reg_cb可以被调用多次，event_fired只能被调用一次
    3. event_fired() 会调用在它被调用之前的所有被调用的reg_cb的参数cb()
    4. 在event_fired()被调用之后，所有的新的reg_cb()的调用需要立即调用其参数cb()
    5. 先用单线程实现上述操作，再转用多线程（特别注意要小心死锁，因为cb可能会调用reg_cb）
'''
# /*
# |------------|  reg_cb()
# |  Module1   |------------|
# |------------|            |
#                           |                        
#                           |                                               |-------------|
# |------------|  reg_cb()  |---------->|-----------|     event_fired()     |             |
# |  Module2   |----------------------->|   Event   |<----------------------|    Event    |
# |------------|            |---------->|  Manager  |                       |             |
#                           |           |-----------|                       |-------------|
#                           |
# |------------|            |
# |  Module3   |------------|
# |------------|  reg_cb()

#                                     cb1()
#                                     cb2()          cb3()
# ------------------------------------------------------------------->time
#       |               |               |              |
#       |               |               |              |
#    reg_cb(cb1)    reg_cb(cb2)    event_fired()    reg_cb(cb3)
   
# Goal is to implement event_fired and reg_cb

# Assumptions
# 1. event_fired is only ever called once
# 2. multi-threaded
# */

# 先来单线程
interface func_t {
    void invoke();  # trigger cb
}

class EventMgr {
    Queue<func_t> eventQueue = new LinkedList<>();
    boolean isFired = false;
    
    public void reg_cb(func_t cb) {
        if(!isFired) {
            eventQueue.offer(cb);
        }
        else {
            cb.invoke();
        }
    }
    
    public void event_fired() {   
        while (!eventQueue.isEmpty()){
            eventQueue.poll().invoke();
        }
        isFired = true;
    }
}

class EventMgr {
    Queue<func_t> eventQueue = new LinkedList<>();  // cb1 cb2 cb3 <eventfire> cb4
    boolean isFired = false;
    Lock lock;     // atomic of eventQueue, only lock critical section
    
    public void reg_cb(func_t cb) {
        lock.lock();
        if(!isFired) {                      // cb4
            eventQueue.offer(cb);           // eventQueue: cb4, critical section
            lock.unlock();
        }
        else {
            lock.unlock();
            cb.invoke();    
        }
    }
    
    public void event_fired() {  
        lock.lock();
        isFired = true;
        while (!eventQueue.isEmpty()){      // eventfire, critical section 疯狂问
            func_t cb = eventQueue.poll();  
            lock.unlock();
            cb.invoke();                    // run in parallel
            lock.lock();
        }                                   // invoke cb1 cb2 cb3
        lock.unlock();
    }
}

class EventMgr {
    Queue<func_t> eventQueue = new LinkedList<>();  // cb1 cb2 cb3 <eventfire> cb4
    boolean isFired = false;
    Lock lock;     // atomic of isFired

    public void reg_cb(func_t cb) {
        lock.lock();
        if(!isFired) {                      // cb4
            eventQueue.offer(cb);           // eventQueue: cb4, critical section
            lock.unlock();
        }
        else {
            lock.unlock();
            cb.invoke();                    // invoke cb4 if isFired==True
        }
    }
    
    public void event_fired() {  
        // set isFired to true
        isFired = true;
        lock.lock();
        lock.unlock();  // make sure all cb are added to eventQueue
        // pop all cb in eventQueue
        while (!eventQueue.isEmpty()){      // eventfire, critical section
            func_t cb = eventQueue.poll();  
            cb.invoke();                    // run in parallel
        }
    }
}

