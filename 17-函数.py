
"""
    函数就是将⼀段具有独⽴功能的代码块 整合到⼀个整体并命名，在需要的位置调⽤这个名称即可完成对应的需求。
    函数在开发过程中，可以更⾼效的实现代码重⽤。

    函数的定义：
        def 函数名(参数):
            代码1
            代码2
            代码3
            ......
            return 返回值

    使用函数，又叫做 调用函数
        函数名(参数)


    注意：python中的函数必须先定义再调用，函数只有调用才会执行

    函数名的命名规则和变量命名规则相同，小驼峰或者下划线，在python建议使用下划线，即：所有单词小写，多个单词使用下划线分割

    函数分类：
        1. 无参数，无返回值 函数
            def 函数名():
                代码
                ......
                return None

            或者不写 return None

        例如：
            def show():
                print("正在学习python")


            show()  # 正在学习python

        2. 有参数，无返回值 函数
            def 函数名(参数1, 参数2, ...):
                代码
                ......

            函数的参数可以有多个

        例如：
            def get_sum(a, b):
                ret = a + b
                print(f"两个数之和为:{ret}")


            get_sum(10, 20)  # 两个数之和为:30

            声明了get_sum函数，并且这个函数有两个参数，get_sum(10, 20)调用函数，会把10传给参数a，把20传给参数b
            通常上，在函数声明上的参数，叫做形参 （形式参数） 用来接收真正参数的值，例如get_sum中的 参数 a 和参数 b
            而实际调用传递的参数，叫做实参，例如get_sum(10, 20)中10，20都是实参

            注意：
                通常上，定义的函数有n个形参，则函数调用时必须传递n个实参，一一对应

        3. 有参数，有返回值 的函数
            def 函数名(参数1, 参数2, ...):
                代码
                ......
                return 返回值

        return 后面就是返回值，可以是一个数，也可以是一个表达式（表达式会执行，最后将结果返回）
        并且一个函数只能有一个return语句，当函数执行到return后，会结束函数执行，因此多写几个return语句永远只会执行到第一个return语句就结束
        例如：
            def get_multiply(a, b):
                ret = a * b
                return ret


            num = get_multiply(10, 20)
            print(num)  # 200

        函数有返回值，在调用时，可以使用变量接收这个返回值，以供给后面代码使用

    在之前学习已经接触了很多函数：
        print()函数，无返回值
        type() 函数，有参数，有返回值
        还有一些，字符串、列表、元组、.....等常用的函数


    一般来说，一个函数是完成一个特定任务的代码，为了方便别人使用，需要书写 函数说明文档，说明函数的功能，参数，返回值等信息
    函数说明文档使用 三对双引号，并且在函数体内首行书写
    def 函数名(参数):
        ""\"这里是函数说明文档\"""
        上面使用\转义，是因为和当前文档冲突
        代码
        return 返回值

    def print_sum(a, b):
        \"""
        输出两个数的和
        :param a: 被加数
        :param b: 加数
        :return: 无返回值
        \"""
        ret = a + b
        print(f"两个数之和为:{ret}")

    param、return 会自动生成

    当书写了函数文档时，可以使用help()函数，输出函数文档
    例如：
        help(print_sum)
        # print_sum(a, b)
        #     输出两个数的和
        #     :param a: 被加数
        #     :param b: 加数
        #     :return: 无返回值


    函数嵌套：
        1. 函数声明中，调用另一个已存在的函数
        2. 函数声明中，在此函数内部再声明一个函数（此种情况，在之后演示，这里不说明）

        例如：
            def test_b():
                print('---- test_b start----')
                print('这⾥是test_b函数执⾏的代码...(省略)...')
                print('---- test_b end----')


            def test_a():
                print('---- test_a start----')
                test_b()
                print('---- test_a end----')


            test_a()
        上述代码一开始声明了一个test_b函数，之后又声明了test_a函数，不过在test_a函数体内，直接调用了test_b函数，
        虽然test_a调用了test_b，但是此时，test_a函数还没调用，因此test_a里代码不会执行，既而test_b也不会被执行
        当执行到test_a()这一行代码，此时，test_a被调用，执行test_a里面代码，继而test_b执行......

    需求：求三个数平均值，用一个函数求和，一个函数求平均值
        def sum_num(a, b, c):
            return a + b + c


        def average_num(a, b, c):
            sumResult = sum_num(a, b, c)
            return sumResult / 3


        result = average_num(1, 2, 3)
        print(result)  # 2.0


    变量作用域：
        1. 全局变量：一般来说，不是声明在函数内部的变量都是全局变量
        2. 局部变量：声明在函数内部的变量

        例如：
            b = 200
            def testA():
                a = 100
                print(a)

            此时，b是全局变量，a是局部变量
            全局变量，在本.py文件里都可以访问，而局部变量只能在当前函数里访问
            例如：
                b = 200  # 全局变量
                def test():
                    a = 100  # 局部变量
                    print(a)  # 100  局部变量，在当前函数内，可以访问
                    print(b)  # 200 全局变量，在函数内部，可以访问
                test()  # 调用函数

                print(a)  # 错误，变量a找不到，无法访问，因为a是局部变量，a定义在test函数内部，离开了test函数体就不能访问

            局部变量和全局变量同名情况：
                b = 200  # 全局变量
                def test():
                    b = 300 # 局部变量，此时同名，默认声明了一个新的局部变量 b,且b=300
                    print(b) # 300
                test()  # 调用函数
                print(b)  # 200 访问不了局部变量，因此访问全局变量b=200

            这样就出现一个问题，在没有传参的情况下，想在函数内部修改全局变量的值，怎么解决
            此时需要使用 关键字 global 标识函数内当前变量是全局变量
            例如：
                b = 200  # 全局变量
                def test_global():
                    global b  # 使用global 关键字，说明当前使用的是全局变量
                    b = 300  # 对全局变量进行修改
                    print(b) # 300
                test_global()  # 调用函数
                print(b)  # 300 全局变量在函数内部被修改

        其实还有个 关键字 nonlocal 这个使用在函数内定义函数时使用，之后讲解


    函数的返回值：
        函数返回值可以是任何一个类型，例如：数字、布尔、字符串、列表、......
        函数没有返回值，指的是函数的返回值是 None
        函数的返回值可以是一个表达式：
        例如：
            return 1+1
            此时返回 2
            return 3 > 2
            此时返回 True
            ......

        函数可以返回多个数据：
            例如：当返回值是多个数据，可以将这些数据组合成，列表、集合、元组等
            def example_list():
                ....
                return [1,2,3]

            def example_tuple():
                ....
                return (1,2,3)

            def example_dict():
                ....
                return {'name' : '533', 'age' : 26}

        不过在没有特殊情况要求，一般会把多个数据包装成元组返回：
            def example_tuple():
                ....
                return (1,2,3)
        因为元组存在自动装包和拆包，因此上述代码可以简化：
            def example_tuple():
                ....
                return 1,2,3
        python会自动将 return 1,2,3装包成 return (1,2,3)
        当调用此函数，用参数接收返回值时可以简化为：
        a, b, c =  example_tuple()
        python会自动将元组(1,2,3)拆包，然后赋值给a, b, c
        注意：需要返回值元组元素个数和参数接收个数相同

        所以：
            def example_tuple():
                ....
                return 1,2,3

            a, b, c =  example_tuple()

"""


