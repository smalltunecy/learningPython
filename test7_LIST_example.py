# coding:utf-8
#---------------list的使用------------------------
# 1.一个产品，需要列出产品的用户，这时候就可以使用一个list来表示
user = ['liangdianshui','twowater','两点水']
new_user= input('请输入要新的用户名:')

def add_user(new_user):
    user.append(new_user)


add_user(new_user)
print(user)

