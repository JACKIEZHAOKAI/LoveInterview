########################################################
#   datavisor  第二轮 又是一个操着qingelish的老中senior
'''
  一个mergersor必须用iteration做    
  一个unsorted array找最小     preprocessing O(n)      findMin() 要求小于 O(n) 
     大致思路是建一个tree，我也没想出来
'''
########################################################
# merge sort
'''
 [1,4,2,5,8,6,3,7]
 
 
1, 4,      2,  5,      8,  6,      3,  7

14     25      68  37

1245    3678

12345678

'''

# buttom up
def mergeSort(arr):
    
    curr_size = 1
    length  = len(arr) -1
    
    # traverse the sub array of curr_size in an outer loop
    while curr_size < length:
        
        left = 0    
        
        # traverse the inner loop for a merge call in a subarray
        while left < length:
            
            mid = min(left + curr_size - 1, length-1)
            
            right =  min(left+ curr_size*2-1, length-1)
            
            # merge call for each sub array
            # arr[left:mid] and arr[mid: right]
            merge(arr, left, mid, right)
            
            # move left
            left = left+ curr_size*2-1
        
        # increase curr_size
        curr_size *= 2

def merge(arr, left, mid, right):
    
    

mergeSort(arr) # => sorted array 


A: 1,3,4,3, 2,5,10,20
# p1 p2
'''
  search == find(range) => minValue         O(log n)
  
                index
        node( start, end, minValue)
            /                  \
    node(start,mid, minV)        node(mid,end, minV)

    n + n/2 + n/4 + ....+ 1=> O(n)
    
             node( 0, 7, 1)
            /               \
    node(0, 3, 1)        node(4, 7, 2)
    
'''

def buildTree(array):
    
    findMin(array)  # O(n)
    

# O(n)  store (start,end) => minValue 
# (2,4) =>100   (4,10) => 80    if(2,10)=> 80

# Length = 1B

# o(n)

# preprocessing: o(n)    
# query: O(log n )  O(n/2)< o(n)

# int getMin(int start, int end){
    



########################################################
''''
    这个datavisor面的这差居然都给我加下一轮？？？snap ps quip面的蛮好的还给我拒了。
    今年的面试，我真的是越来越看不懂形式了。这尼玛都是啥啊。。。
'''
########################################################
# !!! two pointer 真的是我的弱项！！！一定要好好练！！！

# Given a list of timestamps that events occur
# Find maximum event count within the fixed time window

#  s         e
#      s         e
# [1 1 2 2 3 4 4 4 7 8], 3 -> 6
########################################################
def findMaxEventsNaive(timestamps, time_window):
    '''
        Naive    Time    O(n^2)
    '''
    max_events = 0 
    
    for i in range(len(timestamps)):
        for j in range (i,len(timestamps)):
            if timestamps[j] - timestamps[i] > time_window:
                max_events = max(max_events, (j-i))
                
    return max_events


def findMaxEvents(timestamps, time_window):
        
    if not timestamps:
        return 0
        
    newtimestamps = []
    old = timestamps[0]
    count = 1
    
    # O(N) convertion
    for i in range(1, len(timestamps)):
        if timestamps[i] != old:
            newtimestamps.append( (old,count) )
            count = 1
            old = timestamps[i]
        else:
            count += 1
    
    #                     i j        
    # [(1,2),(2,2),(3,1),(4,3), (8,1), (10,10) (12,2)]
    # time_window = 3    
    # max_events => 5
    start, end = 0, 0
    max_events = 0
    counter = 0 

    while end < len(newtimestamps):        
        # try max expand the window for j
        while end < len(newtimestamps) and newtimestamps[end][0] - newtimestamps[start][0] < time_window:
            counter += newtimestamps[j][1]
            end += 1

        # if can not expand, then move i
        # when i catch j,  a gap, set both i and j to be the next
        max_events = max(max_events, counter)
        counter -= newtimestamps[i][1]
        start = start + 1       # move start only when can not expand end
        

    return max_events


print(findMaxEvents([1, 1, 2, 2, 6, 7, 8], 2))   # 4

print(findMaxEvents([1, 1, 2, 2, 3, 4, 4, 4, 7, 8], 3))   # 6


    