'''
五轮面试 Fk。。。

Interview 参考xpeng面试
    1. 工作经历（uber, pony, tusimple）自动驾驶相关
    2. 业务逻辑相关? impact? collebration? vmware on aws(cloud infra)
    3. 自动驾驶场景的问题

（V&V团队背景很杂，交通车辆背景，汽车背景，自动化，CS）
一面
    Coding：做题2道题
    tech-stack: python 代码能力！！！ （Pandas！！！） SQL
TLM
    不侧重SDE，V&V 复合背景的很多（tianyu wu）
    计算机基础知识优先级很低，项目经历很重呀，（pony Tusimple Uber）
    ！！！工作中，更看重如何解决自动驾驶的业务问题！！！
    ！！！更偏向自动驾驶业务方面！！！ （ex 如何评估车辆变道的表现，介个维度）
3面 backtoback 技术岗位

####################################################################
JD:  Autonomous Vehicles -> Verification and Validation
    1. Develop and maintain test plans and test cases for autonomous driving software
    2. Develop and maintain test automation tools 
    3. Execute test cases and analyze test results
    4. Report and track issues found during testing

tech-stack: python, SQL, Spark, MapReduce 
    对自动驾驶系统功能！！！
        Appolo  system requirement -》 看
        component配合 上下游 能力边界, 
        不需要具体算法，模块的抽象层）
    support QA
    1. 数据挖掘 data analysis
    2. 可视化工具

Future plan:
    各模块output的signal, 提取数据, 计算   
    充分测试软件场景（加速验证）场景库 测试完全

路测?
    路测， 中国 德国 美国
    中国的data不能出境， 不能出国，但是美国的数据可以在中国处理（图森数据敏感，Plus，Aurora）
    合作一体化，解决区域问题（cofing 根据各地config）codebase

团队:
    Xpeng 过来的 xinzhou Wu，直接成立BU，report 老黄。
        Automas vehicle 负责人。 目前在reorg
        全栈自动驾驶，算法，infra，软件，测试，simuation，devops
        1000-2000 BU，中国200-300，明年扩招！
            上海 HQ
            北京 深圳

挑战？
BU
    1.  wu xinzhou - Leader 来之后，目标是迭代速度提升，高效闭环，CICD 软件稳定性
V&V 
    1.  大规模路测数据分析，自动化测试，测试工具开发
            release 版本覆盖率
            自动化evaluation
            tools支持
    2.  产品化，工具化，自动化

Question：
    1.  cloud infra -》 云计算，云服务，云平台。 云计算基础设施，云计算平台，云计算服务。
    2.  VMC -》 vmware on aws, 全部服务化，Java-springboot
    3.  为什么回国工作？ 家里人生病
####################################################################
'''

# Hackrank 写代码。。。python写的跟坨屎一样。。。

bad_frames = data_df.loc[(data_df["is_auto"] == 1) & (data_df["lateral_offset"] > 0.5)]  
print(bad_frames)

# EOL产线 sensor set 

# 之前经历不合适？ 车载工具   
#     All in  和自动驾驶强绑定 需求制定 版本把控












