print("初心不变运营模拟系统\n初心不变 超级管理员 叶子\n保留所有权利")

class 初始化失败错误(Exception):
    pass

class 单元测试错误(Exception):
    pass
class 成员不存在错误(Exception):
    pass
"""
自定义错误类
具体细节请查看用户手册
"""

print("加载模块......")

try:
    pass
    from random import random,randint,choice
    from time import time,sleep
    from pickle import dump,load#非必要
    import logging
except ModuleNotFoundError:
    raise 初始化失败错误("您的 Python 缺少必要模块，请查看用户手册获取帮助")
else:
    print("模块加载成功......")

try:
    运行日志 = logging.getLogger("运行日志")
    格式器 = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
    输出器 = logging.FileHandler("运行日志.log")#运行日志输出文件
    输出器.setFormatter(格式器)
    运行日志.addHandler(输出器)
    输出器.setFormatter(格式器)
    运行日志.setLevel(logging.INFO)#运行日志等级
    运行日志.info("日志记录初始化成功")
    事件日志 = logging.getLogger("事件日志")
    格式器 =logging.Formatter('%(asctime)s %(message)s')
    输出器 = logging.FileHandler("事件日志.log")#事件日志输出文件
    输出器.setFormatter(格式器)
    事件日志.addHandler(输出器)
    输出器.setFormatter(格式器)
    事件日志.setLevel(logging.DEBUG)#事件日志等级（无意义）
except:
    运行日志.critical("初始化日志记录失败")
    raise 初始化失败错误("初始化日志记录失败，请查看用户手册")
else:
    print("日志记录初始化成功......")
    运行日志.info("模块加载成功")

print("初始化类......")
运行日志.info("初始化类")

print("初始化基础数值......")

try:
    随机数 = 0
    运行天数 = 0
    警告次数 = 0
    存档文件状态码 = 0
except:
    运行日志.critical("初始化数值失败")
    raise 初始化失败错误("初始化数值失败，请查看用户手册")
else:
    print("数值初始化成功......")
    运行日志.info("初始化数值成功")

