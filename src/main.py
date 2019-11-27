import tkinter as tk
from tkinter import *

from LoginPage import *

root = tk.Tk()
root.title('JLUZH学生管理系统')
photo = tk.PhotoImage(file="jluzh.png")
label_img = tk.Label(root,image=photo,bg='#E0FFFF')
label_img.pack(expand=YES,fill=BOTH)
LoginPage(root)
root.mainloop()
