
// TuSimple	– 8/4 FAILED

// 6/30 	HR chat 
// Background
// Why left TuSimple and why back?
// 4 year UC San Diego and intern in TuSimple, but want to move to the bay area. 
// work with  TLM @haoranWang  and @kangwei 深中,  Onboard Runtime, and Heterogeneous Computing.(GPU/ ML Accelerator) 
// H1b sponsorship
// 200k TC
// 401 K up to 5%
// PTO  15 days  + 8 sick days  + 12 day public holidays
// Interview
//  6 rounds  ==  2 coding  + 4 project-based/HQ
// Questions:
// working hours?  10–6 pm including 1hr lunch-time
// Back to the office (3 days in the office 2 days at home) 
// IPO: Nvidia investor  ⇒
// commercial stage; UPS and xxx;  7k trunks; production stage in early 2024
// Competitor building trucks: Tesla Semi, Embark, Daimler奔驰. TuSimple is now ahead of everyone. 
// The truck is more manageable, on the drive-in Highway.

// 7/12  	第一轮技术面 		@ kangwei (SDE3) 上交CS
// Background
// background Dataset2 at TuSimple
// Java Sprint 后台服务 at VMWare
// Onboard System at Pony
// Onboard Team: Zoro 之前北京做，中美切割
// MiddleWare;  Console interface自动驾驶启动过程（模块启动) — RPC 接口
// 逐步分发给其他team在做
// onboard system: gRPC overhead, 算法模块
// HMI 人机接口
// 做题：Implement Push and Pop for a queue : LC 1188
// Condition Var & Mutex  C++ 使用
// C++  STL Queue 
// C++ Multi threading  
// Incoming Interview 
// 2 flexible coding: 	C++ and Python  ⇒ 1-2 coding problem 
// Virtual Onsite:  3-4

// 8/4  	第二轮技术面		@Aaron Tian 华中科大第一名
// 上来就彪英文，英文还不错，问我为啥离开图森blabla。Senior position 可以remote
// 介绍自己的简历，对着简历问？
// Challenges and how to overcome???
// Communication
// defining data strucuture based on other team
// fixed via global communication
// How to take accidents?
// Clear cross team comm
// UT(functionality) => Dev (system) => stag (1-2 AWS) -> prod (AWS)
// interfacing to reduce risk, backup plan, make sure not ruin other service
// logging and monitoring on real service to support other team
// Spiral Matrix
// 可能挂了，搜到了经典题，优化的思路想到了O(1)，但是思路不清晰导致没有一次写出来，debug过程还是对case分析不够透彻 30min没写完，期待20 min coding 。。
// Q & A? 
// Middleware providing support (timming/ comm/ auth)
// Onboard Runtime: C++() and python for scripting(demo inside)
// Ros is the underlining part
// Ros/Zoro API to improve interface
// Algo module is high level: proception / lidar 
// 确实挂了 还是要多做题 move forward


// ##################################################
// 1188. Design Bounded Blocking Queue
// BoundedBlockingQueue(int capacity) The constructor initializes the queue with a maximum capacity.
// void enqueue(int element) Adds an element to the front of the queue. If the queue is full, the calling thread is blocked until the queue is no longer full.
// int dequeue() Returns the element at the rear of the queue and removes it. If the queue is empty, the calling thread is blocked until the queue is no longer empty.
// int size() Returns the number of elements currently in the queue.
// ##################################################

class BoundedBlockingQueue {
private:
    int capacity;
    queue<int> que;
    mutex mtx;
    condition_variable cvEnqueue;
    condition_variable cvDequeue;
    
public:
    BoundedBlockingQueue(int capacity) : capacity(capacity) { }
    
    void enqueue(int element) {
        // use mutex and cv together, cv to manage the mutex
        unique_lock<mutex> lock(mtx);
        cvEnqueue.wait(lock, [&](){ return que.size() < capacity; }); // block push() if queue is full
        // exeucute
        que.push(element);
        cvDequeue.notify_one(); // unblock pop() since we pop one val
    }
    
    int dequeue() {
        unique_lock<mutex> lock(mtx);
        cvDequeue.wait(lock, [&](){ return que.size() > 0; }); // block pop() if queue is empty
        // exeucute
        int res = que.front();
        que.pop();
        cvEnqueue.notify_one();  // unblock push() since we pop one val
        return res;
    }
    
    int size() {
	    lock_guard<mutex> lock(mtx);
        return que.size();
    }
};


// ##################################################
// 54. Spiral Matrix
// 20 min coding 可能挂了，没写出来优化的方法，还是对case分析不够透彻
// Given an m x n matrix, return all elements of the matrix in spiral order.
// https://leetcode.com/problems/spiral-matrix/
// ##################################################

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
            simulate the movement in the order of down, left, up, right
            Time    O(n)
            Space   O(n)
        '''
        if not matrix: 
            return []
        
        R, C = len(matrix), len(matrix[0])
        visited = set()
        res = []
        
        # use r, c to represent current location, and di to represent the four direction
        r, c = 0, 0
        di = 0
        direction = [(0,1),(1,0),(0,-1),(-1,0)]    # move down, left, up, right
        
        for _ in range(R * C):
            # restore curr position
            res.append(matrix[r][c])
            visited.add((r,c))
            # move
            cr, cc = r + direction[di][0], c + direction[di][1]
            
            if 0 <= cr < R and 0 <= cc < C and (cr,cc) not in visited:
                r, c = cr, cc
            else:
                # direction
                # print("at:",r, c, ", move", direction[di])
                di = (di + 1) % 4
                r, c = r + direction[di][0], c + direction[di][1]
        
        return res