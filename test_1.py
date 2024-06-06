"""
owner:enterusrname@github.com
version:0.03g
cTime:2024-6-3 23:12
ltime:2024-6-6 10:19
"""
import tkinter as tk
w=tk.Tk()
fa=tk.Frame(w)
fa.pack()
e=tk.Entry(fa,show="*",bd=10,bg="yellow")
e.pack()
def job():
    l.pack()
    w.title(e.get())
    return 0

l=tk.Label(fa,anchor="nw",bd=4,cursor="cross",text="Hello world!")
tk.Button(w,command=job,text="点一下试试").pack()
w.mainloop()
