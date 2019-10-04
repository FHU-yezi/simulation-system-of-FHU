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
    def test_测试部门类实例化(self):
        群组运营部 = 群组运营()
        人力资源部 = 人力资源()
        文案宣传部 = 文案宣传()
        舆情分析部 = 舆情分析()
    def test_测试用户类实例化(self):
        for i in range(500):
            exec("用户"+str(i)+"=用户("+str(i)+")")
        for i in range(30):
            exec("用户"+str(i)+".在群中=True")
    def test_压力测试(self):
        for i in range(randint(20000,50000)):
            exec("用户"+str(i)+"=用户("+str(i)+")")
    def test_保存存档测试(self):
        存档文件状态码 = 2
        随机数 = randint(1,100)
        运行天数 = randint(1,65536)
        警告次数 = randint(1,5)
        群组运营部 = 群组运营()
        人力资源部 = 人力资源()
        文案宣传部 = 文案宣传()
        舆情分析部 = 舆情分析()
        保存存档()
    def tearDown(self):
        import os
        try:
            os.remove("存档文件.sav")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    unittest.main()