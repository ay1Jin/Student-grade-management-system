from tkinter import *  
from view import *  #菜单栏对应的各个子页面  
  
class MainPage(object):  
    def __init__(self, master=None):  
        self.root = master #定义内部变量root  
        self.root.geometry('%dx%d' % (350, 500)) #设置窗口大小  
        self.createPage()  
    def createPage(self):  
        self.inputPage = InputFrame(self.root) # 创建不同Frame  
        self.deletePage = DeleteFrame(self.root)
        self.modifyPage = ModifyFrame(self.root)
        self.queryPage = QueryFrame(self.root) 
        self.sortPage = SortFrame(self.root)
        self.analysisPage = AnalysisFrame(self.root)
        self.checkPage = CheckFrame(self.root)
        self.inputPage.pack() #默认显示数据录入界面  
        menubar = Menu(self.root)  
        menubar.add_command(label='增加信息', command = self.inputData)  
        menubar.add_command(label='删除信息', command = self.deleteData)  
        menubar.add_command(label='更改信息', command = self.modifyData)  
        menubar.add_command(label='单科查找', command = self.queryData)  
        menubar.add_command(label='成绩排名', command = self.sortData)
        menubar.add_command(label='成绩分析', command = self.analysisData)
        menubar.add_command(label='查找学生', command = self.checkData)
        self.root['menu'] = menubar  # 设置菜单栏  
    def inputData(self):  
        self.inputPage.pack()  
        self.queryPage.pack_forget()  
        self.deletePage.pack_forget()
        self.modifyPage.pack_forget() 
        self.sortPage.pack_forget()
        self.analysisPage.pack_forget()
        self.checkPage.pack_forget()
    def deleteData(self):  
        self.inputPage.pack_forget()  
        self.queryPage.pack_forget()  
        self.deletePage.pack()  
        self.modifyPage.pack_forget()
        self.sortPage.pack_forget()
        self.analysisPage.pack_forget()
        self.checkPage.pack_forget()
    def modifyData(self):  
        self.inputPage.pack_forget()  
        self.queryPage.pack_forget()  
        self.deletePage.pack_forget()  
        self.modifyPage.pack() 
        self.sortPage.pack_forget()
        self.analysisPage.pack_forget()
        self.checkPage.pack_forget()        
    def queryData(self):  
        self.inputPage.pack_forget()  
        self.queryPage.pack()  
        self.deletePage.pack_forget()  
        self.modifyPage.pack_forget()  
        self.sortPage.pack_forget()
        self.analysisPage.pack_forget()
        self.checkPage.pack_forget()
    def sortData(self):
        self.inputPage.pack_forget()  
        self.queryPage.pack_forget()  
        self.deletePage.pack_forget()  
        self.modifyPage.pack_forget()  
        self.sortPage.pack()
        self.analysisPage.pack_forget()
        self.checkPage.pack_forget()
    def analysisData(self):
        self.inputPage.pack_forget()  
        self.queryPage.pack_forget()  
        self.deletePage.pack_forget()  
        self.modifyPage.pack_forget()  
        self.sortPage.pack_forget()
        self.analysisPage.pack()
        self.checkPage.pack_forget()
    def checkData(self):
        self.inputPage.pack_forget()  
        self.queryPage.pack_forget()  
        self.deletePage.pack_forget()  
        self.modifyPage.pack_forget()  
        self.sortPage.pack_forget()
        self.analysisPage.pack_forget()
        self.checkPage.pack()