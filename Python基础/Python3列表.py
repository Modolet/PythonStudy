print("Python3列表")
print()

'''
Python3列表
    序列是Python中最基本的数据结构
    序列的索引从0开始
    序列可以进行的操作包括索引，切片，加，乘，检查成员
    列表是最常用的python数据类型，它可以作为一个方括号内的逗号分隔值出现
    列表的数据项不需要具有相同类型
    创建一个列表，只要把逗号分隔的不同数据项使用方括号括起来即可
    与字符串的索引一样，列表索引从0开始，列表可以进行截取，组合等
'''
#实例
print('Python3列表')
list1 = ['Google', 'Modolet', 1999, 614]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

del list1, list2, list3
print()

'''
访问列表中的值
    使用下表索引来访问列表中的值，也可以用方括号的形式截取字符
'''
#实例
print('访问列表中的值')
list1 = ['Google', 'Modolet', 1999, 614]
list2 = [1, 2, 3, 4, 5, 6, 7]

print('List1[0]', list1[0])
print('list2[1:5]',list2[1:5])

del list1,list2
print()

'''
更新列表
    可以对列表的数据项进行修改或者更新，也可以使用append()方法来添加列表项
'''
#实例
print('更新列表')
list = ['Google', 'Modolet', 1999, 614]

print('第三个元素为：',list[2])
list[2] = 6666
print('更新后的第三个元素为：',list[3])

del list
print()

'''
删除元素
    可以使用del语句来删除列表中的元素
'''
#实例
print('删除元素')
list = ['Google', 'Modolet', 1999, 614]
print('原始列表：',list)
del list[2]
print('删除第三个元素：',list)
print()

'''
Python列表脚本操作符
    列表对+和*的操作符与字符串相似。+用于组合列表，*用于重复列表。如下表所示
    Python 表达式	                        结果	                        描述
    len([1, 2, 3])	                        3	                            长度
    [1, 2, 3] + [4, 5, 6]	                [1, 2, 3, 4, 5, 6]	            组合
    ['Hi!'] * 4	                            ['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
    3 in [1, 2, 3]	                        True	                        元素是否存在于列表中
    for x in [1, 2, 3]: print(x, end=" ")	1 2 3	                        迭代
'''

'''
Python列表截取与拼接
    Python的列表截取与字符串操作类似，如下所示
        L=['Google', 'Modolet', 'Microsoft']
        Python 表达式	结果	                    描述
        L[2]	        'Microsoft'	                读取第三个元素
        L[-2]	        'Modolet'	                从右侧开始读取倒数第二个元素: count from the right
        L[1:]	        ['Modolet', 'Microsoft']	输出从第二个元素开始后的所有元素
    列表还支持拼接操作
'''
#实例
print('拼接列表')
list = [1, 2, 3, 4, 5]
list += [5, 6, 7, 8, 9]
print(list)
del list
print()

'''
嵌套列表
    使用嵌套列表即在列表里创建其他列表
'''
#实例
print('嵌套列表')
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])
print()

'''
Python列表函数&方法
Python包含以下函数
len(list)                           列表元素个数
max(list)                           返回列表元素最大值
min(list)                           返回列表元素最小值
list(seq)                           将元组转换为列表
Python包含以下方法
list.append(obj)                    在列表末尾添加新的对象
list.count(obj)                     统计某个元素在列表中出现的次数
list.extend(seq)                    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)                     从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj)             将对象插入列表
list.pop([index=-1])                移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)                    移除列表中某个值的第一个匹配项
list.reverse()                      反向列表中元素
list.sort( key=None, reverse=False) 对原列表进行排序
list.clear()                        清空列表
list.copy()                         复制列表
'''