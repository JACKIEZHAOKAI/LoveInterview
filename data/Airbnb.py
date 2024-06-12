
# 两轮back to back，压力有点大面的不好
# 题目没做出来fail了至少一轮

#############################################
# 一面  白人鬼佬  
'''
    开始还是太紧张了，给出了基本思路， 还是有些着急implement，思路没有非常清晰
    implement的时候遇到矛盾的地方，对set和题目不熟悉，反复思考改改删删，沟通也不顺利。

    再加上打字手速跟不上，而且codepad的latancy一直很高打字跟不上，还有桌子没有固定住一直晃，
    床帘断了漏光，心情也非常down！！！

    面试官也不算给力，hint不够      我自己打分40        NO hire

反思：
    硬件设备必须更新！   桌子固定器， 摄像头买一个? 床帘赶紧用胶布胶上去不要动了 

    软件层面：    思路必须清晰，给出很清晰的思路才能动笔code。
                不押题，一定是要清楚每一道题的思路和做法的原因。
'''

#############################################
#   Open Boxes ==>  BFS + set
# 1. I am going to give you a box
# 2. A box can either be locked or unlocked
# 3. Inside the box -> # candies, # nested boxes, # keys
# 4. Keys correspond to specific boxes
# Question: if give you a box, what is the maximum number of candy you can retrieve?
#
# I give you box 1 = [unlocked, Boxes=[2, 3], Keys=[], Candies=5]
#
#            box 2 = [locked, Boxes=[], Keys=[], Candies=2]
#            box 3 = [unlocked, Boxes=[], Keys=[2], Candies=2]
#
# Question: Given box 1, how many candy can you get?
#    box 1 5 +  box 5: 2 + box2: 2 = 9 
#############################################

# 1  Box 的 data structure 要自己设计， 我说用hashmap 存key value
# box{
#     id: int     1
#     locked: Boolean True/ False
#     nestedBox = []
#     keys = []
#     candies= int 
# }

def findCandies(box):
    
    # visited_boxes = set()    #seen
    unvisited_boxes = set(box)
    keys = set()
    total_candies = 0
    canMove = True

    if box['locked']:
        return 0
    
    while canMove:        
        front = unvisited_boxes.remove(0)

        if not front['locked'] or front["id"] in keys:
            # unlocked or found keys, can open the box and update
            keys.add(front['keys'])
            total_candies += front['candies']
        else:
            # locked and not found key yet
            unvisited_boxes.add(front)

        # try to open its nested box
        for neighbour in front["nestedBox"]:
            if neighbour is unvisited_boxes:

            queue.append(neighbour)

        # update canMove
        canMove = False
        for box in unvisited_boxes:
            if not box['locked']:
                canMove = True
                break 
            if box['id'] in keys:
                canMove = True 
                break

        
    return total_candies
    

#########################################################
# 二面  中国女孩  
'''
    在面试官的鼓励下一步步往前move on，而且自己能给出基本思路，在很必要的时候要一下hint
    虽然最后写不出来 backtrack这类题型也不熟练  但是已经 尽力了 
    
    不足：在借鉴了detect cycle的代码之后对于return type还是有点混乱

    题目毕竟hard难度  我自己打分70   Avg hire
    其实发现是面经原题  eight puzzle 没有准备到

# 反思：
    软件层面：    
        在知道基本挂定了的前提现也能放平和心态，坚持完成第二轮，比谷歌的backtoback已经有很大进步了
    
        对于没见过的题目也能积极冷静思考，并且写了基本代码，对我的能力来说已经很不错了

        题目的覆盖面还不够广，比如backtrack的代码准备为0
'''
#########################################################
# 棋盘 eight puzzle   => DFS + BACKTRACKING + Detect cycle

# Given a matrix, determine if can finally reach the ending state:
# 1 2 3
# 4 5 6
# 7 8 X

# 1 设计data structure 用2D list 储存
# 2 什么时候后backtrack？ 
#########################################################

def game(matrix):

    def findEmptySlot():



    def findNeighbourMatrix(matrix, emptySlot):
        # 1     find all neighbour of emptySlot
        # 2     


    def dfs_backtracking(matrix, emptySlot):
        




