#!/usr/bin/python3
import keyword
print(keyword.kwlist)#python 保留字
'''
多行注释
'''

"""
多行注释
"""

'''
python使用缩进来表示代码块
缩进不一致，会导致运行错误
多行语句用\来实现
'''

'''
python有四种数字类型
int
bool
float
complex(复数)：a+bj
    如：3.14j
'''

'''
字符串(String)
python中单引号和双引号使用完全相同。
使用三引号可以指定一个多行字符串。
转义符 '\'
反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
'''

#实例
str="Modolet"
print(str)#输出字符串
print(str[0:-1])#输出第一个字符到倒数第二个的所有字符
print(str[0])#输出字符串的第一个字符
print(str[2:5])#输出从第三个开始到第五个的字符
print(str[2:])#输出第三个开始后的所有字符
print(str * 2)#输出字符串两遍
print(str + '你好')#连接字符串
print('------------------------------------------')
print('Hello\nModolet')#使用转义字符
print(r"Hello\nModolet")#在字符串前面添加一个r，表示原始字符串，不会发生转义

'''
空行
    函数之间或者类的方法之间用空行分隔，表示新的代码段
    类和函数入口之间也用一行空行分割，突出入口的开始
    空行不是python语法的一部分
'''

'''
同一行显示多条语句，语句之间用分号;分割
'''

'''
多个语句构成代码块
    缩进相同的一组语句构成一个代码块，称之为代码组
    if while def 和 class之类的复合语句，首行以关键字开始，以冒号结束，如：
        if expression : 
            suite
    elif expression : 
            suite 
    else : 
            suite
'''

'''
print默认输出换行，如果要实现不换行需要在变量末加上end=""
'''

#实例
x='a'
y='b'
#换行输出
print(x)
print(y)

#不换行输出
print(x,end="")
print(y,end="")

'''
import与from...import
    在python中用import或者from...import来导入相应的模块
    将整个模块（somemodule）导入，格式为：
        import somemodule
    从某个模块中导入某个函数，格式为：
        from somemodule import somefunction
    从某个模块中导入多个函数，格式为：
        from somemodule import firstfunc, secondfunc ,thirdfunc
    将某个模块中的全部函数导入，格式为：
        from somemodule import *
'''