def show():
    print("正在学习python")


show()  # 正在学习python


def get_sum(a, b):
    ret = a + b
    print(f"两个数之和为:{ret}")


get_sum(10, 20)  # 两个数之和为:30


def get_multiply(a, b):
    ret = a * b
    return ret


num = get_multiply(10, 20)
print(num)  # 200


def print_sum(a, b):
    """
    输出两个数的和
    :param a: 被加数
    :param b: 加数
    :return: 无返回值
    """
    ret = a + b
    print(f"两个数之和为:{ret}")


help(print_sum)
# print_sum(a, b)
#     输出两个数的和
#     :param a: 被加数
#     :param b: 加数
#     :return: 无返回值


def test_b():
    print('---- test_b start----')
    print('这⾥是test_b函数执⾏的代码...(省略)...')
    print('---- test_b end----')


def test_a():
    print('---- test_a start----')
    test_b()
    print('---- test_a end----')


test_a()


def sum_num(a, b, c):
    return a + b + c


def average_num(a, b, c):
    sumResult = sum_num(a, b, c)
    return sumResult / 3


result = average_num(1, 2, 3)
print(result)  # 2.0

b = 200  # 全局变量


def test():
    b = 300  # 局部变量，此时同名，默认声明了一个新的局部变量 b,且b=300
    print(b)  # 300


test()
print(b)  # 200 访问不了局部变量，因此访问全局变量b=200

a = 200  # 全局变量


def test_global():
    global a  # 使用global 关键字，说明当前使用的是全局变量
    a = 300  # 对全局变量进行修改
    print(a)  # 300


test_global()
print(a)  # 300 全局变量在函数内部被修改



