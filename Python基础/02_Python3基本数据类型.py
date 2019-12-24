#!/usr/bin/python3
print('Python3基本数据类型')

'''
编码
    默认情况下，python3源码文件以UTF-8编码，所有字符串都是Unicode字符集。也可手动指定编码
        # -*- coding: cp-1252 -*-
'''

'''
python中的变量不需要声明。每个变量在使用前必须赋值，变量赋值后该变量才会被创建
在python中，变量就是变量，它没有类型，我们所说的类型值得是变量所指的内存中对象的类型
等号用来给变量赋值
'''
#实例
counter = 100       #整形变量
miles   = 1000.0    #浮点型变量
name    = "modolet" #字符串

print(counter)
print(miles)
print(name)

del counter, miles, name
'''
多个变量赋值
python允许同时为多个变量赋值
'''
#实例
a = b = c = 1
e, f, g = 1 ,2 ,"modolet"

'''
python3中有六个标准的数据类型
    Number(数字)
    String(字符串)
    List(列表)
    Tuple(元组)
    Set(集合)
    Dictionary(字典)
    其中：
        不可变数据：Number String Tuple
        可变数据  ：List Dictionary Set
    
    内置的type函数可以用来查询变量类型
    也可以用isinstance来判断
'''
#实例
print(type(e),type(f),type(g))
print(isinstance(e,int));

'''
使用del语句删除单个或多个对象
'''
#实例
del a, b, c, e, f, g

'''
数值运算
/   除法，得到一个浮点数
//  除法，得到一个整数
**  乘方，和c语言的^相同
注意：
    在混合计算时，Python会把整型转换为浮点数
'''

'''
String(字符串)
    python中的字符串用单引号'或者双引号"括起来，同时使用反斜杆\转义特殊字符
    字符串的截取的语法格式如下
        变量[头下标:尾下表]
        索引值从0为开始值，-1为末尾的开始位置
        加号+时字符串的连接符，星号*表示赋值当前字符串，紧跟的数字为复制的次数
    python使用反斜杠\转义特殊字符，如果不想发生转义，可以在字符串前面添加一个r
    注意：
        python中的字符串不能被改变
        python没有单独的字符类型，一个字符就是长度为1的字符串
'''
#实例
str = 'Modolet'
print(str)          # 输出字符串
print(str[0:-1])    # 输出第一个到倒数第二个的所有字符
print(str[0])       # 输出字符串第一个字符
print(str[2:5])     # 输出从第三个开始到第五个的字符
print(str[2:])      # 输出从第三个开始的后的所有字符
print(str * 2)      # 输出字符串两次
print(str + "TEST") # 连接字符串

del str
'''
List(列表)
    List(列表)是python中使用最频繁的数据类型
    列表可以完成大多数集合类的数据结构实现
    列表中的元素的类型可以不相同
    列表是写在[]之间，用逗号分隔开的元素列表
    列表的截取规则和string相同
    
    与字符串不一样的是，列表中的元素是可以改变的
    
    List内置了很多方法，如append() pop()等等
    
    python列表截取可以接收第三个参数，参数作用是截取的步长
    如果第三个参数为复数表示逆向读取，以下实例用于翻转字符串
    
    
'''
#实例
list = ['abcd', 666, 3.14, 'modolet', 23.45]
list2 = [456,'asd']
print(list)         #输出完整列表
print(list[0])      #输出列表第一个元素
print(list[1:3])    #从第二个元素开始输出到第三个元素
print(list[2:])     #输出从第三个元素开始的所有元素
print(list2 * 2)    #输出两次列表
print(list + list2) #连接列表

list[2:4] = []      #将对应的元素设为[]
print(list)

del list, list2
#翻转字符串实例
def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")
    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]
    # 重新组合字符串
    output = ' '.join(inputWords)
    return output
input = 'I like Modolet'
rw = reverseWords(input)
print(rw)
del input, rw
'''
Tuple(元组)
    元组与列表相似，不同之处在于元组的元素不能修改。元组卸载小括号里，元素之间用逗号隔开
    元组截取规则与字符串相同
    可以把字符串看作一种特殊的元组
    虽然元组tuple的元素不可改变，但它可以包含可变的对象，比如list列表
    构造包含0个元素或者1个元素的元组比较特殊，所以有一些特殊的语法规则
'''
#实例
tuple   = ('asdf', 666, 3.14, 'modolet', 123)
tuple2  = (999,'xxx')
print(tuple)            #输出完整元组
print(tuple[0])         #输出元组的第一个元素
print(tuple[1:3])       #输出从第二个元素开始到第三个元素
print(tuple[2:])        #输出从第三个元素开始的所有元素
print(tuple * 2)        #输出两次元组
print(tuple + tuple2)   #连接元组
#tuple[0]=11    修改元组元素是非法的
tup1 = ()               #空元组
tup2 = (66,)            #一个元素，需要在元素后添加逗号

del tuple, tuple2, tup1, tup2
'''
Set(集合)
    集合(Set)是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员
    基本功能是进行成员关系测试和删除重复元素
    可以使用大括号{}或者set()函数创建集合
    创建格式：
        parame = {value01,value02,...}
        或者
        set(value)
    注意：
        创建一个空集合必须用set()而不是{}，因为{}是用来创建一个空字典
'''
#实例
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)#输出集合，重复的元素被自动去掉
#成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
#set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)        #a和b的差集
print(a | b)        #a和b的并集
print(a & b)        #a和b的交集
print(a ^ b)        #a和b中不同时存在的元素

'''
Dictionary(字典)
    字典(dictionary)是python中另一个非常有用的内置数据类型
    列表是有序的对象集合，字典是无序的对象集合。两者的区别在于：
        字典当中的元素是通过键来存取的，而不是通过偏移存取
    字典是一种映射类型。字典用{}标识，它是一个无需的 键(key):值(value) 的集合
    键(key)必须使用不可变类型
    在同一个字典中，键(key)必须是唯一的。
    构造函数dict()可以直接从键值对序列中构造字典，如实例2
    字典也有一些内置的函数，例如clear() keys() values()等
    注意：
        字典是一种映射类型，它的元素是键值对
        字典的关键字必须为不可变类型，且不能重复
        创建空字典使用{}
'''
#实例
dict = {}
dict['one'] = '1,Modolet'
dict[2]     = '2,杨越程'

tinydict = {'name':'Modolet', 'code':1, 'site':'www.modolet.com'}

print(dict['one'])          #输出键为'one'的值
print(dict[2])              #输出键为2的值
print(tinydict)             #输出完整的字典
print(tinydict.keys())      #输出所有键
print(tinydict.values())    #输出所有值

del dict, tinydict

#实例2
d = dict([('Modolet', 1), ('Google', 2), ('Microsoft', 3)])
print(d)
#或如
d2 = {x: x**2 for x in (2, 4, 6)}
print(d2)

'''
Python数据类型转换
    数据类型的转换，只需要将数据类型作为函数名即可
    这些函数返回一个新的对象，表示转换的值
'''










