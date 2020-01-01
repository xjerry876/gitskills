import os
"""
f=open("C:/Users/admin/Desktop/11.txt","w") 
f.write("骨灰扬诺夫")

print ("文件名: ", f.name)
print ("是否已关闭 : ", f.closed)
print ("访问模式 : ", f.mode)
print("文件内容是:",f.readline())

f.close()
"""
"""
f=open("C:/Users/admin/Desktop/111.txt","r+")
f.write("三天之内把你骨灰给你扬咯")
print(f.readline())

h=1.75
w=80.5
bmi=w/(h*h)
if(bmi<18.5):
    print("过轻")
elif(bmi>=18.5 and bmi<=25):
    print("正常")
elif(bmi>25 and bmi<=28):
    print("过重")
elif(bmi>28 and bmi<=32):
    print("肥胖")
else:
    print("严重肥胖")

"""
"""
def pro(x,y,*a,**k):
    print(x,y)
    print(x,y,a)
    print(x,y,a)
    print(x,y,a,k)
    print(x,y,a,k)

pro(4,5)
pro(4,5,6)
pro(4,5,6,7)
pro(4,5,6,7,d=8)
pro(4,5,6,7,d=8,f=9)
"""
"""
def trim(s):
    a=" hello "
    s=a[1:-1]
    return s

if trim('hello  ') != 'hello':
    print('测试失败!aa' )
elif trim('  hello') != 'hello':
    print('测试失败!bb')
elif trim('  hello  ') != 'hello':
    print('测试失败!cc')
elif trim('') != '':
    print('测试失败!ee')
elif trim('    ') != '':
    print('测试失败!ff')
else:
    print('测试成功!gg')
"""
"""
def find(L):
    if len(L)==0:
       return(None,None) 
    for i in L:
        lmax=max(i,len(L))
        lmin=min(i,len(L))
        
        print(lmax)
        
    return(lmax,lmin)

if find([]) != (None, None):
    print('测试失败! a1',)
elif find([7, 1]) != (1, 7):
    print('测试失败! a2')
elif find([7]) != (7, 7):
    print('测试失败! a3')
elif find([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败! a4')
else:
    print('测试成功! a5')
"""
"""
g = (x * x for x in range(10))
for n in g:
    print(n)
"""
"""
def normalize(name):
    return name.capitalize()

L1=list(map(normalize,['adam', 'LISA', 'barT']))
print(L1)
"""

"""
from functools import reduce
def prod(x,y):
    return x*y

L2=[3,5,7,9]
L1=reduce(lambda x,y:x*y,L2)
print(L1)
"""


"""
def by_name(s):
    return sorted(s)

L = ["Bob",  "Adam", "Bart","Lisa"]
L1=list(map(by_name,L))
print(L1)
"""

"""
def by_name(s):
    return s[0]

def by_score(s):
    return s[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L1=sorted(L,key=by_name)
L2=sorted(L,key=by_score)
print(L1,L2)
"""
"""
def createCounter():
    s=[0]
    def counter():
        s[0]=s[0]+1
        return s[0]
    return counter


counterA =createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB =createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

"""
"""
L=list(filter(lambda n:n%2==1,range(1,20)))
print(L)
"""
"""
import functools, time

def log(func):
    def wrap(*args,**kw):
        print("call %s():" % log.__name__)
        return func(*args,**kw)
    return wrap

@log

def now():
    n="2019-12-28"
    print(n)

f=now()
print(f)
"""
"""
class Student():
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender

    def get_gender(self):
        return self.__gender
    
    def set_gender(self,gender):
        self.__gender=gender

bart=Student("name","gender")

setattr(bart,"age",28)
t1=getattr(bart,"age")
print(t1)

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

"""
"""
class Student():
    count=0 

    def __init__(self,name):
        self.name=name
        Student.count +=1

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

"""
"""
class  Screen():

    @property
    def set_score(self,width,height):
        self.width=width
        self.height=height

    @property
    def get_score(self):
        return self.width
        return self.height

    @property
    def resolution(self):
        return self.width*self.height


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

"""
"""
from enum import Enum,unique

@unique
class Gender(Enum):
    Male=0
    Female=1
    A=3
    B=4
    C=5

class Student():
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    
    def __str__(self):
        return "Student object (name:%s)"% self.name

bart=Student("Bart",Gender.Male)
print(bart)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

"""
"""
from functools import reduce

def str2num(s):
    try:
        return int(s)
    except :
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
"""
"""
from io import StringIO

f=StringIO("hello!,hi!,goodbye")
for i in f:
    i=f.readline()
    if i=="":
        break
    print(i.strip())

#print(f.getvalue())
"""
"""
#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
import os 

def main():
    str=input("输入查询的字符串:")
    path_name=input("输入查询的路径(默认为工作路径):")
    if path_name=="":
        path_name="."
    minus=len(path_name)

    def list_file(str,path):
        list_all=os.listdir(path)                                                    #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
        for name_f in list_all:
            path_c=os.path.join(path,name_f)                                         #os.path.join:把目录和文件名合成一个路径
            if os.path.isfile(path_c) and str in os.path.splitext(name_f)[0]:        #os.path.isfile():判断路径是否为文件   os.path.splitext():分割路径，返回路径名和文件扩展名的元组
                print(path_c[minus])                                                 #把路径前缀去掉
            elif os.path.isdir(path_c):                                              #os.path.isdir():判断路径是否为目录
                list_file(str,path_c)

    list_file(str,path_name)

main()
"""
"""
import pickle
import os
import json
class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)
"""

str=input("请输入")
print("是是是",str)