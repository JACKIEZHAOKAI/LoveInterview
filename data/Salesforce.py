##########################################################
'''
    Quip    11/4 店面一面
    上来直接做题，tech lead 白人女生面，题目不难，基本上就是扫一遍string看delimiter在不在set里面
    如果在的话再用两个list分别存words, delimeters, reverse一下words list，最后再拼起来输出string。
    主要卡在了一些edge case，通过分析走testcase和面试官引导并且及时debug解决了。
    11：10--11：45大概35min面完了
    
    然后blabla聊了些BQ问题，quip是12年新起的starttup做办公软件，80+engineer团队很小，实习全美招4-5个，
    而且期望都是fullstack 基本上一个组一个，可能会非常难。

    反思：
        1   不准备有时候就是最好的准备，正因为没有面经，所以可以把所有精力投入题目本身的思考
        2   紧跟面试官思路，积极思考debug，问题一定要拆分分快完成，现在的水平还是不可能一口气写下来workable code。
            开始遇到bug没问题，只要能够积极思考并且figure our，完成了大体框架思路，要hint也没问题，面试本来就是考察沟通技能。
'''
##########################################################
"""
You are given a string and a set of delimiters, reverse the words in the given string. 
(Each substring between two consecutive delimiters is a word) You need to preserve the order of delimiters. 

delimiters = {' '}
"mouse cat"  => "cat mouse"

delimiters = {' ', '_',  '/'}
"dog/cat_mouse" => "mouse/cat_dog"

delimiters = {}
"mouse cat"  => "mouse cat"

delimiters = {'0'}
"mouse cat"  => "mouse cat"

delimiters = {'0'}
"mous00 ecat"  => "mous",

delimiters = {'0'}
"a0b"  => "b0a",
"a00b"  => "b00a",


"dog/cat_mouse" => 
    [dog,cat,
    [/,_]

"mouse/cat_dog"

"""

def reverseString(string, delimiters):
    '''
    Time     O(n)    n =len(string)
    Space    O(n)
    '''
    # edge case check    O(n * d)
    # for d in delimiters:
    #     if string.split(d) == list(string):
    #         return string

    if not string or not delimiters:
        return string
    
    word_list = []
    delimiter_list = []    # off by ones
    res = []
    start = 0
    
    for end in range(len(string)):
        # deal with last char
        if end == len(string)-1:
            if string[end] in delimiters:
                word_list.append(string[start:end])
                delimiter_list.append(string[end])
                word_list.append("")
            else:
                word_list.append(string[start:end+1])
        # parsing
        else:
            if string[end] in delimiters:
                word_list.append(string[start:end])
                delimiter_list.append(string[end])
                start = end + 1
    
    # print(word_list, delimiter_list)
    
    # reverse the word_list
    word_list.reverse()
    
    # reconstruct the res string
    for i in range(len(word_list)-1):
        res.append(word_list[i])
        res.append(delimiter_list[i])
    res.append(word_list[-1])
    
    return ''.join(res)
    
    
    
# print(reverseString("mouse cat", set([' '])))    #"cat mouse"

# print(reverseString("dog/cat_mouse", set([' ','_','/'])))    # "mouse/cat_dog"

# print(reverseString("mouse cat", set(['0'])))    # mouse cat


print(reverseString("/dog/cat_mouse/", set(["/", "_"])))    # "/mouse/cat_dog/"
# print(reverseString("dog//cat_mouse", set(["/", "_"])))    # "mouse/cat/_dog"
# """
# "dog", "", "cat", "mouse"
# "/dog/cat_mouse/" => "", "dog", "cat", "mouse", ""
# ""
# "

