'''
HR
    Emily Hunter (BLOOMBERG/ 731 LEX) <ehunter49@bloomberg.net
    Liz Choi (BLOOMBERG/ 731 LEX) <echoi156@bloomberg.net

Final round 	4h

8/21   VO   

    第一轮，准备不充分，网上有题但是没有看懂解答。
    根据面经，面试题几乎全部是中高频的“变形”（原题其实对理解新题帮助并不大）
        reinterpretation of https://leetcode.com/problems/design-browser-history/,
    
    第二轮  
        不做题 简历deep dive + 技术探讨 40min

        问Vmware 工作内容 自己先介绍两分钟左右。之后两个人轮流问 大概问10min
            SDDC work at VMware
            What metric

        问简历出现的相关概念
            java    
                Gradle build 原理？ dependency Tree...
                deployment of service on JDK?
            docker VS VM
            Restful API


8/12  phone interview

    这个中国人语速奇快无比  10min
    Candy Crush 1D 消消乐	20 min
    1D消消乐  https://zhuanlan.zhihu.com/p/412472385
    
    简历 Follow up  10min
        how to solve scale problem  how to scale SDDC?
        what component in SDDC?     networking, storage, CPU and security
        how to build web service?
    
    Q&A:	10 min
        Key product: terminal	⇒ SAAS platform now, data platform about market data
        How to get more efficiency !!! C++ performance requirement, more in python layer.
 
7/27  HR chat
    Position
    Cloud engineer at Bloomberg
    Relocate to NY => OK
    3 days in office 2 days remote
    Fully vaccinated Covid 19
    Compensation:	
    230K - 250K TC =  cash + bonus (No RSU, private company)
'''


######################################################################################
'''
    Design and implement a module that provides a simple web browser history functionality. The module should be capable of capturing and providing the web URLs visited in chronological order (most recently visited first). Each URL should be listed only once.

    Example of inputs is to visit

    http://www.bloomberg.com,
    then visit http://www.bbc.com,
    then visit http://www.cnn.com
    then visit http://www.bbc.com again.

    The expected output for this case is:

    http://www.bbc.com
    http://www.cnn.com
    http://www.bloomberg.com

    # [h.visit(x) for x in [A B C D A D E X]]
    # h.get_history() -> [E D A C B]

    history:  (2, B), (1, A), (0, X)    MaxHeap     O(logN)

    URLMap:     {
        A: 3
        B: 2
        X: 0     
    }
'''
from collections import defaultdict
import heapq

class WebBrowser:
    def __init__(self):
        self.history = []
        self.webPageMap = defaultdict(int) # self.visitCount 
    
    def vist(self, url: str) -> None:
        if url not in self.webPageMap:
            self.webPageMap[url] += 1
            heapq.heappush(history, url)
        else:
            theURL = webPageMap[url]
            self.history.remove(theURL)
            self.webPageMap[url] += 1
            heapq.heappush(history, url)
        return None

    def get_history(self) -> list[str]:
        
        return self.history 

