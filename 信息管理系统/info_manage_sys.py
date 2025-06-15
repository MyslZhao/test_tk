import tkinter as tk
from tkinter import ttk
import json as js
# -*- coding: unicode -*-
DATA=[]
STATUE=0
PEOPLE={}

with open("./信息管理系统/login.bin","r",encoding="utf-8") as file:
    login_data=file.read()
    cache=js.loads(login_data)
    print(cache)
    #for i in cache:
    #    DATA.append(list())
    DATA=cache
    file.close()

def user_signup(name, password):
    """
    用户注册功能实现
    """
    name_value=name.get()
    password_value=password.get()
    print(name_value, password_value)
    # 注册功能待实现

def user_login(name,password):
    """
    用户登录功能实现
    """
    global STATUE,PEOPLE #!noqa: W0603
    name_value=name.get()
    password_value=password.get()
    #print(name_value,password_value)
    for i in DATA:
        if name_value == i["name"] and password_value == i["password"]:
            print("登录成功")
            if i["root"] == True:
                STATUE = 1
            else:
                STATUE = 2
            PEOPLE = i
            main_win.destroy()
        else:
            print("登录失败")

def signup(old_frame):
    """
    注册界面设计
    """
    old_frame.destroy()
    # login_frame登录框架初始化
    login_frame = tk.Frame(main_frame, height=500, width=500, relief="groove", bd=5, bg="white")
    # 添加标签控件title_label
    title_label = tk.Label(login_frame, text="信息管理系统", font="courior 20 bold", bd=10, bg="white", fg="black")
    title_label.grid(row=0, column=1, rowspan=1,columnspan=3, sticky="w", padx=10, pady=10)
    #添加按钮return_button
    return_button = tk.Button(login_frame, text="返回", bd=10, command=lambda: login(login_frame),relief="flat", bg="white")
    return_button.grid(row=1, column=1, sticky="w", padx=10, pady=20)
    # 添加标签控件name_label和pwd_label
    name_label = tk.Label(login_frame, text="用户名:", font="courior", bd=10, bg="white", fg="black")
    name_label.grid(row=2, column=1, padx=10, pady=20)
    pwd_label = tk.Label(login_frame, text="密码:", font="courior", bd=10, bg="white", fg="black")
    pwd_label.grid(row=3, column=1, padx=10, pady=20)
    # 添加输入控件name
    name = tk.Entry(login_frame, bd=10, font="courior", bg="white")
    name.grid(row=2, column=2, columnspan=2, padx=20, pady=20)
    # 添加输入控件password和submit
    password = tk.Entry(login_frame, bd=10, font="courior", bg="white", show="*")
    password.grid(row=3, column=2, columnspan=2)
    submit = tk.Button(login_frame, command=lambda:user_login(name,password), text="注册", bd=10)
    submit.grid(row=4, column=1, columnspan=3, ipadx=30)
    main_frame.pack(fill=tk.BOTH, expand=True)
    login_frame.pack(expand=True)

def login(old_frame=None):
    """
    登录界面设计
    """
    #判断是否返回自注册页面还是初次加载
    if old_frame is not None:
        old_frame.destroy()
    #login_frame登录框架初始化
    login_frame=tk.Frame(main_frame,height=500,width=500,relief="groove",bd=5,bg="white")
    #添加标签控件title_label,name_label和pwd_label
    title_label=tk.Label(login_frame,text="信息管理系统",font="courior 20 bold",bd=10,bg="white",fg="black")
    title_label.grid(row=0,column=2,columnspan=3,sticky="w",padx=10,pady=20)
    name_label=tk.Label(login_frame,text="用户名:",font="courior",bd=10,bg="white",fg="black")
    name_label.grid(row=1,column=2,sticky="w",padx=10,pady=20)
    pwd_label=tk.Label(login_frame,text="密码:",font="courior",bd=10,bg="white",fg="black")
    pwd_label.grid(row=2,column=2,sticky="w",padx=10,pady=20)
    #添加输入控件name
    name=tk.Entry(login_frame,bd=10,font="courior",bg="white")
    name.grid(row=1,column=3,columnspan=2,sticky="w",padx=20,pady=20)
    #添加输入控件password和submit
    password=tk.Entry(login_frame,bd=10,font="courior",bg="white",show="*")
    password.grid(row=2,column=3,columnspan=2)
    submit=tk.Button(login_frame,command=lambda:user_login(name,password),relief="flat",bg="blue",text="登录",bd=10)
    submit.grid(row=3,column=2,columnspan=3,ipadx=30)
    login_frame.pack(expand=True)
    #添加signup按钮
    signup_button=tk.Button(login_frame,text="没有账号？去注册",bd=10,relief="flat",bg="white",command=lambda:signup(login_frame))
    signup_button.grid(row=4,column=2,columnspan=3,ipadx=30,pady=20)

def user():
    global PEOPLE
    pass

def management():
    """
    后台管理界面设计及功能实现
    """
    global PEOPLE
    def logout():
        pass
    
    management_win=tk.Tk()
    management_win.geometry("500x500+500+250")
    management_win.title("后台管理")
    management_frame=tk.Frame(management_win,height=500,width=500,relief="groove",bd=0,bg="blue")
    management_frame.pack(fill=tk.BOTH,expand=True)
    manager_name=tk.Label(management_frame,text="欢迎，管理员"+PEOPLE["name"],font="courior 20 bold",bd=10,bg="white",fg="black")
    manager_name.pack(fill=tk.X, padx=10, pady=10)
    user_list=ttk.Treeview(management_frame, columns=("name", "password", "root"), show="headings")
    user_list.heading(column="id",test="ID")
    user_list.heading("name", text="用户名")
    user_list.heading("password", text="密码")
    user_list.heading("root", text="管理员")
    user_list.column("id", width=50, anchor="center")
    user_list.column("name", width=150, anchor="center")
    user_list.column("password", width=150, anchor="center")
    user_list.column("root", width=100, anchor="center")
    user_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    # 其他管理功能的实现
    management_win.mainloop()
    pass

#main_win主窗口初始化
main_win=tk.Tk()
main_win.geometry("500x500+500+250")
main_win.title("信息管理系统")
#main_frame主窗口的框架初始化
main_frame=tk.Frame(main_win,height=500,width=500,relief="groove",bd=0,bg="blue")
main_frame.pack(fill=tk.BOTH,expand=True)
login()
main_win.mainloop()
if STATUE == 1:
    del STATUE
    management() 
elif STATUE == 2:
    del STATUE
    user()
else:
    pass