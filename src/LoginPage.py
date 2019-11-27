from tkinter import *
from tkinter.messagebox import *
from MainPage import *
import tkinter.font as tkFont

class LoginPage(object):
    def __init__(self, master=None):
        self.root = master #定义内部变量root
        self.root.geometry('%dx%d' % (304, 400)) #设置窗口大小  
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()
    def createPage(self):
        a = '#AFEEEE'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)
        self.page = Frame(self.root,bg='#E0FFFF') #创建Frame
        self.page.pack(expand=YES,fill=BOTH)
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text = '账户: ',font=ft,bg=a).grid(row=1, stick=N, pady=5)
        Entry(self.page, textvariable=self.username,width=25,).grid(row=1, column=1, stick=E)
        Label(self.page, text = '密码: ',font=ft,bg=a).grid(row=2, stick=N, pady=10)
        Entry(self.page, textvariable=self.password, show='*',width=25).grid(row=2, column=1, stick=E)
        Button(self.page, text='登陆', command=self.loginCheck,font=ft,bg=a).grid(row=3, column=0, pady=5)
        Button(self.page, text='注册', command=self.register,font=ft,bg=a).grid(row=3, column=1, pady=5)
        Button(self.page, text='退出', command=self.page.quit,font=ft,bg=a).grid(row=3, column=2, pady=5)
    def loginCheck(self):
        name = self.username.get()
        password = self.password.get()
        if self.isLegalUser(name,password):
            self.page.destroy()
            MainPage(self.root)
        else:
            showinfo(title='错误', message='账号或密码错误！')
    def isLegal(self,string):
        alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','J','L','U','Z','H']
        for i in string:
            if i in alp:
                pass
            else:
                return False
        return True
    def isLegalUser(self,name,password):
        f = open('Password.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<2:
                break
            if info[0].strip()==name and  info[1].strip()==password :
                 f.close()
                 return True
        return False
    def register(self):
        name = self.username.get()
        password = self.password.get()
        if len(name)==0 or len(password)==0:
            showinfo(title='错误', message='账号密码不能为空')
            return
        for i in password:
            if i is ',' or i is ' ':
                showinfo(title='错误', message='密码不能含有非法字符')
                return
        if self.isLegal(name):
            pass
        else:
            showinfo(title='错误', message='账号不能含有非法字符')
            return
        f = open('Password.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<2:
                break
            if info[0].strip()==name:
                 messagebox.showinfo(title='结果', message ="已存在该用户信息！")
                 f.close()
                 return
        f.close()
        f = open('Password.csv','a',encoding='utf-8')
        f.write('{},{}\n'.format(name,password))
        f.close()
        messagebox.showinfo(title='提示', message ="注册成功")
