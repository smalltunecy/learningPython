# def sum(num1, num2):
#     #两数之和
#     if not (isinstance(num1, (int, float))) and (isinstance(num2, (int, float))):
#         raise TypeError("参数类型错误")
#     return num1+num2
# print(sum('2',11))

def division(num1, num2):
    #求商与余数
    a = num1 % num2
    b = (num1-a)/num2
    return b,a
num1 ,num2 =division(9,4)
tuple1 = division(9,4)
print(num1,num2)
print(tuple1)