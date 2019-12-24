print('Python3字典')
print()
'''
Python3字典
    字典是另一种可变容器，且可存储任意类型对象
    字典的每个键值(key=>value)对用冒号:分割,每个对之间用逗号,分割，整个字典包括在花括号{}中
    键必须是唯一的，但值则不必
    值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组
'''
#实例
d1 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
d2 = {'abc': 456}
d3 = {'abc': 123, 98.7: 37}

del d1, d2, d3

'''
访问字典里的值
    把相应的键放到方括号中
    如果用字典里没有的键访问数据，则会输出错误keyError
'''
#实例
print('访问字典里的值')
dict = {'name': 'Modolet', 'age': 21, 'Class': 'First'}
print("dict['name']:",dict['name'])
print("dict['age]",dict['age'])
del dict
print()

'''
修改字典
    向字典里添加新内容的犯法是增加新的键/值对，修改或删除已有键/值对
'''
#实例
print('修改字典')
dict = {'name': 'Modolet', 'age': 21, 'Class': 'First'}
dict['age'] = 8             #更新age
dict['school'] = 'HBUT'     #添加信息
print("dict['age']",dict['age'])
print("dict['school']",dict['school'])
del dict
print()

'''
删除字典元素
    能删除单一的元素也能清空字典，清空只需一项操作
    显示删除一个字典用del命令
'''
#实例
dict = {'name': 'Modolet', 'age': 21, 'Class': 'First'}

del dict['name']    #删除键name
dict.clear()        #清空字典
del dict            #删除字典

'''
字典键的特性
    字典值可以是任何的Python对象，即可以是标准的对象，也可以是用户定义的，但键不行
    两个重要的点需要记住
        不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如实例1
        键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如实例2
'''
#实例
print('字典键的特性')
#实例1
print('实例1')
dict = {'name': 'Modolet','age': 20,'name': 'Sulilet'}
print("dict['name]", dict['name'])
del dict
print()
#实例2
print('实例2')
dict = {['name']: 'Modolet','age': 7}
print(dict)#会报TypeError错误
del dict
print()
'''
字典内置函数&方法
    Python字典包含了以下内置函数
len(dict)           计算字典元素个数，即键的总数。	
str(dict)           输出字典，以可打印的字符串表示。	
type(variable)      返回输入的变量类型，如果变量是字典就返回字典类型。	
    Python字典包含了以下内置方法
radiansdict.clear()                             删除字典内所有元素
radiansdict.copy()                              返回一个字典的浅复制
radiansdict.fromkeys()                          创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
radiansdict.get(key, default=None)              返回指定键的值，如果值不在字典中返回default值
key in dict                                     如果键在字典dict里返回true，否则返回false
radiansdict.items()                             以列表返回可遍历的(键, 值) 元组数组
radiansdict.keys()                              返回一个迭代器，可以使用 list() 来转换为列表
radiansdict.setdefault(key, default=None)       和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
radiansdict.update(dict2)                       把字典dict2的键/值对更新到dict里
radiansdict.values()                            返回一个迭代器，可以使用 list() 来转换为列表
pop(key[,default])                              删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
popitem()                                       随机返回并删除字典中的最后一对键和值。
'''