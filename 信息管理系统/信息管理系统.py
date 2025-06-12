import tkinter as tk
# -*- coding: utf-8 -*-
#version:0.2
DATA={}

with open("./信息管理系统/login.json","r",encoding="utf-8") as f:
    login_data=f.read()
    DATA=login_data

def main_window():
    def user_login():
        name_value=name.get()
        password_value=password.get()
        print(name_value,password_value)
        pass

    #main_win主窗口初始化
    main_win=tk.Tk()
    main_win.geometry("500x500+500+250")
    main_win.title("信息管理系统")
    #main_frame主窗口的框架初始化
    main_frame=tk.Frame(main_win,height=500,width=500,relief="groove",bd=0,bg="blue")
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
    submit=tk.Button(login_frame,command=user_login,text="登录",bd=10)
    submit.grid(row=3,column=2,columnspan=3,ipadx=30)
    main_frame.pack(fill=tk.BOTH,expand=True)
    login_frame.pack(expand=True)
    main_win.mainloop()

main_window()