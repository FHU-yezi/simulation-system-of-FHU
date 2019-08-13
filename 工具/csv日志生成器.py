print("csv 日志生成器")
print("by 叶子")

from csv import writer
import time

try:
    in_file=open("运行日志.log","r")
    out_file=open("运行日志.csv","w")
    in_data=in_file.readlines()
    out_data=[ ]
    for i in in_data:
        spilted=i.split()
        out_data.append(spilted)
    head=[["该日志由 csv 日志生成器生成","生成时间 ："+time.strftime("%Y-%m-%d %X")],["日期","时间","等级","信息"]]
    log_writer=writer(out_file)
    log_writer.writerows(head)
    log_writer.writerows(out_data)
except FileNotFoundError:
    print("未找到运行日志文件")
else:
    print("运行日志表格生成成功！")
finally:
    in_file.close()
    out_file.close()
try:
    in_file=open("事件日志.log","r")
    out_file=open("事件日志.csv","w")
    in_data=in_file.readlines()
    out_data=[ ]
    for i in in_data:
        spilted=i.split()
        out_data.append(spilted)
    head=[["该日志由 csv 日志生成器生成","生成时间 ："+time.strftime("%Y-%m-%d %X")],["日期","时间","信息"]]
    log_writer=writer(out_file)
    log_writer.writerows(head)
    log_writer.writerows(out_data)
except FileNotFoundError:
    print("未找到事件日志文件")
else:
    print("事件日志表格生成成功！")
finally:
    in_file.close()
    out_file.close()
