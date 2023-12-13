#user input to db and file handling
import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd="root")
cur=myconn.cursor()
cur.execute("show databases")
for x in cur:
    print(x)
    
myconn=mysql.connector.connect(host="localhost",user="root",passwd="root")
cur=myconn.cursor()
cur.execute("create database shull")
cur.execute("show databases")
for x in cur:
    print(x)   
    
myconn=mysql.connector.connect(host="localhost",user="root",passwd="root",database="shull")
cur=myconn.cursor()
cur.execute("create table Info(registerno int not null auto_increment primary key,name varchar(50),course varchar(20),mobileno varchar(13))")
cur.execute("show tables")
for x in cur:
    print(x)
    
file=open("D:\\Project\\Python\\shull.txt","w")
print(file.write("Reg.No \t\t Name \t\t Course \t Mobileno \n"))
file.close()

file=open("D:\\Project\\Python\\shull.txt","a")
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "root",database = "shull")
cur = myconn.cursor()
for i in range(5):
    registerno=input("Enter your Reg.No:  ")
    name=input("Enter your Name:   ")
    course=input("Enter your Course:   ")
    mobileno=input("Enter your MobileNo:   ")
    print(file.write(registerno))
    print(file.write("\t\t"))
    print(file.write(name))
    print(file.write("\t\t"))
    print(file.write(course))
    print(file.write("\t\t"))
    print(file.write(mobileno))
    print(file.write("\n"))
    cur.execute("insert into Info values(%s,%s,%s,%s)",(registerno,name,course,mobileno))
myconn.commit()
myconn.close()
file.close()

file=open("D:\\Project\\Python\\shull.txt","a")
myconn=mysql.connector.connect(host="localhost",user="root",passwd="root",database="shull")
cur=myconn.cursor()
cur.execute("alter table Info add qualification varchar(13)");
for x in cur:
    print(x)
file.close()

file=open("D:\\Project\\Python\\shull.txt","a")
myconn=mysql.connector.connect(host="localhost",user="root",passwd="root",database="shull")
cur=myconn.cursor()
cur.execute("update Info set qualification='BCA' where registerno=101");
myconn.commit()
for x in cur:
    print(x)
file.close()

file=open("D:\\Project\\Python\\shull.txt","a")
myconn=mysql.connector.connect(host="localhost",user="root",passwd="root",database="shull")
cur=myconn.cursor()
cur.execute("delete from Info where registerno=105");
myconn.commit()
for x in cur:
    print(x)
file.close()