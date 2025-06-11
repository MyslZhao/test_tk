import tkinter as tk
# -*- coding: utf-8 -*-
#version:0.1
DATA={}

with open("./login.json","r",encoding="utf-8") as f:
    login_data=f.read()
    DATA=login_data

def main_window():
    def login():
        name_value=name.get()
        password_value=password.get()
        print(name_value,password_value)
        pass

    #main_win主窗口初始化
    main_win=tk.Tk()
    main_win.geometry("500x500+500+250")
    main_win.title("五子棋")

    #main_frame主窗口的框架初始化
    main_frame=tk.Frame(main_win,height=500,width=500,relief="groove",bd=0,bg="blue")

    #在框架中添加控件name
    name=tk.Entry(main_frame,bd=10,font="courior",bg="white")
    name.grid(row=1,column=2,columnspan=2)
    
    #以及控件password和submit
    password=tk.Entry(main_frame,bd=10,font="courior",bg="white",show="*") 
    password.grid(row=2,column=2,columnspan=2)
    submit=tk.Button(main_frame,command=login,text="登录",bd=10)
    submit.grid(row=3,column=1,columnspan=3)
    main_frame.pack(expand=True)
    main_win.mainloop()

main_window()