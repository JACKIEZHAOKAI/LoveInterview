###########################################################
#   12/17   店面

# 女的白人，不好聊天，一上来就没精打采，问问题也不积极回答我。

# 考了game of life,  不知咋回事rules 四个变得只剩下两个？让我有点慌
# 最后debug发现时abs（）函数的括号放错了位置，对着代码抄让后讲，没啥意思。
# follow up问size很大咋办？    Disk load to memory         read 3 lines at each time to get row’s neighbor

# 聊天很尴尬 草草结束    没意思。。。
###########################################################
#   289.    Game of life, 
'''
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules 
    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.
The next state is created by applying the above rules simultaneously to every cell in the current state, 
where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
'''

###########################################################
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        难点是如何表示这个board每一轮的变化状态
            2   ->  the cell was dead before but now live.
            -1  ->  the cell was live before but now dead. 
            0   ->  still dead
            1   ->  still alive
        finally update the board:
            2, 1 => 1
            -1, 0 => 0

        Time: O(M×N), where M is the number of rows and N is the number of columns of the Board.
        Space: O(1)
        """
        rows = len(board)
        cols = len(board[0])
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        for row in range(rows):
            for col in range(cols):
                # for each cell the updated rules are:
                # Rule 1: Any live cell with fewer than two live neighbors dies, as if caused by under-population. 
                # Hence, change the value of cell to -1. This means the cell was live before but now dead.

                # Rule 2: Any live cell with two or three live neighbors lives on to the next generation. 
                # Hence, no change in the value.

                # Rule 3: Any live cell with more than three live neighbors dies, as if by over-population. 
                # Hence, change the value of cell to -1. This means the cell was live before but now dead. R1 and R3 same representation!

                # Rule 4: Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction. 
                # Hence, change the value of cell to 2. This means the cell was dead before but now live.
                live_neighbors = 0
                for neighbor in neighbors:
                    r = (row + neighbor[0])
                    c = (col + neighbor[1])
                    # Check the validity of the neighboring cell AND if it was originally a live cell.
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1
                    
                # Rule 1 or Rule 3
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # -1 signifies the cell is now dead but originally was live.
                    board[row][col] = -1

                # Rule 4
                if board[row][col] == 0 and live_neighbors == 3:
                    # edge case: 2 signifies the cell is now live but was originally dead. 
                    # avoid counting as alive and activate other neighbours wrongly
                    board[row][col] = 2

        # update board
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0


###########################################################
#   609. find dupl‍‍‍‌‍‌‍‍‍‍‍‍‌‌‍‍‌‌‌icate files 
    # 对于不同path下的所有files，如果file内容重复，归为一类。
    # 用hashtable 存 contents =>    list_of_file_paths_with_this_content

''' 
Given a list of directory info including directory path, and all the files with contents in this directory, 
you need to find out all the groups of duplicate files in the file system in terms of their paths.

Example 1:
Input:
[   "root/a 1.txt(abcd) 2.txt(efgh)",  
    "root/c 3.txt(abcd)",       
    "root/c/d 4.txt(efgh)",        
    "root 4.txt(efgh)"
]
Output:  
[   ["root/a/2.txt","root/c/d/4.txt","root/4.txt"],    
    ["root/a/1.txt","root/c/3.txt"] ]

Follow-up beyond contest:
1   Imagine you are given a real file system, how will you search files? DFS or BFS?
    # In general, BFS will use more memory then DFS. 
    # However BFS can take advantage of the locality of files in inside directories,
    #      and therefore will probably be faster

2   If the file content is very large (GB level), how will you modify your solution?
    
    # In a real life solution we will not hash the entire file content, since it's not practical.
    #  Instead we will first map all the files according to size. !!!
    #  Files with different sizes are guaranteed to be different. 
    #  We will than hash "a small part" of the files with equal sizes !!!
    #  (using MD5 for example). Only if the md5 is the same, we will compare the files byte by byte

3   If you can only read the file by 1kb each time, how will you modify your solution?
    # This won't change the solution. 
    # We can create the hash from the 1kb chunks, and then read the entire file if a full byte by byte comparison is required.

4   What is the time complexity of your modified solution? 
    # Time complexity is O(n^2 * k) since in worse case we might need to compare every file to all others. k is the file size
    
    What is the most time-consuming part and memory consuming part of it? How to optimize?
    # I/O

5   How to make sure the duplicated files you find are not false positive?
    # We will use several filters to compare: File size, Hash and byte by byte comparisons.

'''
###########################################################
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        '''
            Time:   O(nx). n strings of avg length x is parsed.
            Space:  O(nx). map and resres size grows upto nx.
        '''
        path_map = collections.defaultdict(list)    # map content to paths
        res = []

        for line in paths:
            # separate path And files
            data = line.split()         #"root/a 1.txt(abcd) 2.txt(efgh)"
            path = data[0]
            files = data[1:]
            for file in files:
                # extract content of each file
                name, _, content = file.partition('(')  # "xxx(content)".partition('(') >>> ('xxx', '(', 'content)')
                content = content[:len(content)-1]
                # insert key-value pairs                
                path_map[content].append(path + '/' + name)

        for content, paths in path_map.items():
            if len(paths) > 1:  # only count as duplicated files if len>1
                res.append(paths)

        return res


###########################################################
#   379. Design Phone Directory
'''
Design a Phone Directory which supports the following operations:

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
Example:

// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2);
'''

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.available = set(range(maxNumbers))

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        return self.available.pop() if self.available else -1
    
    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number in self.available

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        self.available.add(number)
       
# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
