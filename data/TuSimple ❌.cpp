
// ########################################################
// 聊得还不错，介绍了实习做的内容（为什么？怎么设计方案解决？技术方案对比优劣）和简单介绍vmware开发
// googledoc做（抄）了一道LC题，就是之后说bigO开始说错了O(n^2）， DFS应该都是O(n)。

class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        """
        Tusimple Fulltime Interview
        :type nums: List[int]
        :rtype: bool
        
        Time O(n)
        Space O(1)
        """

        # If there are no matchsticks, then we can't form any square
        if not nums:
            return False

        L = len(nums)
        perimeter = sum(nums)
        possible_side =  perimeter // 4
        
        # check if dividible by 4
        if possible_side * 4 != perimeter:
            return False

        # Reverse sort the matchsticks because we want to consider the biggest one first.
        nums.sort(reverse=True)

        # This array represents the 4 sides and their current lengths
        sums = [0 for _ in range(4)]

        def dfs(index):
            if index == L:
                return sums[0] == sums[1] == sums[2] == possible_side

            for i in range(4):
                if sums[i] + nums[index] <= possible_side:
                    # Recurse
                    sums[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    # Revert the effects of recursion because we no longer need them for other recursions.
                    sums[i] -= nums[index]
            return False
        
        return dfs(0)


// ########################################################
// ASSUME we have 

// class DS(data stream)
// constructor
// int NextInt(): non-decreasing       // a number or exception
// bool HasNext()      // Ture/false

// ds1: 0, 1, 2, 3, 4, 5...            //non decreasing
// ds2: -2, -1, 0, 0, 0, 2, 4, 6
// ---

// YOU are asked to implement a special DS class, called FreqDS
// 1. constructor: several DS objects and int k as the input
// 2. int NextInt(): return an int appearing at least k times in the input DS
// 2. bool HasNext()
// FreqDS({ds1, ds2}, k = 2):  
// class FreqDS:
//     fds = {ds1, ds2}
//     k = 2

// EX   NextInt() 0, 2, 4, 6


// helper funciton for counting the apperance of currNum in the ds
int countAppearance(DS ds, int currNum, int prevNum){
    int prevCount = 0;
    // count the apperance of the successive number
    while (ds->HasNext()) {
        currNum = ds->NextInt();
        if (prevNum == currNum){
            prevCount ++;
        }
        else{
            return prevCount;    
        }
        prevNum = currNum;
    }
}


int NextInt(){
    int totalCount;
    int dsIndex;
    int currCount;
    int prevNum[fds.size()];
    int currNum;
    
    // start from the min of all array
    std::vector<int> minArr;
    for (auto it = fds.begin(); it != fds.end(); it++){
        minArr.pushback(it.begin());   
    }
    currNum = min_element(minArr.begin(),minArr.end());
        
    // keep calling countAppearance for each datastream until count >=k, then return the number 
    while(1){
        //init
        totalCount = 0;
        dsIndex = 0;
        currCount = 0;
        currNum = 0;
        // one round check of the apperance of currNum
        for (auto it = fds.begin(); it != fds.end(); it++){
            currCount = countAppearance(it, currNum, prevNum[dsIndex]);
            totalCount += currCount;
            prevNum[dsIndex] = currNum;
            // check if occurance of currNum reaching k
            if(totalCount>=k){
                return currNum;
            }
            dsIndex ++;
        }
    }    
}
    
    
