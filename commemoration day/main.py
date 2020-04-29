
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2020/02/27 12:21
# # @Author  : Cxk
# # @File    : main.py

import os
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk # 导入ttk模块，因为下拉菜单控件在ttk中
from datetime import datetime
import threading
import webbrowser
from Ann_date_sql import *
from year_today import *
import time
from random import randint

# from error import save_error
class Addpage(object):
    def __init__(self, master=None):
        self.root = master#master: 父容器。
        self.createPage()
        self.year=''
        self.month=''
        self.day=''

    
    def createPage(self):
        """
        获得输入框内容进行保存
        进行容错处理，对于未输入的标题与日期提示用户进行更改
        """
        def save():
            titles=self.titles.get()
            if self.year=='' or self.month=='' or self.day=='' or titles=='':
                showinfo(title='错误', message='标题或者日期不能为空！')
                
            else:
                date=self.year+'-'+self.month+'-'+self.day
                date=str(datetime.strptime(date,"%Y-%m-%d")).split(' ')[0]#将字符串改为时间类型

                info=text.get('0.0', END)
                now_time=str(datetime.strptime(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"),"%Y-%m-%d-%H-%M-%S"))

                user_insertData(titles,date,info,now_time)

                showinfo(title='提示', message='纪念日保存成功，请重启软件生效！')
                self.page.destroy()
                self.root.destroy()
        self.page = Toplevel(self.root)
        self.page.title('添加纪念日') 
        self.titles = StringVar()
        winWidth = 300
        winHeight = 350
        screenWidth = self.page.winfo_screenwidth()
        screenHeight = self.page.winfo_screenheight()

        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗口初始位置在屏幕居中
        self.page.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x-351, y))
        # 设置窗口图标
        # root.iconbitmap("./image/icon.ico")
        # 设置窗口宽高固定
        self.page.resizable(0, 0)
        
        Label(self.page,font=("微软雅黑", 12),text="标题").place(x=132,y=0)
        Entry(self.page,textvariable=self.titles,width=10,bd=5).place(x=108,y=25)
        Label(self.page,font=("微软雅黑", 12),text="开始时间").place(x=120,y=55)
    
        # 创建下拉菜单
        cmb = ttk.Combobox(self.page,width=11,foreground='blue',background='blue')
        cmb.place(x=0,y=85)
        # 设置下拉菜单中的值
        cmb['value'] = ('点击选择年份...', '1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', 
                        '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917',
                        '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927',
                        '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937',
                        '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947',
                        '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957',
                        '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', 
                        '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', 
                        '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
                        '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997',
                        '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', 
                        '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', 
                        '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', 
                        '2028', '2029')
        # 设置默认值，即默认下拉框中的内容
        cmb.current(0)
        # 默认值中的内容为索引，从0开始
        # 执行函数
        def func(event):
            self.year=cmb.get()
        cmb.bind("<<ComboboxSelected>>",func)
        
        # 创建下拉菜单
        cmb1 = ttk.Combobox(self.page,width=11,foreground='blue',background='blue')
        cmb1.place(x=100,y=85)
        # 设置下拉菜单中的值
        cmb1['value'] = ('点击选择月份...', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
        # 设置默认值，即默认下拉框中的内容
        cmb1.current(0)
        # 默认值中的内容为索引，从0开始
        # 执行函数
        def func1(event):
            self.month=cmb1.get()
        cmb1.bind("<<ComboboxSelected>>",func1)
        
        # 创建下拉菜单
        cmb2 = ttk.Combobox(self.page,width=11,foreground='blue',background='blue')
        cmb2.place(x=200,y=85)
        # 设置下拉菜单中的值
        cmb2['value'] = ('点击选择日期...', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                         '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
        # 设置默认值，即默认下拉框中的内容
        cmb2.current(0)
        # 默认值中的内容为索引，从0开始
        # 执行函数
        def func2(event):
            self.day=cmb2.get()
        cmb2.bind("<<ComboboxSelected>>",func2)
        
        Label(self.page,font=("微软雅黑", 12),text="内容详情").place(x=120,y=110)
        text = Text(self.page,width=30, height=12)
        text.place(x=45,y=140)
        Button(self.page,text='保存', bd =5,width=10,command=save).place(x=110,y=310)
        

class Infopage(object):
    def __init__(self, master=None):
        self.root = master#master: 父容器。
        self.createPage()
        
    def createPage(self):
        def del_ann(x):
            user_deldb(x)
            showinfo(title='提示', message='该纪念日已删除！请重启软件生效！')
            self.page.destroy()
            self.root.destroy()
        global titless
        if titless=='暂无':
            showinfo(title='错误', message='暂无该纪念日！')
        else:
            self.page = Toplevel(self.root)
            self.page.title('纪念日详情') 
            winWidth = 400
            winHeight = 400
            screenWidth = self.page.winfo_screenwidth()
            screenHeight = self.page.winfo_screenheight()

            x = int((screenWidth - winWidth) / 2)
            y = int((screenHeight - winHeight) / 2)
            # 设置窗口初始位置在屏幕居中
            self.page.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x+401, y))
            # 设置窗口图标
            # root.iconbitmap("./image/icon.ico")
            # 设置窗口宽高固定
            self.page.resizable(0, 0)
            
            #根据标题查询数据库返回数据，获取标题，开始时间，内容。
            all_title=list(user_showdb(titless))
            title=all_title[1]
            start_day=all_title[2]
            #获取当前时间
            now_day=str(datetime.datetime.now().date())
            #获得当前时间减去纪念日的开始时间的相差天数
            date=str(datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d'),"%Y-%m-%d")-datetime.datetime.strptime(start_day,"%Y-%m-%d")).split(',')[0]
            info=all_title[3]
            
            j=0
            infos=''
            #由于内容太长会超出窗口显示不美观，我们对内容进行处理，每10个字符进行换行
            for i in info:
                if j<=10:
                    infos+=i
                    j+=1
                else:
                    infos+=i+'\n'
                    j=0

            Label(self.page,font=("微软雅黑", 25),text=title).pack()

            Label(self.page,font=("微软雅黑", 10),text=start_day+"---"+now_day,fg = "red").pack()
            Label(self.page,font=("微软雅黑", 20),text=date,fg = "red").pack()

            Label(self.page,font=("微软雅黑", 15),text=infos).pack()
            
            Button(self.page,text='删除该纪念日', bd =5,width=10,command=lambda :del_ann(title)).pack(anchor=N)
            
            #优先查找数据库看看有没有
            #没有就去爬取
            a=thing_showdb(now_day[5:])
            if a==[]:
                year_today_main(now_day[5:])
                time.sleep(1)
                a=thing_showdb(now_day[5:])
                
            year_date=a[randint(0,len(a)-1)][1]
            info=a[randint(0,len(a))][2]
            url=a[randint(0,len(a))][3]
            j=0
            urls=''
            infos=''
            for i in info:
                if j<=10:
                    infos+=i
                    j+=1
                else:
                    infos+=i+'\n'
                    j=0
            j=0
            for i in url:
                if j<=50:
                    urls+=i
                    j+=1
                else:
                    urls+=i+'\n'
                    j=0
            def open_url(event):
                webbrowser.open(url, new=0)
            Label(self.page,font=("微软雅黑", 10),text='历史上的今天\n'+year_date).pack()
            Label(self.page,font=("微软雅黑", 15),text=infos,fg = "red").pack()
            link=Label(self.page,font=("微软雅黑", 10),text=urls,fg = "blue")
            link.pack()
            link.bind("<Button-1>", open_url)
        
class Rootpage(object):
    def __init__(self, master=None):
        self.root = master
        winWidth = 400
        winHeight = 400
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗口初始位置在屏幕居中
        self.root.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        # 设置窗口图标
        # root.iconbitmap("./image/icon.ico")
        # 设置窗口宽高固定
        self.root.resizable(0, 0)
        self.createPage()

    
    def createPage(self):
        def fun():
            Addpage(self.root)
        def fun2(x):
            global titless
            titless=x
            Infopage(self.root)
            
        self.author_page = Frame(self.root) 
        self.author_page.pack()
        
        def open_url(event):
            webbrowser.open("https://me.csdn.net/Cxk___", new=0)
            
        Label(self.author_page,font=("微软雅黑", 12),text="点击联系作者@Cxk").pack()
        link=Label(self.author_page,font=("微软雅黑", 12),fg='blue',text="CSDN博客@半盏清茶℡")
        link.pack()
        link.bind("<Button-1>", open_url)
        Button(root,text='+', bd =5,width=10,command=fun).place(x=160,y=55)
        
        #查询数据库所有的内容获得返回，由于我们的界面是要最新的4个纪念日，所以对于小于4个纪念日我们要进行处理
        #至于获得前4个最新的内容我们进行从后往前进行切片处理[-4:],代表从后往前切4个
        all_ann=user_slectTable()
        if all_ann==[]:
            Button(root,text='暂无纪念日信息', bd =5,width=20,height=5,command="#").place(x=130,y=150)
        else:
            if len(all_ann)==1:
                Button(root,text="%s\n%s\n%s\n%s"%(all_ann[0][1],all_ann[0][2],
                                                   all_ann[0][3][0:10:],all_ann[0][4]), bd =5,width=20,height=5,command=lambda :fun2(all_ann[0][1])).place(x=125,y=150)
            if len(all_ann)==2:
                Button(root,text="%s\n%s\n%s\n%s"%(all_ann[1][1],all_ann[1][2],
                                                   all_ann[1][3][0:10:],all_ann[1][4]), bd =5,width=20,height=5,command=lambda :fun2(all_ann[1][1])).place(x=125,y=100)
                Button(root,text="%s\n%s\n%s\n%s"%(all_ann[0][1],all_ann[0][2],
                                                   all_ann[0][3][0:10:],all_ann[0][4]), bd =5,width=20,height=5,command=lambda :fun2(all_ann[0][1])).place(x=125,y=205)
            if len(all_ann)==3:
                all_ann.append(('0','暂无','暂无','暂无','暂无'))
                all_ann=all_ann[-4:]
                j=0
                for i in range(0,2):
                    if i==0:
                        Button(root,text="%s\n%s\n%s\n%s"%(all_ann[3][1],all_ann[3][2],
                                                           all_ann[3][3][0:10:],all_ann[3][4]), bd =5,width=20,height=5,command=lambda :fun2(all_ann[3][1])).place(x=30+j,y=100)
                        Button(root,text="%s\n%s\n%s\n%s"%(all_ann[1][1],all_ann[1][2],all_ann[1][3][0:10:],all_ann[1][4]), bd =5,width=20,height=5,command=lambda :fun2(all_ann[1][1])).place(x=30+j,y=205)
                    else:
                        Button(root,text="%s\n%s\n%s\n%s"%(all_ann[2][1],all_ann[2][2],
                                                           all_ann[2][3][0:10:],all_ann[2][4]), bd =5,width=20,height=5,command=lambda :fun2(all_ann[2][1])).place(x=30+j,y=100)
                        Button(root,text="%s\n%s\n%s\n%s"%(all_ann[0][1],all_ann[0][2],
                                                           all_ann[0][3][0:10:],all_ann[0][4]), bd =5,width=20,height=5,command=lambda :fun2(all_ann[0][1])).place(x=30+j,y=205)
                    j+=180
            else:
                all_ann=all_ann[-4:]
                j=0
                for i in range(0,2):
                    if i==0:
                        Button(root,text="%s\n%s\n%s\n%s"%(all_ann[3][1],all_ann[3][2],
                                                           all_ann[3][3][0:10:],all_ann[3][4]), bd =5,width=20,height=5,command=lambda :fun2(all_ann[3][1])).place(x=30+j,y=100)
                        Button(root,text="%s\n%s\n%s\n%s"%(all_ann[1][1],all_ann[1][2],all_ann[1][3][0:10:],all_ann[1][4]), bd =5,width=20,height=5,command=lambda :fun2(all_ann[1][1])).place(x=30+j,y=205)
                    else:
                        Button(root,text="%s\n%s\n%s\n%s"%(all_ann[2][1],all_ann[2][2],
                                                           all_ann[2][3][0:10:],all_ann[2][4]), bd =5,width=20,height=5,command=lambda :fun2(all_ann[2][1])).place(x=30+j,y=100)
                        Button(root,text="%s\n%s\n%s\n%s"%(all_ann[0][1],all_ann[0][2],
                                                           all_ann[0][3][0:10:],all_ann[0][4]), bd =5,width=20,height=5,command=lambda :fun2(all_ann[0][1])).place(x=30+j,y=205)
                    j+=180
                    
        #获取菜单栏的标题展示返回的是title的列表，我们转换成元组b
        # 创建下拉菜单
        a=user_titledb()
        b=['点击查看更多...']
        for i in a:
            b.append(list(i)[0])
        b=tuple(b)
        cmb = ttk.Combobox(root,width=20,foreground='blue',background='blue')
        cmb.place(x=120,y=330)
        # 设置下拉菜单中的值
        cmb['value'] = b
        # 设置默认值，即默认下拉框中的内容
        cmb.current(0)
        # 默认值中的内容为索引，从0开始
        # 执行函数
        def func(event):
            global titless
            titless=cmb.get()
            Infopage(self.root)
        cmb.bind("<<ComboboxSelected>>",func)
        
if __name__ == "__main__":
    global titless
    root = Tk() 
    root.title('纪念日') 
    Rootpage(root)
    root.mainloop() 
