"""
owner:enterusrname@github.com
version:0.02a
cTime:2024-6-3 23:12
ltime:2024-6-4 10:10
"""
import tkinter as tk #导入Tk
w=tk.Tk() #Tk对象"w"
l=tk.Label(w,anchor="nw",bd=4,cursor="cross",text="Hello world!") #Label对象"l"
b=tk.Button(w,command="l.pack()",text="点一下试试") #控制"l"的载入
b.pack() #载入"b"
m.mainloop() #开启窗口
