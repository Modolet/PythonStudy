print('Python3元组')
print()
'''
Python3元组
    Python的元组与列表相似，不同之处在于
        元组的元素不能修改
        元组使用小括号，列表使用方括号
    元组创建很简单，只需要在括号（不使用括号也可以）中添加元素，并使用逗号隔开即可
'''
#实例
print('Python3元组')
tup1 = ('Google', 'Modolet', '1999', '614')
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d";#不使用括号也可以
print(type(tup3));
del tup1, tup2, tup3
print()
#创建空元组
tup1 = ();
del tup1;

'''
元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
'''
#实例
print('一个元素的元组')
tup1 = (50)
print(type(tup1))
tup1 = (50,)
print(type(tup1))
del tup1
print()

'''
访问元组
    元组可以使用下标索引来访问元组中的值
'''
#实例
print('访问元组')
tup1 = ('Google', 'Modolet', '1999', '614')
tup2 = (1, 2, 3, 4, 5, 6, 7)
print('tup1[0]: ',tup1[0])
print('tup2[1:5]:',tup2[1:5])
del tup1, tup2
print()

'''
修改元组
    元组中的元素时不允许修改的，但是可以对元组进行连接组合
'''
#实例
print('连接组合元组')
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2;
print (tup3)
del tup1, tup2, tup3
print()

'''
删除元组
    元组中的元素值时不允许删除的，但是可以使用del语句删除整个元组
'''

'''
元组运算符
    与字符串一样，元组之间可以使用+和*进行运算。就是说他们可以组合和赋值，运算后会生成一个新的元组
Python表达式	                结果	                        描述
len((1, 2, 3))	                3	                            计算元素个数
(1, 2, 3) + (4, 5, 6)	        (1, 2, 3, 4, 5, 6)	            连接
('Hi!',) * 4	                ('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
3 in (1, 2, 3)	                True	                        元素是否存在
for x in (1, 2, 3): print (x,)	1 2 3	                        迭代
'''

'''
元组索引，截取
    因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素。如下所示
L = ('Google', 'Microsoft', 'Modolet')
Python表达式	结果	                    描述
L[2]	        'Modolet'	                读取第三个元素
L[-2]	        'Microsoft'	                反向读取；读取倒数第二个元素
L[1:]	        ('Microsoft', 'Modolet')	截取元素，从第二个开始后的所有元素。
'''

'''
元组内置函数
    Python元组包含了以下内置函数
len(tuple)      计算元组元素个数。	
max(tuple)      返回元组中元素最大值。	
min(tuple)      返回元组中元素最小值。	
tuple(seq)      将列表转换为元组。
'''