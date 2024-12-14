
"""
    条件语句之if-elif-else
    有的情况条件有多个则需要使用if-elif-else语句，并且elif可以有多个，适配不同的条件

    格式：
        if 条件1：
            条件1成立时执行的语句1
            条件1成立时执行的语句2
            条件1成立时执行的语句3
            ......
        elif 条件2:
            条件2成立时执行的语句1
            条件2成立时执行的语句2
            条件2成立时执行的语句3
            ......
        elif 条件3:
            条件3成立时执行的语句1
            条件3成立时执行的语句2
            条件3成立时执行的语句3
            ......
        ......
        else:
            所有条件都不成立执行的语句1
            所有条件都不成立执行的语句2
            所有条件都不成立执行的语句3
            ......

    注意：
        - 1 同一对 if-else 或者 if-elif-else  if-elif-...-else需要对其
        - 2 可以if单独使用，可以if-else 配合使用 可以if-elif-else配合使用 也可以if-elif配合使用
            即：不能单独出现 else语句或者elif或者elif-else


    条件语句可以嵌套使用，也就是if语句里还有if语句
    例如：
        if 大条件:
            if 小条件：
                小条件成立语句执行
            else:
                小条件不成立语句执行
        else:
            大条件不成立时执行
    条件嵌套没有新知识，只是形式不一样


    if-else 简单的情况下可以写在一行 称为三目运算符
    格式：
        a = 表达式0 if 表达式1 else 表达式2
    解释：
        如果表达式1为真，则a的值为 表达式0的计算结果 否则 a的值 是表达式2的结果

    例如：
        a = 1
        b = 2
        c = a if a > b else b
        print(c)  ------> 2

        因为 a > b不成立，所以 就把b的值赋值给c， c=2

"""

"""
    案例：
        中国合法⼯作年龄为18-60岁，即如果年龄⼩于18的情况为童⼯，不合法；如果年龄在18-
        60岁之间为合法⼯龄；⼤于60岁为法定退休年龄。
"""

age = int(input("请输入你的年龄："))

if age < 18:
    print("年龄⼩于18的情况为童⼯，不合法")
elif age > 60:
    print("⼤于60岁为法定退休年龄")
else:
    print("年龄在18-60岁之间为合法⼯龄")

a = 1
b = 2
c = a if a > b else b
print(c)


