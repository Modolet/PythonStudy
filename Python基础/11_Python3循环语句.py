print('Python3循环语句')
print()
'''
Python3循环语句
    Python中的循环语句有for和while
    在Python中没有do..while循环
    可以使用break跳出循环体
    可以使用continue跳过本次循环
    注意：
        循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。
'''
'''
while循环
    Python中while语句的一般格式:
while 判断条件(condition)：
    执行语句(statements)……
'''
#实例
print('实例：计算1到100的总和')
n       = 100
sum     = 0
counter = 1
while counter <= n:
    sum     += counter
    counter += 1
print("1 到 %d 之和为： %d"%(n, sum))
del n, sum, counter
print()

'''
无限循环（死循环）
    可以通过设置条件表达式永远不为false来实现无限循环
    可以使用ctrl+c来退出当前的无限循环
    无限循环在服务器上客户端的实时请求非常有用
#实例
while 1:
    num = int(input("输入一个数字  :"))
    print("你输入的数字是: ", num)
'''
'''
while循环使用else语句
    在while...else在语句条件为false是执行else语句块
    语法格式如下
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
'''
#实例
print('while循环使用else语句')
#循环输出数字，并判断大小
count = 0
while count < 5:
    print(count, '小于5')
    count += 1
else:
    print(count, '大于或等于5')
print()

'''
for语句
    Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串
    for循环的一般格式如下
for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''
#实例
print('for循环')
languages = ['C', 'C++', 'Python', 'Java']
for x in languages:
    print(x)
del languages, x
print()

'''
range()函数
    如果需要遍历数字序列，可以使用内置range()函数，他会生成数列
'''
#实例
print("range函数")
for i in range(5):
    print(i)
#可以指定区间的值
for i in range(5, 10):
    print(i)
#还可以指定步长
for i in range(0, -10, -1):
    print(i)
#可以结合range()和len()以遍历一个序列的索引
a = ['Google', 'Baidu', 'Modolet', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i,a[i])

'''
pass语句
    pass是空语句，不做任何事情，一般用作占位语句
'''
