def print_user_info(name, age, sex='男'):
    # 打印用户信息
    print('昵称:{}'.format(name), end='')
    print('年龄:{}'.format(age), end='')
    print('性别:{}'.format(sex))


# 调用print_user_info函数
print_user_info('陈阳', 12)
print_user_info('dada', 14, '女')
