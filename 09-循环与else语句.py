
"""
    循环可以和else配合使⽤，else下⽅缩进的代码指的是当循环正常结束之后要执⾏的代码。

    循环正常结束： 指的是正常结束，例如使用break是非正常，而continue是正常，另外如果循环内抛出了异常也是非正常

    格式：
        while 条件:
            ......
        else:
            ......


        for i in 序列：
            ......
        else:
            ......
"""

# while-else 正常退出
i = 1
while i <= 5:
    print('Python')
    i += 1
else:
    print('正常退出打印')

# while-else 不正常退出
i = 1
while i <= 5:
    print('Python')
    if i == 3:
        break
    i += 1
else:
    print('正常退出打印')

# for-else 正常退出
str1 = 'Python'
for i in str1:
    print(i)
else:
    print('循环正常结束之后执⾏的代码')

# for-else 不正常退出
str1 = 'Python'
for i in str1:
    if i == 'y':
        print('遇到y不打印')
        break
    print(i)
else:
    print('循环正常结束之后执⾏的代码')
