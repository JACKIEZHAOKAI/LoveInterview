#############################################################################
# 10/31  实习面经
'''
    这次面试直接睡到了面试前十分钟起床，本以为挂定了完全没怎么准备而且网上也没有什么题库
    但是没想到总体表现还挺不错。

    面试的是新人刚加入concluent的韩国小哥，和我差不多大，上来基本直接做题。
    开始被面试题目有点吓到了，而且是OOD design， 因为内容很多，还是啥解析函数。register都来了，我看的有些害怕。

    不过，我专注于思考和做题，也没想那么复杂，很直观的思路解题。

    1    先不考虑isVariadic，用hashmap存 map key(para type) to value(fun name),
    implement简单的版本并且走过testcase， OK

    2    Follow Up问如果加 isVariadic，我最开始的代码逻辑并不是很好，还想着增加了另一个dict存储，
    但是之后想了下register 可以不改，改find_matches  backward tracking, 当遇到不同类型停止
    可算是on the right track, 除了沟通上有些紧张磕磕碰碰，英语流利沟通还要加强。    整体表现不错的 自己打80分

    但是有些细节是经过提示之后补上的，
        比如key  开始key是hash成一个string处理，收到anagram那道题对于key的处理的思路的影响
                用tuple存而不用string存可以避免重新construct key的时间和空间成本，slicing，
                不用list是因为tuple不可改
        比如backward tracking的时候，每走一步都要去查prev_key 有没有存，因为可能有很多不同的pre_key

    3   最后一个follow Up， 如果还要考虑supporting 0 variadics怎么做？  
        直接在reigister的时候多存一个key-value entry存储

反思：
    1   真的不再押题了，高频面经都是骗人的。。。押题只会限制自己的水平正常发挥，增加不必要的紧张
    2   相信自己的第一直觉，怎么想就怎么做。
    3   专注当下的题目，专心思考，主动和面试官沟通思路，思路确定下来后，积极implement动手打代码，问on the right track?
    4   主动traverse testcase，通过testcase矫正自己的代码

'''
#############################################################################
# register({
#    Function("funA", ["Boolean", "Integer"], isVariadic=False),
#    Function("funB", ["Integer"], isVariadic=False),
#    Function("funC", ["Integer"], isVariadic=True)            
#    Function("funD", ["Integer"], isVariadic=False),
# })

# find_matches(["Boolean", "Integer"])            -> [funA]
# find_matches(["Integer"])                       -> [funB, funC, funD]
# find_matches(["Integer", "Integer", "Integer"]) -> [funC]
  
# More Examples:
#    Function("funD", ["String", "Integer", "Integer"], isVariadic=True),
#    Function("funE", ["String", "Integer", "Integer", "Integer"], isVariadic=False)
# find_matches(["String", "Integer"])             -> [funD]   # funD due to the supporting 0 variadics
# find_matches(["String", "Integer", "Integer", "Integer"])  -> [funD, funE]



# find_matches(["String", "Integer", "Integer", "Integer"]) => []
'''
Function("funE", ["String", "Integer"], isVariadic=True)
Function("funF", ["String", "Integer", "Integer"], isVariadic=True)
Function("funG", ["String", "Integer", "Integer","Integer"], isVariadic=True)

{
"String", "Integer"        (Integer ,funE)
"String", "Integer", "Integer"    (Integer ,funF)
"String", "Integer", "Integer","Integer"    (Integer ,funG)
}

Function("funD", ["String", "Integer", "Integer","Integer"], isVariadic=False)
'''


class Function(object):
    def __init__(self, name, argumentTypes, isVariadic):
        self.name = name
        self.argumentTypes = argumentTypes
        self.isVariadic = isVariadic
     
    def __repr__(self):
        return "Function<{}>".format(self.name)

    
    
class FunctionLibrary(object):
    def __init__(self):
        self.fun_dict = {}    # maping fun para to fun name
    
    def register(self, listOfFunctions):
        
        for fun in listOfFunctions:
            
            key = tuple(fun.argumentTypes)
            # store para into fun_dict
            if key not in self.fun_dict:
                self.fun_dict[key] = [fun]
            else:
                self.fun_dict[key].append(fun)

            # FollowUp3:
            if fun.isVariadic:
                key2 = tuple(fun.argumentTypes[:len()])
                # store para into fun_dict
                if key2 not in self.fun_dict:
                    self.fun_dict[key2] = [fun]
                else:
                    self.fun_dict[key2].append(fun)

        
    def find_matches(self, argumentTypes):
        res = []
        
        # 1 can find the entire argumentTypes matches a fun
        key = tuple(argumentTypes)    
        if key in self.fun_dict:
            for f in self.fun_dict[key]:
                res.append(f.name)
        
        # FollowUp2:
        # 2 traverse backward to check if prev part matched   
        for i in range(len(argumentTypes)-1, -1, -1):
            
            prev_key = tuple(argumentTypes[:i])
            if prev_key in self.fun_dict:      
                for f in self.fun_dict[prev_key]:
                    if f.isVariadic:
                        res.append(f.name)
            
            #check when changing type
            if argumentTypes[i] != argumentTypes[i-1]:
                break

        return res
        

        
fb = FunctionLibrary()
f1 = Function("funA", ["Boolean", "Integer"], isVariadic=False)
f2 = Function("funB", ["Integer"], isVariadic=False)
f3 = Function("funC", ["Integer"], isVariadic=True)
f4 = Function("funD", ["String", "Integer", "Integer"], isVariadic=True)
f5 = Function("funE", ["String", "Integer", "Integer", "Integer"], isVariadic=False)

fb.register([f1,f2,f3,f4,f5])

print(fb.find_matches(["Boolean", "Integer"]))     #-> [funA]
print(fb.find_matches(["Integer"]))                #-> [funB, funC]
print(fb.find_matches(["Integer", "Integer", "Integer"])) # -> [funC]
        
print(fb.find_matches(["String", "Integer"]))     #-> [funD]   # funD due to the supporting 0 variadics
print(fb.find_matches(["String", "Integer", "Integer", "Integer"]))    # [funD, funE]