try:
    class 部门():
        def __init__(self):
            self.人数 = 0
            self.部门人员列表 = [ ]
            self.能力 = 0
        def 部门成员加入(self,编号):
            if 编号 in 人力资源部.群成员列表:
                self.部门人员列表.append(编号)
                事件日志.info("编号为"+str(编号)+"的成员加入了",self.__class__)
            else:
                raise 成员不存在错误("编号为"+str(编号)+"的成员不在群中")
        def 部门成员退出(self,编号):
            if 编号 in 人力资源部.群成员列表 and 编号 in self.部门人员列表:
                self.部门人员列表.remove(编号)
                事件日志.info("编号为"+str(编号)+"的成员退出了",self.__class__)
            else:
                raise 成员不存在错误("编号为"+str(编号)+"的成员不在群或部门中")

        def __str__(self):
            return "一个未定义名称的部门：\n\t人数："+str(self.人数)+"\n\t能力："+str(self.能力)+"\n\t人员列表："+str(self.部门人员列表)

    class 群组运营(部门):
        """
        后期会继续添加更多方法
        """
        def __str__(self):
            return "群组运营部：\n\t人数："+str(self.人数)+"\n\t能力："+str(self.能力)+"\n\t部门人员列表："+str(self.部门人员列表)

    class 人力资源(部门):
        def __init__(self):
            self.人数 = 0
            self.部门人员列表 = [ ]
            self.群成员列表 = list(range(15))#range 会返回一个生成器，需要用 list 转换
            self.能力 = 0
            self.当前群人数 = 15#人数上限为 500，与真实情况相同
        def 群成员加入(self):
            for i in range(500):
                temp_dict = {"进入":False}
                exec("if 用户"+str(i)+".满意度 >= 70 and 用户"+str(i)+".活跃度 >= 7 and 用户"+str(i)+".在群中 == False and randint(0,11) == 1:进入=True",globals(),temp_dict)#别随便改这个，很复杂
                if temp_dict["进入"] == True:
                    exec("用户"+str(i)+".在群中=True",globals())
                    self.群成员列表.append(i)
                    self.当前群人数+=1
                    print("有 1 个成员进入了初心不变，他的成员编号是",i)
                    事件日志.debug("编号为"+str(i)+"的成员加入了初心不变")
            del temp_dict
        def 群成员退出(self):
            for i in range(500):
                temp_dict = {"退出":False}
                exec("if 用户"+str(i)+".满意度 <= 30 and 用户"+str(i)+".活跃度 <= 3 and 用户"+str(i)+".在群中 == True and randint(0,11) == 1:进入=True",globals(),temp_dict)#别随便改这个，很复杂
                if temp_dict["退出"] == True and i != 0:#不能让自己退出
                    exec("用户"+str(i)+".在群中=False",globals())
                    self.群成员列表.remove(i)
                    self.当前群人数-=1
                    print("有 1 个成员退出了初心不变，他的成员编号是",i)
                    事件日志.debug("编号为"+str(i)+"的成员退出了初心不变")
            del temp_dict
        def __str__(self):
            return "人力资源部：\n\t人数："+str(self.人数)+"\n\t能力："+str(self.能力)+"\n\t部门人员列表："+str(self.部门人员列表)+"\n\t当前群人数："+str(self.当前群人数)

    class 文案宣传(部门):
        def __init__(self):
            self.人数 = 0
            self.部门人员列表 = [ ]
            self.能力 = 0
            self.文案列表 = [ ]
            self.当前进行文案 = None
            self.总文案数量 = 0
            self.当前文案进度 = None
        def 新文案(self):
            if self.当前进行文案:
                if input("当前已经有一个文案，如创建新文案，将会覆盖原先的文案，是否确认？(y/n)")=="y":
                    文案名称 = input("请输入文案名称：")
                    self.当前进行文案 = 文案名称
                    self.文案列表.append(文案名称)
                    self.总文案数量 += 1
                    print("名为",文案名称,"的文案已成功创建！")
                    事件日志.info("创建了一个叫做"+文案名称+"的文案")
            else:
                文案名称=input("请输入文案名称：")
                self.当前进行文案 = 文案名称
                self.文案列表.append(文案名称)
                self.总文案数量 += 1
                print("名为",文案名称,"的文案已成功创建！")
                事件日志.info("创建了一个叫做"+文案名称+"的文案")
        def 文案处理(self):
            self.当前文案进度 += self.能力+randint(1,10)
            print("名为",self.当前进行文案,"的文案进度增加了",self.能力+3,"点")
            事件日志.info(str(self.当前进行文案)+"的文案进度增加了"+str(self.能力+3)+"点")
        def 文案完成度检测(self):
            if not self.当前进行文案:
                print("您当前没有文案，请先创建文案！")
            elif self.文案完成度 >= 100:
                文案质量=randint(0,101)
                print("您完成了一篇新的文案，其质量为",文案质量,"，全体成员活跃度与满意度上升！")
                for i in range(500):
                    exec("用户"+i+".活跃度+=int(文案质量/10)",globals())
                    exec("用户"+i+".满意度+=文案质量",globals())
                self.当前进行文案 = None
                self.当前文案进度 = None
                事件日志.info("完成了叫做"+self.当前进行文案+"的文案，质量为",文案质量)
        def __str__(self):
            return "文案宣传部：\n\t人数："+str(self.人数)+"\n\t能力："+str(self.能力)+"\n\t部门人员列表："+str(self.部门人员列表)+"\n\t当前进行文案："+str(self.当前进行文案)+"\n\t当前文案进度："+str(self.当前文案进度)

    class 舆情分析(部门):
        def __init__(self):
            self.人数 = 0
            self.部门人员列表 = [ ]
            self.能力 = 0
            self.当前舆情事件编号 = None
            self.舆情事件等级 = None
            self.舆情事件产生者 = None
            self.舆情事件指数 = None
            self.舆情事件编号列表 = [ ]
        def 新舆情事件(self):
            if 人力资源部.当前群人数 != 1 and not self.当前舆情事件编号:
                self.舆情事件产生者 = choice(人力资源部.群成员列表)
                self.当前舆情事件编号 = randint(0,501)
                while True:
                    if (self.当前舆情事件编号 in self.舆情事件编号列表) == False:
                        self.舆情事件编号列表.append(self.当前舆情事件编号)
                        break
                    else:
                        self.当前舆情事件编号 = randint(0,501)
                self.舆情事件指数 = randint(10,101)-self.能力*3
                print("产生了一个新的舆情事件，该事件的编号为",self.当前舆情事件编号,"，该事件是由",self.舆情事件产生者,"产生的。舆情事件指数为：",self.舆情事件指数)
                事件日志.info("产生了编号为"+str(self.当前舆情事件编号)+"的舆情事件")
        def 舆情事件处理(self):
            while True:
                if randint(1,10) == 1:#十分之一的概率会直接凉凉
                    结束("遇到了一个无法处理的舆情事件")
                回答 = input("舆情事件：请选择您要进行的操作：\n<1>发布声明\n<2>不予理睬\n<3>停止运营")
                if 回答 == "1":
                    temp=randint(1,5)
                    self.舆情事件指数 -= self.能力+temp
                    print("舆情事件指数降低了",self.能力+temp)
                    事件日志.info("舆情事件指数降低了"+str(self.能力+temp))
                    if self.舆情事件指数 <= 0:
                        self.舆情事件结束()
                    break
                elif 回答 == "2" or 回答 == "":
                    print("您选择不予理睬")
                    事件日志.info("对于舆情事件，选择了不予理睬")
                    break
                elif 回答 == "3":
                    if input("该操作不可逆，请输入 y 确认.....") == "y":
                        结束("您在一次舆情事件中主动停止运营")
                    break
        def 舆情事件结束(self):
            print("编号为",self.当前舆情事件编号,"的舆情事件结束")
            self.舆情事件等级 = None
            self.舆情事件产生者 = None
            self.当前舆情事件编号 = None
            self.舆情事件指数 = None
        def __str__(self):
            return "舆情分析部：\n\t人数："+str(self.人数)+"\n\t能力："+str(self.能力)+"\n\t部门人员列表："+str(self.部门人员列表)+"\n\t当前舆情事件产生者："+str(self.舆情事件产生者)

    运行日志.debug("初始化部门类成功")

    class 用户():
        def __init__(self,编号):
            self.编号 = 编号
            self.满意度 = randint(30,71)
            self.活跃度 = randint(0,10)
            self.计算机技术 = randint(0,10)#未使用
            self.所属部门 = None
            self.在群中 = False

    运行日志.debug("初始化用户类成功")

    class 管理组():#未使用
        def __init__(self):
            self.人数 = 0
            self.人员列表 = [ ]
