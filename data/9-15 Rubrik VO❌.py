##############################################################################
# 9/15 VO
# HR Travis Garland <travis.garland@rubrik.com>
'''
Your final round will have two Algorithm Coding, one Systems Coding, and a Culture Add interview with the hiring manager. 

    12:30PM (PDT) - 1:30PM (PDT): Gurneet Singh (Sr Software Engineer) - Algorithms Interview 四年经验小印 印度调过来
    1:30PM (PDT) - 2:30PM (PDT): Sophia Chen (Sr Software Engineer) - Algorithms Interview  caltech 斯坦福MS 三年半 ABC女
    
    2:30PM (PDT) - 3:00PM (PDT):  - Break

    3:00PM (PDT) - 4:00PM (PDT): Patricia Beekman (Software Engineer) - Systems "Coding" Interview 三年半经验白人女
    TODO
        synchronization, mutli-threading and file system calls. 

        Concurrency 
        concurrent programming, 
        semaphores, 
        condition variables, 
        memory management, 
        I/O, 
        multithreading

    4:00PM (PDT) - 4:45PM (PDT): Gurjeet Arora - Culture Interview      20年 TLM 老印 https://www.linkedin.com/in/gurjeet-a-9878462/

    根据具体项目经验说，围绕问题说，证明如果解决问题 Answer the question + Detailed

    围绕这五个点问：
        ● 坚持 Relentlessness: Never give up. Solve the hardest problem by taking risks.
            Q   How to solve challenges?
            Q   How to drive a project independently?
        
        ● Integrity: Be honest. Do what you say, and say what you do - even when no one is watching.
            Q   Find some error and how to 

        ● 效率 Velocity: Move fast. Move quickly and decisively to conquer challenges. Actions are louder than words.
        
        
        ● 工作质量 Excellence: Be your best. Do your life’s best work and leave your mark.
        
        
        ● 合作 Transparency: Be open. Share information to drive smarter decisions and engender trust.
            Q:  experience working with others? Disagree with others and how to over come?
                    cross team work
                    After analyzing the pros cons, doing in depth reseach of the implementation and consequence of each solution
                    Proactively reaching out to other seniro engineer to review the plan, demo, and ask for feedback
''' 

##############################################################################
"""
Coding 1

1. There can be multiple snakes on the board.
2. Only one snake moves at a time.
3. When two snakes collide, the moving snake will die.
4. When a snake collides with a wall/edge of the board, it will die.
5. Consuming food increases the length of the snake.

When the game starts, board is empty

Point: (x,y)
createSnake(Point p) -> int  # snake ID 

# Place food at a random empty place on the board
createFood()

# moveSnake
moveSnake(snakeID: int, direction: U/D/L/R)
    1. check if head(Head+dir) hits the boundary => dies, removed from  snakesMap
    2. check hit any other snake(Head+dir in the set of other snake's body set<Point>), removed from  snakesMap
  
    3. check if head(Head+dir) hits the food( in the set of foodMap) => 
        update the head
        
    4. normal move 
        update the tail => (tail+ tailDir)

// getSnakes returns all of the existing snakes.
// Map from snake ID to collection of points on which snake body lies.
Map<int, Collection<Point>> getSnakes()

// getFoods returns all of the existing foods on the board.
Collection<Point> getFoods()
"""

from collections import dequeue, Hashable
from collections.abc import Hashable
import random 

