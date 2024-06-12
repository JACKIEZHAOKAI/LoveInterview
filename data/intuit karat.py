"""

We are designing a 2D game and we have a game map that we represent by an integer matrix. For now, each cell can be a wall (denoted by -1) or a blank space (0).

board = [
  [0,  0,  0, -1, -1],
  [0,  0, -1,  0,  0],
  [0, -1,  0, -1,  0],
  [0,  0, -1,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
]

The player can move 1 space at a time up, down, left, or right. The player can't go through walls or land on a wall, or go through the edges of the board.

Write a function that, given a board and a player starting position (represented as a row-column pair), returns all of the possible next positions for the player.

Sample inputs (board, starting_position) and outputs (in any order):

findLegalMoves(board, (3, 1)) =>
  (3, 0), (4, 1)

findLegalMoves(board, (5, 3)) =>
  (5, 2), (5, 4), (4, 3), (6, 3)

findLegalMoves(board, (5, 1)) =>
  (6, 1), (4, 1), (5, 0), (5, 2)

findLegalMoves(board, (6, 0)) =>
  (5, 0), (6, 1)

findLegalMoves(board, (6, 4)) =>
  (5, 4), (6, 3)

findLegalMoves(board, (0, 0)) =>
  (0, 1), (1, 0)

findLegalMoves(board, (2, 2)) =>
  [empty]

n: width of the input board
m: height of the input board

"""
def neighbour(board, start_point):
    
    # get row col of the board, start_point
    row_num, col_num = len(board), len(board[0])
    r, c = start_point[0], start_point[1]
    neighbour = []

    # check if the neighbour of start_point is reachable 
    # check boundary 
    for nr, nc in (r+1, c), (r-1, c), (r, c-1), (r, c+1):
        if ( 0 <= nr < row_num) and (0 <= nc < col_num) and board[nr][nc]==0:
            neighbour.append((nr, nc))
    return neighbour
    
    
