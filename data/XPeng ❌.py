# 数字化营销，用户增长岗位？
# 	算法（5-6），数据开发，后台。。。30+人

# DE技术栈：统计 建模 SQL。 大数据开发，国内一般用阿里 腾讯云的数据平台。

# 广州


# 利用词典对文章进行分词，词典文件中每一行是一个词，如
# 中国
# 中华人民共和国
# 人民
# 成员

# 利用这个词典文件，对文章的内容进行切词，要求最大匹配，如
# 我 是 中华人民共和国 的 成员

# 输出
# 我
# 是
# 中华人民共和国
# 的
# 成员

def FMM_func(dic, sentence):
	# FMM
	# O(n)

	# find max len in dic
    max_len = max([len(item) for item in dic])
    start = 0
    length = len(sentence)
    res = []

    while start != length:
        end = start+max_len
        if end > length:
            end = length
        # traverse the substring
        for i in range(length):
            substring = sentence[start:end]
            if (substring in dic) or (len(substring)==1):
                res.append(substring)
                # print(substring)
                start = end
                break
            end += -1
    return res

dic = ['中国','中华','中华人民共和国','人民','成员']
sentence = '我是中华人民共和国的成员'
print(FMM_func(dic, sentence))


# 优化数据结构？Tries tree存储

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr_node = self.root
        # iterate the word by char to build the word in the Trie
        for c in word:
            curr_node = curr_node.children[c]
        curr_node.is_word = True

    def search(self, word: str):
    	# return a bool whether found it
        curr_node = self.root
        # iterate the word by char to traverse the word in the Trie
        for c in word:
            curr_node = curr_node.children.get(c)
            if curr_node == None:
                return False
        return curr_node.is_word



