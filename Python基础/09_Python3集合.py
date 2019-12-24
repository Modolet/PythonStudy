print('Python3集合')
print()
'''
Python3集合
    集合(set)时一个无序的不重复元素序列
    可以使用大括号{}或者set()函数创建集合
    注意：
        创建一个空集合必须用set()而不是{}，因为{}是用来创建一个空字典
    创建格式
        parame = {value01, value02,...}
        或者
        :param = set(value)
'''
#实例
print('Python3集合实例')
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   #演示去重功能
print('orange' in basket)#快速判断元素是否在集合内
print('crabgrass' in basket)
#下面展示两个集合间的运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)    #集合a中包含而集合b中不包含的元素
print(a | b)    #集合a或b中包含的所有元素
print(a & b)    #集合a和b中都包含了的元素
print(a ^ b)    #不同时包含与a和b的元素
del a, b, basket
print()

'''
类似列表推导式，同样集合支持集合推导式(Set comprehension)
'''
#实例
print('集合推导式')
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
del a
print()

'''
集合的基本操作
    添加元素
        s.add(x)        将元素添加到集合s中，如果元素已存在，则不进行任何操作
        s.update(x)     也可添加元素，且参数可以是列表，元组，字典等。x可以有多个，用逗号分开
    移除元素
        s.remove(x)     将元素x从集合s中溢出，如果元素不存在，则会发生错误
        s.discard(x)    移除集合中的元素x，且如果元素不存在也不会发生错误
        s.pop()         随机删除集合中的一个元素
    计算集合元素个数
        len(s)          计算集合s元素个数
    清空集合
        s.clear()       清空集合s
    判断元素是否在集合中
        x in s          判断元素x是否在集合s中，存在返回Ture，不存在返回False
'''

'''
集合内置方法完整列表
add()	                        为集合添加元素
clear()	                        移除集合中的所有元素
copy()	                        拷贝一个集合
difference()	                返回多个集合的差集
difference_update()	            移除集合中的元素，该元素在指定的集合也存在。
discard()	                    删除集合中指定的元素
intersection()	                返回集合的交集
intersection_update()	        返回集合的交集。
isdisjoint()	                判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	                    判断指定集合是否为该方法参数集合的子集。
issuperset()	                判断该方法的参数集合是否为指定集合的子集
pop()	                        随机移除元素
remove()	                    移除指定元素
symmetric_difference()	        返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	                        返回两个集合的并集
update()	                    给集合添加元素
'''