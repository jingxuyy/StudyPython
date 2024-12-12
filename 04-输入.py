
"""
    输入，表示键盘输入到程序里
    input(*args, **kwargs)
    input函数没有其它参数，input()函数括号里可以输入一些提示信息，用来提醒用户输入
    此函数有返回值，返回值就是用户输入的内容
    注意：
        input() 会将用户输入的一切信息转换成字符串
        input("提示信息")
        例如：
            password = input('请输⼊您的密码：')
            print(f'您输⼊的密码是{password}')
            print(type(password))  ------> <class 'str'>
"""
password = input('请输⼊您的密码：')
print(f'您输⼊的密码是{password}')
print(type(password))


"""
    数据类型转换，一些数据类型可以彼此之间相互转换，例如 字符串形式的 '123' 可以转换成 整数 int 类型的 123
    具体如下：
        函数                          说明
        int(x [,base ])             将x转换为⼀个整数
        float(x )                   将x转换为⼀个浮点数
        complex(real [,imag ])      创建⼀个复数，real为实部，imag为虚部
        str(x )                     将对象 x 转换为字符串
        repr(x )                    将对象 x 转换为表达式字符串
        eval(str )                  ⽤来计算在字符串中的有效Python表达式,并返回⼀个对象
        tuple(s )                   将序列 s 转换为⼀个元组
        list(s )                    将序列 s 转换为⼀个列表
        chr(x )                     将⼀个整数转换为⼀个Unicode字符
        ord(x )                     将⼀个字符转换为它的ASCII整数值
        hex(x )                     将⼀个整数转换为⼀个⼗六进制字符串
        oct(x )                     将⼀个整数转换为⼀个⼋进制字符串
        bin(x )                     将⼀个整数转换为⼀个⼆进制字符串
    
    常用的是 int float str 之间的相互转换，列表，元组等其它类型转换，在之后讲解
    
    str1 = '123'
    print(type(str1))   ------> <class 'str'>
    num1 = int(str1)
    print(type(num1))   ------> <class 'int'>
    
    str2 = '0.33'
    print(type(str2))   ------> <class 'str'>
    num2 = float(str2)
    print(type(num2))   ------> <class 'float'>
    
    print(type(num2))   ------> <class 'float'>
    num3 = int(num2)    
    print(num3)         ------> 0  浮点数转成整数会损失精度
    print(type(num3))   ------> <class 'int'>
    
    
    因此对于input输入函数，可以使用类型转换将用户输入转换成正确类型
    
    
"""

str1 = '123'
print(type(str1))
num1 = int(str1)
print(type(num1))

str2 = '0.33'
print(type(str2))
num2 = float(str2)
print(type(num2))

print(type(num2))
num3 = int(num2)
print(num3)
print(type(num3))


# 需求：input接收⽤户输⼊，⽤户输⼊“1”，将这个数据1转换成整型。
# 1. 接收⽤户输⼊
num = input('请输⼊您的幸运数字：')
# 2. 打印结果
print(f"您的幸运数字是{num}")
# 3. 检测接收到的⽤户输⼊的数据类型 -- str类型
print(type(num))
# 4. 转换数据类型为整型 -- int类型
print(type(int(num)))

