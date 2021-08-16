import random as rd
import tkinter as tk
from tkinter.messagebox import *

root = tk.Tk() #创建窗口
root.title("随机提问")#设置窗口标题
root.geometry("300x200")#设置窗口大小
root.resizable(0,0)#禁止调整窗口大小

#添加文本标签提示输入
tk.Label (root,text="请输入班级：",font=('Arial',10)).pack()



#添加文本框获取人数
inps = tk.StringVar()
tk.Entry(root,textvariable=inps,width=10).pack()

#添加文本标签显示抽取的姓名
var = tk.StringVar()
ops = tk.Label(root,textvariable=var,font=('宋体',30),width=10,height=2).pack()

def start():
    f = open("学生名单.txt","r")
    stu_dict = {}
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n","").split("\t")
        stu_dict.setdefault(line[0],[]).append(line[1]) #在字典中用班级映射学生名单列表
    f.close()    
    nums = inps.get()
    if nums not in stu_dict.keys():
        showwarning('警告','班级错误！')
    class_stu_list = stu_dict[nums]
    jieguo = rd.choice(class_stu_list)
    var.set(jieguo)


#添加提问按钮
tk.Button(root,text="提问",relief="solid",command=start,width=10,height=2).pack()

root.mainloop() #窗口消息时间循环
