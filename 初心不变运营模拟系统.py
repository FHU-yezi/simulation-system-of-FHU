print("初心不变运营模拟系统\n初心不变 超级管理员 叶子\n保留所有权利")
print("加载模块......")

try:
    print("\t初始化日志记录模块......")
    import logging
except:
    print("关键错误：缺少日志记录模块 logging，该模块用于支持日志记录功能，请先安装此模块")
finally:
    print("\t日志记录模块加载成功......")

global 运行日志,事件日志
运行日志=logging.getLogger("运行日志")
格式器=logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
输出器=logging.FileHandler("运行日志.log")
输出器.setFormatter(格式器)
运行日志.addHandler(输出器)
输出器.setFormatter(格式器)
运行日志.setLevel(logging.DEBUG)
运行日志.info("日志记录初始化成功")

事件日志=logging.getLogger("事件日志")
格式器=logging.Formatter('%(asctime)s %(levelname)s %(message)s')
输出器=logging.FileHandler("事件日志.log")
输出器.setFormatter(格式器)
事件日志.addHandler(输出器)
输出器.setFormatter(格式器)
事件日志.setLevel(logging.DEBUG)

try:
    pass
except:
    print("缺少必要组件，请检查文件是否齐全")
    运行日志.critical("缺少必要组件")
else:
    print("\t必要组件加载成功......")
    运行日志.debug("必要组件加载成功")
try:
    from random import random,randint,choice
except:
    print("关键错误：缺少 random 模块，该模块用于支持随机数功能，请先安装此模块。")
    运行日志.critical("缺少 random 模块")
else:
    运行日志.debug("\trandom 模块加载成功")
try:
    from time import time,sleep
except:
    print("关键错误：缺少 time 模块，该模块用于支持等待功能，请先安装此模块。")
    运行日志.critical("缺少 time 模块")
else:
    运行日志.debug("\ttime 模块加载成功")

print("所有模块加载成功......")
运行日志.info("所有模块加载成功")

print("初始化类......")
运行日志.info("初始化类")

print("初始化基础数值......")######应该取代

随机数=0
运行天数=0
buff=0

print("数值初始化成功......")

