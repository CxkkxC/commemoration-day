# -*- coding:utf-8 -*-
import sqlite3

def thing_opendb():
    conn = sqlite3.connect("ann_date.db")
    cur = conn.execute("""create table if not exists things_info(date varchar(10),year_date char(30),info varchar(256),url varchar(256))""")
    return cur,conn

#  往学生数据库中添加内容
def thing_insertData(date,year_date,info,url):
        hel = thing_opendb()
        hel[1].execute("insert into things_info(date,year_date,info,url)values (?,?,?,?)",(date,year_date,info,url))
        hel[1].commit()
        hel[1].close()
        
#   删除学生数据库中的全部内容
def thing_delalldb():
        hel = thing_opendb()              # 返回游标conn
        hel[1].execute("delete from things_info")
        print("删库跑路Cxk我最帅")
        hel[1].commit()
        hel[1].close()
        
#查询学生个人信息
def thing_showdb(date):
        hel = thing_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from things_info where date='%s'"%date)
        res = cur.fetchall()
        return res
        cur.close()

# 打开学生数据库
def user_opendb():
    conn = sqlite3.connect("ann_date.db")
    cur = conn.execute("""create table if not exists ann_info(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,title varchar(128),start_time char(128),info varchar(256),add_time varchar(128))""")
    return cur,conn
    
#查询所有列名
def user_lie_name():
    hel = user_opendb()
    cur = hel[1].cursor()
    cur.execute("select * from ann_info")
    col_name_list = [tuple[0] for tuple in cur.description]  
    return col_name_list
    cur.close()

#查询学生全部信息
def user_slectTable():
        hel = user_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from ann_info")
        res = cur.fetchall()
        #for line in res:
                #for h in line:
                        #print(h),
                #print(line)
        return res
        cur.close()
        
#  往学生数据库中添加内容
def user_insertData(title,start_time,info,add_time):
        hel = user_opendb()
        hel[1].execute("insert into ann_info(title,start_time,info,add_time)values (?,?,?,?)",(title,start_time,info,add_time))
        hel[1].commit()
        hel[1].close()
        
#查询学生个人信息
def user_showdb(title):
        hel = user_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from ann_info where title='%s'"%title)
        res = cur.fetchone()
        return res
        cur.close()
        
    
#   删除学生数据库中的全部内容
def user_delalldb():
        hel = user_opendb()              # 返回游标conn
        hel[1].execute("delete from ann_info")
        print("删库跑路Cxk我最帅")
        hel[1].commit()
        hel[1].close()
        
#   删除学生数据库中的指定内容
def user_deldb(title):
        hel = user_opendb()              # 返回游标conn
        hel[1].execute("delete from ann_info where title='%s'"%title)
        print("已删除标题为 %s 纪念日" %title)
        hel[1].commit()
        hel[1].close()
        
#  修改学生数据库的内容
def user_alter(title,start_time,info,add_time):
        hel = user_opendb()
        hel[1].execute("update ann_info set start_time=?, info= ?,add_time=? where title="+title,(start_time,info,add_time))
        hel[1].commit()
        hel[1].close()
        
        
#查询学生个人信息
def user_titledb():
        hel = user_opendb()
        cur = hel[1].cursor()
        cur.execute("select title from ann_info")
        res = cur.fetchall()
        return res
        cur.close()