class SnakeGame:

    def __init__(self, width, height):
        self.snakeMap = {}   #  Hashable<int, dequeue<tuple>>  lived snake ID -> Point(x,y)
        self.snake_set = set()
        self.food_set = set()               # set of food Point ()
        
        self.movement = {'U':[-1,0], 'D':[1,0], 'L':[0,-1], 'R':[0,1]}
        self.width = width
        self.height = height
        
    def createSnake(self, Point p) -> int  # snake ID 

    # Place food at a random empty place on the board
    def createFood(self):
        # add a point on the board not in snake_set and not in food_set
        foodRand = []
        for i in self.width:
            for j in self.height:
                if (i,j) not in self.food_set and (i,j) not in self.snake_set:
                    foodRand.append((i,j))
        return random.choice(foodRand)

    def moveSnake(self, snakeID: int, dir):
        # 1. check if head(Head+dir) hits the boundary => dies, removed from  snakesMap
        # 2. check hit any other snake(Head+dir in the set of other snake's body set<Point>), removed from  snakesMap
    
        # 3. check if head(Head+dir) hits the food( in the set of foodMap) => 
        #     update the head
            
        # 4. normal move 
        # update the tail => (tail+ tailDir)

        # new Head
        snake = self.snakeMap[snakeID]
        newHead = (snake[0][0] + self.movement[dir][0], snake[0][1] + self.movement[dir][1])

        # boundary check 
        bound1 = newHead[0] < 0 or newHead[0]  >= self.height
        bound2 = newHead[1] < 0 or newHead[1]  >= self.width

        # check if bit any snake
        bit_self = newHead in self.snake_set
        if bound1 or  bound2 or bit_self:
            del self.snakeMap[snakeID]
            for point in snake:
                self.snake_set.remove(point)
            return -1
        
        # check if eats a food
        if snake[0] not in self.food_set:
            # update the tail
            tail = self.snakeMap[snakeID].pop()
            del self.snake_set[tail]

        self.snakeMap[snakeID].appedleft(newHead)
        self.snake_set.add(newHead)
        return 



##############################################################################
'''
Coding 2    斯坦福女，完全没搞懂要写什么，尬了半个多钟。。。

    Google Calendar Desing 
        How to add and send notification?
'''



##############################################################################
'''
Coding 3    System coding   白人女胖胖 感觉人不错 挺友善
    
    非常简单的O(n) 过了一下，升级难度

    file system =》 blocking 的基础处理，居然完全没问系统相关的。。。
    而且 只用写psedocode ... 随便像一个libary的接口随便写
    一点不push
    
    最后10min  Q&A  
        感觉还是不太会提问组相关的问题

    我也不知道怎么安排的， 我明显感觉到这一轮更像写code
'''

# ---------------------
# ------   --    ----
# (0, 5)  (8, 9)  (13, 16) // <- inclusive

#   xxxxxxxxxxx forget(2, 8)
# (0, 1)  (9, 9)  (13, 16)

#   xxxxxxxxxxx forget(5, 8)
# (0, 4)  (9, 9)  (13, 16)


#   xxxxxxxxxxx forget(1, 2)
# (0, 0)  (3, 5)  (8, 9)  (13, 16)

# remember(start, end)
# // assume that (start, end) does not overlap with anything already populated

# forget(start, end)

# Collection?
#   HashSet   #   tuple to represent all block to be populated 

#   Pirority Queue    # O(n) to traverse  O(logn) for insertion
  
#   Tree    # O(logn) Insert/Delete

class TreeNode:
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None

'''
    tree.update(interval, oldhead, oldtail, newhead, newtail)    
    intervalList = self.tree.findInterval(start, end)    
'''
# (0, 5) forget(1, 4)
class FileSystem:
    def __init__(self) -> None:
        self.tree = BalancedBST()
    
    def remember(start, end):
        self.tree.insert(start, end)

    def forget(start, end): # (8,8)
    
        intervalList = self.tree.findInterval(start, end)   # (0, 5)  (8, 9) in sorted order

        if len(intervalList) == 0:
            return 
        
        if len(intervalList) == 1:
            head, tail = intervalList[0][0], intervalList[0][1]
            if head <= start and  tail >= end:      # (0, 5) => start end (0-, 5+)
                self.tree.delete(head, tail)
            elif head < start and tail >= end:      # (0, 5) => start end (4, 5), update head
                tree.update(interval[0], head, tail, start, tail)
            elif head <= start and tail > end:      # (0, 5) => start end (0, 3), update tail
                tree.update(interval[1], head, tail, head, end)
            else:                                   # (0, 5) => start end (1, 3), update both
                tree.update(interval[0], head, tail, start, end)
            return
        
        # update the start and ending intervals in the tree
        tree.update(interval[0], interval[0][0], interval[0][1], interval[0][0], start)      # update (0, 5) to (0, start=1)
        tree.update(interval[-1], interval[-1][0], interval[-1][1], end+1, interval[-1][1])      # update (8, 9) to (end+1=9, 9)

        # remove internal intervals from the tree
        for interval in intervalList[1: len(intervalList)-1]:
            self.tree.delete(interval[0], interval[1])
        


##############################################################################
'''
    4 round     Hiring manager 印度版罗翔
    
    各种general的 culture BQ



'''






