except:
    运行日志.critical("初始化类失败")
    raise 初始化失败错误("初始化类失败，请查看用户手册")
else:
    print("初始化类成功......")
    运行日志.info("初始化类成功")

运行日志.info("初始化对象")

try:
    群组运营部 = 群组运营()
    人力资源部 = 人力资源()
    文案宣传部 = 文案宣传()
    舆情分析部 = 舆情分析()
    运行日志.debug("初始化部门对象成功")

    for i in range(500):
        exec("用户"+str(i)+"=用户("+str(i)+")")#用户批量实例化，核心代码
    for i in range(30):
        exec("用户"+str(i)+".在群中=True")
    运行日志.debug("初始化用户对象成功")
except:
    运行日志.critical("初始化对象失败")
    raise 初始化失败错误("初始化对象失败，请查看用户手册")
else:
    运行日志.info("初始化对象成功")
    print("初始化对象成功......")

print("初始化函数......")

try:
    def 主程序():
        print("即将开始模拟......")
        sleep(1)
        事件日志.info("开始")
        while True:
            global 运行天数
            运行天数 += 1
            print("今天是第",运行天数,"天")
            事件日志.info("第"+str(运行天数)+"天")
            if randint(0,11) <= 3:
                舆情分析部.新舆情事件()
                运行日志.debug("触发新舆情事件")
            if randint(0,11) <= 5:
                人力资源部.群成员加入()
                运行日志.debug("触发成员加入事件")
            if randint(0,11) <= 5:
                人力资源部.群成员退出()
                运行日志.debug("触发成员退出事件")
            if 文案宣传部.当前进行文案:
                文案宣传部.文案处理()
                运行日志.debug("触发文案处理事件")
            if 舆情分析部.当前舆情事件编号:
                舆情分析部.舆情事件处理()
                运行日志.debug("触发舆情处理事件")
            用户操作()
            if 人力资源部.当前群人数 <= 10:
                警告次数 += 1
                print("警告：人数不足！（如连续出现此警告 10 次将结束）")
                运行日志.info("触发人数不足事件")
            else:
                警告次数 = 0
                运行日志.debug("警告次数归零")
            if 警告次数 >= 10:
                结束("人数不足")

    def 初始操作():
        while True:
            回答=input("请选择您要进行的操作：\n\t<1>开始新的模拟\n\t<2>读取存档\n\t:")
            if 回答 == "1":
                主程序()
                break
            elif 回答 == "2":
                读取存档()
                主程序()
                break
            elif 回答 == "Debug_Mode":
                print("Debug Mode")
                运行日志.setLevel(logging.DEBUG)
                运行日志.warning("Debug 模式开启")
                主程序()
                break
            elif 回答 == "Unit_Test":
                单元测试()
                break
            else:
                print("输入无效！")

    def 用户操作():
        回答 = input("请选择您的操作：\n\t<1>查看运营情况\n\t<2>创建新文案\n\t<3>保存存档\n\t<4>更改成员对应部门\n\t:")
        if 回答 == "1": 
            print(群组运营部)
            print(文案宣传部)
            print(舆情分析部)
            print(人力资源部)
            input("按下 Enter 键继续")
            运行日志.debug("用户查看了运营情况")
        elif 回答 == "2":
            文案宣传部.新文案()
        elif 回答 == "3":
            保存存档()
        elif 回答 == "4":
            部门成员操作()
        elif 回答 == "Debug_Mode":
            print("Debug Mode")
            运行日志.setLevel(logging.DEBUG)
            运行日志.warning("Debug 模式开启")
        else:
            print("您跳过了查询")

    def 结束(原因):
        print("您结束了长达",运行天数,"个虚拟天的初心之旅，因为",原因,"。")
        print("但是，初心不变的种子仍在，它将重新启动，继续在这个神秘莫测的环境中进化，欢迎您再次归来。")
        运行日志.info("结束")
        事件日志.info("结束运营，因为"+原因)
        input("按下 Enter 键退出......")
        exit()

    def 保存存档():
        try:
            with open("存档文件.sav","wb") as 存档文件:
                print("开始保存存档......")
                dump(存档文件状态码)
                dump(群组运营部,存档文件)
                dump(人力资源部,存档文件)
                dump(文案宣传部,存档文件)
                dump(舆情分析部,存档文件)
                dump(随机数,存档文件)
                dump(运行天数,存档文件)
                dump(警告次数,存档文件)
                for i in range(500):
                    exec("dump(用户"+str(i)+",存档文件)")
                print("存档成功！")
                运行日志.info("存档成功")
        except:
            print("存档失败！")
            运行日志.error("存档失败")

    def 读取存档():
        try:
            with open("存档文件.sav","rb") as 存档文件:
                global 存档文件状态码,群组运营部,人力资源部,文案宣传部,舆情分析部,随机数,运行天数,警告次数
                print("开始读取存档......")
                存档文件状态码 = load(存档文件)
                群组运营部 = load(存档文件)
                人力资源部 = load(存档文件)
                文案宣传部 = load(存档文件)
                舆情分析部 = load(存档文件)
                随机数 = load(存档文件)
                运行天数 = load(存档文件)
                警告次数 = load(存档文件)
                for i in range(500):
                    exec("用户"+str(i)+"=load(存档文件)")
                print("读档成功！")
                运行日志.info("读档成功")
                if 存档文件状态码 != 0:
                    print("警告：该存档文件未通过校验，其中可能含有恶意代码，请您知悉！")
                    运行日志.warning("存档文件校验失败")
        except FileNotFoundError:
            print("无存档文件！")
            运行日志.error("无存档文件")
        except:
            print("读档失败！")
            运行日志.error("读档失败")

    def 单元测试():
        for i in range(500):
            exec("global 用户"+str(i))
        测试类型 = input("请选择您要进行的测试类型：\n\t<1>完整测试\n\t<2>快速测试")
        if 测试类型 == "1":
            print("开始运行完整单元测试......")
            for _ in range(100):
                temp_dict = {}
                temp_int = randint(0,499)
                exec("if 0 <= 用户"+str(temp_int)+".编号 < 500:OK = True",globals(),temp_dict)
                if temp_dict["OK"] != True:
                    raise 单元测试错误("测试"+str(_)+"号对象的 编号 属性时出现问题")
                exec("if 30 <= 用户"+str(temp_int)+".满意度 <= 71:OK = True",globals(),temp_dict)
                if temp_dict["OK"] != True:
                    raise 单元测试错误("测试"+str(_)+"号对象的 满意度 属性时出现问题")
                exec("if 0 <= 用户"+str(temp_int)+".活跃度 <= 10:OK = True",globals(),temp_dict)
                if temp_dict["OK"] != True:
                    raise 单元测试错误("测试"+str(_)+"号对象的 活跃度 属性时出现问题")
                exec("if 0 <= 用户"+str(temp_int)+".计算机技术 <= 10:OK = True",globals(),temp_dict)
                if temp_dict["OK"] != True:
                    raise 单元测试错误("测试"+str(_)+"号对象的 计算机技术 属性时出现问题")
                exec("if  用户"+str(temp_int)+".所属部门 in (None,'群组运营部','人力资源部','文案宣传部','舆情分析部'):OK = True",globals(),temp_dict)
                if temp_dict["OK"] != True:
                    raise 单元测试错误("测试"+str(_)+"号对象的 所属部门 属性时出现问题")
                exec("if 用户"+str(temp_int)+".在群中 == True or 用户"+str(temp_int)+".在群中 == False:OK = True",globals(),temp_dict)
                if temp_dict["OK"] != True:
                    raise 单元测试错误("测试"+str(_)+"号对象的 在群中 属性时出现问题")
            print("完成用户类随机抽样测试，未发现问题")
        elif 回答 == "2":
            for _ in range(20):
                temp_dict = {}
                temp_int = randint(0,499)
                exec("if 0 <= 用户"+str(temp_int)+".编号 < 500:OK = True",globals(),temp_dict)
                if temp_dict["OK"] != True:
                    raise 单元测试错误("测试"+str(_)+"号对象的 编号 属性时出现问题")
                exec("if 30 <= 用户"+str(temp_int)+".满意度 <= 71:OK = True",globals(),temp_dict)
                if temp_dict["OK"] != True:
                    raise 单元测试错误("测试"+str(_)+"号对象的 满意度 属性时出现问题")
                exec("if 0 <= 用户"+str(temp_int)+".活跃度 <= 10:OK = True",globals(),temp_dict)
                if temp_dict["OK"] != True:
                    raise 单元测试错误("测试"+str(_)+"号对象的 活跃度 属性时出现问题")
                exec("if 0 <= 用户"+str(temp_int)+".计算机技术 <= 10:OK = True",globals(),temp_dict)
                if temp_dict["OK"] != True:
                    raise 单元测试错误("测试"+str(_)+"号对象的 计算机技术 属性时出现问题")
                exec("if  用户"+str(temp_int)+".所属部门 in (None,'群组运营部','人力资源部','文案宣传部','舆情分析部'):OK = True",globals(),temp_dict)
                if temp_dict["OK"] != True:
                    raise 单元测试错误("测试"+str(_)+"号对象的 所属部门 属性时出现问题")
                exec("if 用户"+str(temp_int)+".在群中 == True or 用户"+str(temp_int)+".在群中 == False:OK = True",globals(),temp_dict)
                if temp_dict["OK"] != True:
                    raise 单元测试错误("测试"+str(_)+"号对象的 在群中 属性时出现问题")
            print("完成用户类随机抽样测试，未发现问题")
        print("完成所有单元测试，未发现问题")

    def 部门成员操作():
        print("目前成员情况如下：")
        print("成员编号\t所属部门")
        for 成员 in 人力资源部.群成员列表:
            print(成员,end = "\t\t")
            exec("print(用户"+str(成员)+".所属部门)",globals())
        运行日志.info("用户查看了成员/部门列表")
        编号 = int(input("\n请输入您要操作的成员编号:"))
        if 编号 in 人力资源部.群成员列表:
            回答 = int(input("您要把这位成员变更到哪个部门中？\n\t<0>无\n\t<1>群组运营部\n\t<2>人力资源部\n\t<3>文案宣传部\n\t<4>舆情分析部\n\t请输入对应编号:"))
            if 回答 == 0:
                try:
                    群组运营部.部门成员退出()
                    人力资源部.部门成员退出()
                    文案宣传部.部门成员退出()
                    舆情分析部.部门成员退出()
                except 成员不存在错误:
                    pass
                exec("用户"+str(编号)+".所属部门 = None",globals())
                运行日志.info("编号为"+str(编号)+"的成员退出了部门")
                事件日志.info("编号为"+str(编号)+"的成员退出了部门")
            elif 回答 == 1:
                群组运营部.部门成员加入(编号)
                exec("用户"+str(编号)+".所属部门 = '群组运营部'",globals())
                运行日志.debug("编号为"+str(编号)+"的陈冠进入了群组运营部")
                事件日志.info("将编号为"+str(编号)+"的成员分配到了群组运营部")
            elif 回答 == 2:
                人力资源部.部门成员加入(编号)
                exec("用户"+str(编号)+".所属部门 = '人力资源部'",globals())
                运行日志.debug("编号为"+str(编号)+"的陈冠进入了人力资源部")
                事件日志.info("将编号为"+str(编号)+"的成员分配到了人力资源部")
            elif 回答 == 3:
                文案宣传部.部门成员加入(编号)
                exec("用户"+str(编号)+".所属部门 = '文案宣传部'",globals())
                运行日志.debug("编号为"+str(编号)+"的陈冠进入了文案宣传部")
                事件日志.info("将编号为"+str(编号)+"的成员分配到了文案宣传部")
            elif 回答 == 4:
                舆情分析部.部门成员加入(编号)
                exec("用户"+str(编号)+".所属部门 = '舆情分析部'",globals())
                运行日志.debug("编号为"+str(编号)+"的陈冠进入了舆情分析部")
                事件日志.info("将编号为"+str(编号)+"的成员分配到了舆情分析部")
            else:
                print("输入无效！")
            print("已成功将",编号,"号成员添加到此部门！")
        else:
            print("此成员不在群中！")
except:
    运行日志.critical("初始化函数失败")
    raise 初始化失败错误("初始化函数失败，请查看用户手册")
else:
    运行日志.info("初始化函数成功")
    print("函数初始化成功......")

初始操作()#入口