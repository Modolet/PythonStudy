print('Python3迭代器与生成器')
print()
'''
迭代器
    迭代时Python最强大的功能之一，是访问集合元素的一种方式
    迭代器是一个可以记住遍历的位置的对象
    迭代器对象从集合的第一个元素开始访问，直到所有的对象被访问结束。迭代器只能往前不能后退
    迭代器有两个基本的方法，iter()和next()
    字符串，列表或者元组对象都可以用于创建迭代器
    迭代器可以使用常规for语句进行遍历（实例2）
    也可以使用next语句（实例3）
'''
#实例1
print('迭代器实例1')
list = [1, 2, 3, 4]
it = iter(list) #创建迭代器
print(next(it)) #输出迭代器的下一个元素
print(next(it))
del list, it
print()
#实例2
print('迭代器实例2')
list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x, end=" ")
del list, it, x
print()
#实例3
print('迭代器实例3')
import sys  # 引入 sys 模块
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        break;
del list, it
print()
'''
创建一个迭代器
    把一个类作为一个迭代器使用需要在类中实现两个方法__iter__()与__next__()
    如果了解面向对象编程的话，就知道类中有一个构造函数，Python的构造函数为__init__()。他会在对象初始化的时候执行
    __iter__()方法返回一个特殊的迭代器对象，这个迭代器对象实现了__next__()方法并通过StopIteration异常标识迭代的完成
    __next__()方法（Python2里是next()）会返回下一个迭代器对象
'''
#实例
#创建一个返回数字的迭代器，初始值为1，逐步递增1
print('创建一个迭代器')
class MyNumbers1:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers1()
myiter  = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
del myclass, myiter
print()

'''
StopIteration
    StopIteration异常用于标识迭代的完成，防止出现无限循环的情况，在__next__()方法中我们可以设置在完成指定寻黄次数后处罚StopIteration异常来结束迭代
'''
#实例
#在20次迭代后停止执行
print('StopIteration')
class MyNumbers2:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = MyNumbers2()
myiter = iter(myclass)

for x in myiter:
    print(x)
del myiter, myclass
print()

'''
生成器
    在Python中，使用了yield的函数被称为生成器(generator)
    跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器
    在调用生成器运行的过程中，每次遇到yield是函数会暂停并保存当前所有的运行信息，放回yield的值，并在下一次执行next()方法时从当前位置继续运行
    调用一个生成器函数，返回的是一个迭代器对象
'''
#实例
print('生成器')
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)# f 是一个迭代器，由生成器返回生成
while True:
    try:print(next(f),end=" ")
    except StopIteration:
        break