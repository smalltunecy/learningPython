name1 = 'First'
name2 = 'Second'
name3 = 'Third'
name4 = 'Fourth'
name5 = 'Fifth'
'''列表就是用中括号[]括起来的数据，每一个数据就叫做元素。每个元素之间使用逗号分隔'''
name = ['First', 'Second', 'Third', 'Fourth', 'Fifth']

list1 = ['两点水', 'First', 123]
# print(list1)
#
'''用索引取出列表的元素'''
# print(list1[0])
#
'''通过方括号形式来截取列表中的数据'''
# print(list1[0:2])
# print(name[0:2])
# print(name[:2])
# print(name[:])
# print(name[1:2])
# print(name[0:3])

'''怎么去更新List'''
# name[1] = 2
# name.append('Sixth')
# print(name)

'''怎么删除List'''
# print(name)
# del name[3]
# print(name)

'''List运算符'''
#计算元素个数
print(name)
print(len(name))

#组合
print([1,2,3]+[4,5,6])

#复制
print(['Hi']*4)

#元素是否存在于列表中