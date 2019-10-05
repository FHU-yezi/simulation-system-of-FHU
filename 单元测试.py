print("单元测试工具")
print("该工具仅供测试使用！")

try:
    import unittest

except ModuleNotFoundError:
    print("加载 unittest 模块失败！")
    input()
    exit()

from 初心不变运营模拟系统 import *

class 测试(unittest.TestCase):
    def setUp(self):
        from random import random,randint,choice
        from time import time,sleep
        from pickle import dump,load
        import logging
    def test_测试日志初始化(self):
        初始化运行日志()
        初始化事件日志()
    def test_测试数值初始化(self):
        初始化数值()
        self.assertEqual(随机数,0)
        self.assertEqual(运行天数,0)
        self.assertEqual(警告次数,0)
        self.assertEqual(存档文件状态码,0)
    def test_测试部门类(self):
        初始化类()
        群组运营部 = 群组运营("测试")
        人力资源部 = 人力资源("测试")
        文案宣传部 = 文案宣传("测试")
        舆情分析部 = 舆情分析("测试")
        self.assertEqual(群组运营部.name,"测试")
        self.assertEqual(人力资源部.name,"测试")
        self.assertEqual(文案宣传部.name,"测试")
        self.assertEqual(舆情分析部.name,"测试")
        self.assertEqual(群组运营部.人数,0)
        self.assertEqual(人力资源部.人数,0)
        self.assertEqual(文案宣传部.人数,0)
        self.assertEqual(舆情分析部.人数,0)
        self.assertEqual(群组运营部.部门人员列表,[])
        self.assertEqual(人力资源部.部门人员列表,[])
        self.assertEqual(文案宣传部.部门人员列表,[])
        self.assertEqual(舆情分析部.部门人员列表,[])
        self.assertEqual(群组运营部.能力,0)
        self.assertEqual(人力资源部.能力,0)
        self.assertEqual(文案宣传部.能力,0)
        self.assertEqual(舆情分析部.能力,0)
        self.assertEqual(文案宣传部.文案列表,[])
        self.assertEqual(文案宣传部.当前进行文案,None)
        self.assertEqual(文案宣传部.总文案数量,0)
        self.assertEqual(文案宣传部.当前文案进度,None)
        self.assertEqual(人力资源部.当前群人数,15)
        self.assertEqual(人力资源部.当前群人数,15)
        self.assertEqual(舆情分析部.当前舆情事件编号,None)
        self.assertEqual(舆情分析部.舆情事件等级,None)
        self.assertEqual(舆情分析部.舆情事件产生者,None)
        self.assertEqual(舆情分析部.舆情事件指数,None)
        self.assertEqual(舆情分析部.舆情事件编号列表,[])
    def test_测试用户类(self):
        初始化类()
        for i in range(500):
            exec("用户"+str(i)+"=用户("+str(i)+")")
        for i in range(30):
            exec("用户"+str(i)+".在群中=True")
        self.assertEqual(用户100.所属部门,None)
        self.assertEqual(用户200.编号,200)
    def test_压力测试(self):
        初始化类()
        for i in range(randint(20000,50000)):
            exec("用户"+str(i)+"=用户("+str(i)+")")
    def test_保存存档测试(self):
        存档文件状态码 = 2
        随机数 = randint(1,100)
        运行天数 = randint(1,65536)
        警告次数 = randint(1,5)
        群组运营部 = 群组运营(测试)
        人力资源部 = 人力资源(测试)
        文案宣传部 = 文案宣传(测试)
        舆情分析部 = 舆情分析(测试)
        保存存档()
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
