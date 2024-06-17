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