board = [
  [0,  0,  0, -1, -1],
  [0,  0, -1,  0,  0],
  [0, -1,  0, -1,  0],
  [0,  0, -1,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
]

start1 = (3, 1)
start2 = (5, 3)
start3 = (5, 1)
start4 = (6, 0)
start5 = (6, 4)
start6 = (0, 0)
start7 = (2, 2)


print(neighbour(board, start1))
print(neighbour(board, start2))
print(neighbour(board, start3))
print(neighbour(board, start4))
print(neighbour(board, start5))
print(neighbour(board, start6))
print(neighbour(board, start7))

"""

Given a board and an end position for the player, write a function to determine if it is possible to travel from every open cell on the board to the given end position.

board1 = [
    [ 0,  0,  0, 0, -1 ],
    [ 0, -1, -1, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0, -1,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
]

board2 = [
    [  0,  0,  0, 0, -1 ],
    [  0, -1, -1, 0,  0 ],
    [  0,  0,  0, 0,  0 ],
    [ -1, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
]

board3 = [
    [ 0,  0,  0,  0,  0,  0, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0,  0,  0,  0,  0,  0, 0 ],
]

board4 = [
    [0,  0,  0,  0, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0,  0,  0,  0, 0],
]

end1 = (0, 0)
end2 = (5, 0)

Expected output:

isReachable(board1, end1) -> True
isReachable(board1, end2) -> True
isReachable(board2, end1) -> False
isReachable(board3, end1) -> False
isReachable(board4, end1) -> True

n: width of the input board
m: height of the input board

"""
import copy
def isReachable(board, end_point):
    row_num, col_num = len(board), len(board[0])
    row, col = end_point[0], end_point[1]
    counter = 0
    new_board = copy.deepcopy(board)

    def dfs(row, col):
        # traverse all the neighbours using recursive calls
        if not (0 <= row < row_num and 0 <= col < col_num):
            return False 
        if new_board[row][col] == -1:
            return False 
        if new_board[row][col] == 0:
            new_board[row][col] = -1
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
            return True

    for r in range(row_num):
        for c in range(col_num):
            if counter > 1:
                return False
            if dfs(r,c):
                counter += 1
    return True 

board1 = [
    [ 0,  0,  0, 0, -1 ],
    [ 0, -1, -1, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0, -1,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
    [ 0,  0,  0, 0,  0 ],
]

board2 = [
    [  0,  0,  0, 0, -1 ],
    [  0, -1, -1, 0,  0 ],
    [  0,  0,  0, 0,  0 ],
    [ -1, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
    [  0, -1,  0, 0,  0 ],
]

board3 = [
    [ 0,  0,  0,  0,  0,  0, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1,  0,  0,  0, -1, 0 ],
    [ 0, -1, -1, -1, -1, -1, 0 ],
    [ 0,  0,  0,  0,  0,  0, 0 ],
]

board4 = [
    [ 0,  0,  0,  0, 0 ],
    [ 0, -1, -1, -1, 0 ],
    [ 0, -1, -1, -1, 0 ],
    [ 0, -1, -1, -1, 0 ],
    [ 0,  0,  0,  0, 0 ],
]

end1 = (0, 0)
end2 = (5, 0)


print(isReachable(board1, end1)) #-> True
print(isReachable(board1, end2)) #-> True
print(isReachable(board2, end1)) #-> False
print(isReachable(board3, end1)) #-> False
print(isReachable(board4, end1)) #-> True

"""

Now the board also includes treasures, denoted by 1.

Given a board and start and end positions for the player, write a function to return the shortest simple path from start to end that includes all the treasures, if one exists. If multiple shortest paths exist, return any of them. A simple path is one that does not revisit any location.

board3_1 = [
    [  0,  0,  0, 0, 0 ],
    [  0, -1, -1, 0, 0 ],
    [  0, -1,  0, 1, 0 ],
    [ -1,  0,  0, 0, 0 ],
    [  0,  1, -1, 0, 0 ],
    [  0,  0,  0, 0, 0 ],
]

board3_2 = [
    [  0,  1, -1 ],
    [  0,  0,  0 ],
    [  0,  0,  0 ],
]

treasure(board3_1, (5, 0), (0, 4)) -> None

treasure(board3_1, (5, 2), (2, 0)) ->
  [(5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]
  Or
  [(5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]

treasure(board3_1, (0, 0), (4, 1)) ->
  [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (3, 1), (4, 1)]
  Or
  [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1)]

treasure(board3_2, (2, 1), (1, 2)) ->
  [(2, 1), (2, 0), (1, 0), (0, 0), (0, 1), (1, 1), (1, 2)]

n: width of the input board
m: height of the input board

"""

import copy
def isReachable(board, start_point, end_point):
    
    one_set = set() 
    res = []

    row_num, col_num = len(board), len(board[0])
    new_board = copy.deepcopy(board)

    #scan the board to find all ones
    for r in range(row_num):
        for c in range(col_num):
            if board[r][c] == 1:
                one_set.add((r,c))
    
    print("one_set", one_set)
    
    def dfs(row, col):
        res.append((row, col))
        
        if row == end_point[0] and col == end_point[1] and len(one_set) == 0:
            return True 
        
        # traverse all the neighbours using recursive calls
        if not (0 <= row < row_num and 0 <= col < col_num):
            return False 
        if new_board[row][col] == -1:
            return False 
        if new_board[row][col] == 1:
            # take out the position from the set, and dfs
            one_set.remove((row,col))
            
        # in place update
        new_board[row][col] = -1
        dfs(row-1, col)
        dfs(row+1, col)
        dfs(row, col-1)
        dfs(row, col+1)
        

    if not dfs(start_point[0],start_point[1]):
        return None 
    else:
        return res
    

board3_1 = [
    [  0,  0,  0, 0, 0 ],
    [  0, -1, -1, 0, 0 ],
    [  0, -1,  0, 1, 0 ],
    [ -1,  0,  0, 0, 0 ],
    [  0,  1, -1, 0, 0 ],
    [  0,  0,  0, 0, 0 ],
]

board3_2 = [
    [  0,  1, -1 ],
    [  0,  0,  0 ],
    [  0,  0,  0 ],
]

print(isReachable(board3_1,(5, 0), (0, 4)))


print(isReachable(board3_1, (5, 2), (2, 0)))









###################################################################################################
# 1. tell me a time when you work with a team and have challenge / conflicts    (win together)
# 这个问题我是往value里面的win together上靠的，就说我说动了team然后说大家出发点都是为了做好工作


# Decisive: 一样的例子说自己当机立断放弃了自己的方案而选择和 build from scratch 一起开发。
# 主要是 看到他们 知道具体要做什么，有详细的计划虽然我是团队里面最有 front-end experience, 但是还是 respect their opinion 

# Task:
# In one programming class that I took in the end of my second year, I worked in a team of eight on a final project.
# Its goals was to build a social web app that has features similar to facebook, like posting, friending, liking, 
# commenting, but based on Google Services and use Firestore as the user database. 

# Situation:
# We were given example social web app project on GitHub, but it was written with the React framework and in the TypeScript language. 
# Only me in the team had background developing on React stacks, and none of us has worked with TypeScript before. 
# We had two options: 
# - one was to reuse the front-end from the example project, 
# - The other option was to build the app's front end entirely from scratch. 
#       The conflict was, me and another team member wants to reuse the front-end code from the example project, 
#       but the rest of the team insisted on building completely from scratch.

# The context of the debate was that when we seriously started the process of the implementation, 
# there were only 2 weeks remaining, and since we have different class schedules, it wasn't easy to meet up with each other. 
# We want to pick the option that results in more features listed on the grading rubrics in the limited time frame. 


# Approach:
# Since we had a division, we setup a meeting to leverage the pros and cons of each option. The decision had to be made quick.

# Reuse option:
#     - has a lot of features completed, like friending, image upload, liking, commenting, etc. saves time re-implementing
#     - still need to spend time convert typescript to javascript, read the know source code. 
#       If there're bugs or the source code is using outdated Google APIs it would block and slow down process a lot.

# From Scratch option:
#     - the difficulty here is that we only had two weeks to build the project. 
#       If we build the app from scratch, there're a lot of technical details to figure out
#     - majority of our team members could help out

# One thing that pursuaded me to take the second approach was that, it would be too risky to take the first option. 
# if our team took the reuse option, they are all counting on me. I would be the major contributor and if they would come to me if they have any questions. 
# The bus factor of this project would be too low. if there's any chance I couldn't participate in the development on some days or if there's any bugs I couldn't resolve, the team couldn't do anything. 
# Additionally, It would make the rest of the team look useless, and they wouldn't score high in the personal contribution component of the grading.

# ==> So I decided to take the build from scratch option to win together. I actively interacted  with the rest of the team and each of us know very well of the part we were supposed to build. 
# I gave a lot of constructive opinions regarding the order of the implementation, which feature is easy to implement, which ones are hard based on my past experience. We got complete control of the code base. 

# We've got complete control of the code base. 

# Result:
#   In the final project demo day, we were the only team not reusing any existing codebase. Though we spent a lot of time implementing from scratch,
#   we still completed the majority features in the grading guideline and got a decent grade out of this project.



###################################################################################################
# 2. tell me a time when you do more than requirement   (deliver awesome)

# Situation:
# Go back to my internship at whova, one thing I did in the web team was to automate the process of importing the schedule of an event to MySQL database.

# We allow our clients to upload their schedule as formatted excel file so that they could batch upload  event schedules instead of 
# manually clicking on our app's interface to add one by one. 

# Task:
# The core functionality was to design a Database table schema allowing to store agenda information, 
# provide python functions to parse and store the excel file content and lookup the table based on the conditions. 
# The Python functions I wrote would support corresponding REST Apis consumed by the front end. 

# I think that the functions could be reused by testing of other similar features that would be developed the platform. 
# e.g. need have testing event agendas in db, so need to setup event agendas repeatedly.

# After I finished and have some extra time before the ddl, I proposed to my manager to turn it into an independently runnable script. 
# I made the script able to accept command line arguments. I discussed back and forth with my manager, 
# so clients could supply a custom start parsing position to the cli, or they could supply the policy to deal with null values, 
# or able to store information into multiple tables with name other than the default. The manager was very satisfied with my efforts put into this feature.
# So that's how the awesomeness was delivered. 


# ** Why Software Engineer? **



###################################################################################################
# 3. tell me a time when you learn new tech         (be passionate)
# # 这个问题我往passion上面靠的，就说自己想做个项目，然后在udemy上学习


# 讲去年在 evt.ai 的实习 和兼职

# - built a highly customized video player using video.js library. Supports normal video player features, pause, resume, forward, backward, fullscreen. 
# - But is also Horizontally scrollable, and supports auto-scrolling with given tracking data from backend. 

# - The difficulty was, not familiar with video.js at all and haven't built any components as heavy as a full-featured video player before, 
# it was distributed as a standalone js module, so need to integrate with React and SCSS preprocessing framework.

# - was very passionate about front-end technologies, so I started looking at example GitHub repos regarding the usage of the video.js library, 
# how to it is configured and instantiated with the react framework. 
 # After that, experimented myself. To get more familiar with it, I found several medium articles regarding the best practices of using the video.js framework.
 # I was very passionate so I wanted to know inside out, so I built some plugins for the video player. the video content is segmented so I built Custom Seekbar 
 # Marker that shows the segment interval. After doing all these above, I confidently integrated the video.js player and incrementally built to customize it.


# - It wasn't a one time thing. Later in the internship I saw that there's a library that resolves the fullscreen browser compatibility issue. So I came back, researched how it works with video.js and used that library instead of the native chrome fullscreen solution



###################################################################################################
# 4. tell me a time when you fail something   ==> (learn fast)
# 这个问题我往passion上面靠的，就说自己想做个项目，然后在udemy上学习
        # 1   and improve efficiency, 
        # 2   have a good estimation of project timeline, prioritize the tasks
        # 3   keep on hte same pace(one on one meeting)  )


# “I was developing a feature in my previous company, and I was so eager to please them that I told them we could finish the project within 2 weeks. 
# I was overly optimistic about time estimation. I thought this was doable, but it ended up taking 3 weeks due to lot of test cases and my manager was not so happy. 

# Looking back, I realized I should have been more conservative in my estimate to the client. !!!!!!! 
# I realized that my client, which was my manager in this case, isn’t going to be upset if you’re clear about the timeline in advance, 
# But they are going to be disappointed if you promise something and then don’t deliver. 

# So I took this experience and used it to become much better at managing expectations of clients during projects I oversee.
#     For example, on the next project in the second team with a different manager, I told them it’d take 4 weeks and we finished in 3. 
# They were very happy about this.” 





###################################################################################################
# BQ1：讲一段 learn from mistakes 的经历（对应 learn fast）。
# BQ2：讲一段 work with others 的经历（对应 win together），讲完两位面试官各提了一个 follow up。
    # BQ2.1：你提到了你的小组因为使用的 Python 版本不一致导致最后合并 code 的时候出现了麻烦，你从中学到了什么？
    # BQ2.2：你之前说的是作为 leader 给组员分配任务的例子，可以说说你作为 leader 帮助组员的经历吗？
# BQ3：讲一段 learn new tech 的经历（对应 be passionate）。
# BQ4：讲一段你做出的成果超出 professor / TA 预期的经历（对应 be bold / deliver awesome）。

# BQ 问完之后问我有没有想咨询他们的问题，我问了两个，一个是面试官最看重的品质，一个是 intern 是直接贡献公司代码还是有专属的 intern project。
# 问完之后刚好 20min，白人小哥哥表示很惊讶，说这么快就结束了。



###################################################################################################
# 理论上面试持续30分钟，但实际面了20分钟就结束了。

# 全是BQ，面经如下：
# 1. Give me an example that you learn from mistakes
# 2. How do you update your technical stack?
# 3. Tell me a time when you did something more than the requirement
# 4. Tell me a time when you had a conflict with others in your group, and how did you solve the conflict?
# 都是按照它家value出的题，而且问的题目非常固定，如果还有head count 好好准备肯定没问题。



###################################################################################################
# 自我介绍完直接开始问问题

# 1. 有没有和组员发生conflict，如何解决的
# 2. 和别人合作的时候，说的话有没有被误解过，如何解开误会的，从中学到了什么
# 3. 学到的最新技术是什么，如何stay updated in tech
# 4. 讲一下你是怎么解决一个问题的
# 5. do something beyond expectation的例子