try:
    class 部门():
        def __init__(self):
            self.人数=0
            self.人员列表=[]
            self.能力=0
        def 加入(self):
            pass
        def 退出(self):
            pass
    class 群组运营部(部门):
        pass
    class 人力资源部(部门):
        def __init__(self):
            self.人数=0
            self.人员列表=[]
            self.群成员列表=[]
            self.能力=0
            self.当前人数=1#人数上限为 500，与真实情况相同
            self.成员编号列表=["0"]
            self.未分配部门人员=[]
        def 加入新成员(self):
            global 当前人数,buff#指针
            随机数=randint(0,10)+buff#buff 会影响成员进入概率
            if 随机数<5 and 随机数>1:#+1
                self.当前人数+=1
                加入成员编号=randint(0,499)
                self.群成员列表.append(加入成员编号)
                print("加入了 1 个新成员，该成员的编号为",加入成员编号,"。")
            elif 随机数==1:#+2
                self.当前人数+=2
                加入成员编号1=randint(0,499)
                加入成员编号2=randint(0,499)
                if (加入成员编号1!=加入成员编号2)==True:
                    if((加入成员编号1 in self.群成员列表) and (加入成员编号2 in self.群成员列表))==False:
                        人力资源部.群成员列表.append(加入成员编号1)
                        人力资源部.群成员列表.append(加入成员编号2)
                        print("加入了 2 个新成员，这些成员的编号为",加入成员编号1,"和",加入成员编号2)
            elif 随机数==0:#+3
                self.当前人数+=3
                加入成员编号1=randint(0,499)
                加入成员编号2=randint(0,499)
                加入成员编号3=randint(0,499)
                if 加入成员编号1!=加入成员编号2!=加入成员编号3 and ((加入成员编号1 in self.群成员列表) and (加入成员编号2 in self.群成员列表) and (加入成员编号3 in self.群成员列表)):
                    人力资源部.群成员列表.append(加入成员编号1)
                    人力资源部.群成员列表.append(加入成员编号2)
                    人力资源部.群成员列表.append(加入成员编号3)
                    print("加入了 3 个新成员，这些成员的编号为",加入成员编号1,"、",加入成员编号2,"和",加入成员编号3,"。")
        def 成员退出(self):
            if self.群成员列表!=["0"]:#如果没有可以退出的人就跳过
                self.当前人数-=1
                退出成员编号=choice(self.群成员列表)
                if 退出成员编号=="0":#你肯定不能让自己退出
                    退出成员编号=choice(self.成员列表)
                else:
                    ####功能缺失
                    #成员列表.remove(退出成员编号)
                    print("有 1 个成员退出了初心不变，他的成员编号是",退出成员编号,"。")
    class 文案宣传部(部门):
        def __init__(self):
            self.人数=0
            self.人员列表=[]
            self.能力=0
            self.当前进行文案="无"
            self.状态="无正在进行的文案"
            self.总文案数量=0
        def 新文案(self):
            pass
        def 文案处理(self):
            pass
    class 舆情分析部(部门):
        def __init__(self):
            self.人数=0
            self.人员列表=[]
            self.能力=0
            self.舆情事件进行中=False
            self.当前进行舆情事件编号=0
            self.舆情事件等级="无"
            self.舆情事件产生者=""
            self.总舆情事件数量=0
            self.舆情事件编号列表=[]
        def 新舆情事件(self):
            self.舆情事件产生者=choice(人力资源部.群成员列表)#随便选一个人中招
            self.舆情事件进行中=True
            self.总舆情事件数量=1+总舆情事件数量#舆情数量+1
            self.当前舆情事件编号=randint(0,300)#随机产生编号
            while True:#判断编号是否存在于列表中
                if (self.当前舆情事件编号 in self.舆情事件编号列表)==False:
                    self.舆情事件编号列表.append(self.当前舆情事件编号)
                    break
                else:
                    self.当前舆情事件编号=randint(0,300)
            本次buff=round(random(),3)#随机降低 buff
            buff=buff-本次buff
            if self.舆情分析部能力==0:
                self.舆情事件等级="重要"
            elif self.舆情分析部能力<=5:
                self.舆情事件等级="一般"
            elif self.舆情分析部能力<=10:
                self.舆情事件等级="微弱"
            elif self.舆情分析部能力>10:
                self.舆情事件等级="微不足道"
            print("产生了一个新的舆情事件，该事件的编号为",当前舆情事件编号,"，该事件是由",舆情事件产生者,"产生的。该事件的等级为：",舆情事件等级,"\n该事件导致成员加入概率降低了",本次buff)
        def 舆情事件处理(self):
            pass
    运行日志.debug("初始化部门类成功")

    class 用户():
        def __init__(self,编号):
            self.编号=编号
            self.满意度=randint(30,71)
            self.活跃度=randint(0,11)
    运行日志.debug("初始化用户类成功")

    class 管理组():
        def __init__(self):
            self.人数=0
            self.人员列表=[]
except:
    print("初始化类失败")
    运行日志.critical("初始化类失败")
else:
    print("初始化所有类成功......")
    运行日志.info("初始化类成功")

运行日志.info("初始化对象")
try:
    群组运营部=群组运营部()
    人力资源部=人力资源部()
    文案宣传部=文案宣传部()
    舆情分析部=舆情分析部()
    运行日志.debug("初始化部门对象成功")

    for i in range(500):
        exec("用户"+str(i)+"=用户("+str(i)+")")
    运行日志.debug("初始化用户对象成功")
except:
    print("初始化对象失败")
    运行日志.critical("初始化对象失败")
else:    

    运行日志.info("初始化对象成功")
    print("初始化对象成功")

print("初始化函数......")
#函数初始化开始


def 查看运营情况():
    print("你想要查看运营情况吗？(Y/N)")
    回答=input("")
    if 回答=="Y": 
        print("群组运营部：\n现在是模拟系统中的第",运行天数,"天")
        print("文案宣传部：\n当前进行文案：",当前进行文案,"\n状态：",状态,"\n总文案数量：",总文案数量)
        print("舆情分析部：\n当前进行舆情事件编号",当前进行舆情事件编号,"\n舆情事件等级：",舆情事件等级,"\n总舆情事件数量：",总舆情事件数量)
        print("人力资源部：\n当前人数：",当前人数,"\n当前 buff 加成：",buff,"\n当前综合退群率：",4*buff*-1,"%")
        input("按下 Enter 键继续")
    else:
        print("您跳过了查询")
    
#函数初始化结束
print("函数初始化成功......")
print("即将开始模拟......")
sleep(2)
#主程序
while True:
    运行天数=1+运行天数
    print("今天是第",运行天数,"天")
    随机数=randint(0,10)
    if 随机数==0:
        舆情分析部.新舆情事件()
    elif 随机数>0 and 随机数<5:
        人力资源部.加入新成员()
    elif 随机数>4 and 随机数<9:
        人力资源部.成员退出()
    else:
        print("风平浪静的一天。")
    查看运营情况()
#判断模块####################功能
