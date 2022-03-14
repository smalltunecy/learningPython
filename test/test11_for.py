for num in range(10,20):
    for i in range(2,num):
        if num%i ==0:
            j=num/i
            print('%d是一个合数'%num)
            break
    else:
            print('%d是一个质数'%num)