
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


    函数的参数：
        函数的参数可以细分为四种：1. 位置参数 2. 关键字参数 3. 缺省参数 4. 不定长参数

        1. 位置参数：
            例如：
                def user_info(name, age, gender):
                    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')

                user_info('TOM', 20, '男')  # 您的名字是TOM, 年龄是20, 性别是男    位置参数，一一对应
                user_info(20, 'TOM', '男')  # 您的名字是20, 年龄是TOM, 性别是男    位置参数，没有一一对应

            位置参数，具体是，函数的形参和实参 位置要一一对应，否则程序会出现错误

        2. 关键字参数：
            关键字参数是对于函数调用方而言的
            位置参数调用：user_info('TOM', 20, '男')
            关键字参数调用：user_info(name='Tom', age=20, gender='男')  # 您的名字是TOM, 年龄是20, 性别是男
            即关键字参数，就是调用方，在调用时，指明把实参传递给哪个形成
            由于关键字参数，指定了哪个实参对应哪个形参，因此不需要位置一一对应
            user_info(gender='男', age=20, name='Tom')  # 您的名字是TOM, 年龄是20, 性别是男

            位置参数和关键字参数可以一起使用：
            user_info('Tom', age=20, gender='男')  # 您的名字是TOM, 年龄是20, 性别是男

            位置参数和关键字参数一起使用：必须位置参数写在最前面
            例如：
                user_info(name='Tom', 20, gender='男')  错误，位置参数20在关键字参数中间
                user_info('Tom', age=20, gender='男') 正确
                user_info('Tom', 20, gender='男') 正确
                user_info('Tom', gender='男', age=20) 正确

        3. 缺省参数：
            缺省参数是相对于形参而言的
            缺省参数指的是，函数定义时，给了函数的形参默认值，这样，调用方可以选择要不要给缺省参数赋值，不给则使用默认值
            例如：
                def user_info(name, age, gender='男'):
                    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')

                user_info('TOM', 20)  # 您的名字是TOM, 年龄是20, 性别是男
                user_info('Rose', 18, '⼥')  # 您的名字是Rose, 年龄是18, 性别是⼥
            使用user_info('TOM', 20)调用时，没有给缺省参数 gender赋值，则调用函数时，使用默认值
            使用user_info('Rose', 18, '⼥')调用时，有给缺省参数 gender赋值为 女，则调用函数时，使用调用传递过来的值
            使用缺省参数可以实现形参个数和实参个数不相等

        4. 不定长参数：
            有的时候函数定义时，并不知道函数调用方会传递多少参数过来，即不定参数用于接收多个参数，且参数个数动态变化
            例如：
                需求根据用户输入的数字求和，用户可以输入1、2、3、4、....、n个参数
                def get_all_sum(*args):
                    sum = 0
                    for num in args:
                        sum += num
                    print(f"{len(args)}个数的和是：{sum}")

                get_all_sum(1)  # 1个数的和是：1
                get_all_sum(1, 2)  # 2个数的和是：3
                get_all_sum(1, 2, 3)  # 3个数的和是：6
                get_all_sum(1, 2, 3, 4)  # 4个数的和是：10

            不定长参数 函数形参 使用 *args 表示不定长参数   但是并不是一定使用 *args  ，其中args可以是任何变量名，不过在python中默认使用args
            args 其实是一个元组，当调用方传递一个数，则 args为一个元素的元组，传递n个参数 args为n个元素的元组

            同理：
                也可以使用 **kwargs 接收多个参数，不过 kwargs表示的是字典，因此，调用方传递参数时，需要使用关键字参数传递，即key=value传递
                例如：
                    def user_info(**kwargs):
                        print(kwargs)

                    user_info(name='TOM', age=18, id=110)  # {'name': 'TOM', 'age': 18, 'id': 110}


        多种参数在一起时：定义时，需要指定 不定长参数在最后，位置参数在最前面，不定长参数中：需要 *args在 **kwargs前面
                        调用时，位置参数在最前面，不定长参数在最后


    python的变量交换值：
        a=1, b= 2  现在要求 a和b的值相互交换，a=2, b=1

        方案一：
        使用临时变量
        c = a
        a = b
        b = c

        方案二：
        python特有的交换方式
        a, b = b, a


    引用：
        指的是变量在内存里的位置（不是真正位置，做了转换）
        可以通过两个变量的引用来判断两个变量是不是同一个变量
        id(变量)
        id函数可以输出变量的引用
        print(id(1))  # 1507308431664


    注意：
        如果函数参数接收的是不可变数据类型，则在函数内对这个参数进行修改不会影响到实参
        如果函数参数接收的是可变数据类型，则在函数内部对这个参数进行修改会影响到实参
        var_c = 10
        var_list = [10]
        def var(c, b):
            c = 20
            b.append(20)

        var(var_c, var_list)
        print(var_c)
        print(var_list)


    匿名函数：即没有名字的函数，当一个函数只使用一次，并且函数体只有一个表达式可以使用
    形式：
        lambda 参数 : 表达式
    参数可以没有，也可以有多个

    也可以强行给匿名函数取名字
    函数名 = lambda 参数 : 表达式

    def sum_func(a1, b1, c1):
        return a1 + b1 + c1

    sum_lambda = lambda a1, b1, c1: a1 + b1 + c1
    print(sum_func(1, 2, 3))  # 6
    print(sum_lambda(1, 2, 3))  # 6
    print((lambda a1, b1, c1: a1 + b1 + c1)(1, 2, 3))  # 6

    一般来说：匿名函数可以当作函数参数传递、或者函数返回值传递



    函数递归：
        即函数自己调用自己：注意函数自己调用自己，必须有一个停止条件，不然自己调用自己会一直调用下去

    例如：
        求 n 的阶乘
        n! = n * (n-1)!
        (n-1)! = (n-1)*(n-2)!
        .......
        1!= 1 * 0!= 1

        如果把求阶乘定义一个函数，就会发现，n! = n * (n-1)! 是自己调用自己，只是第一次 实参是 n 第二次实参是n-1

        def fact(n):
            if n == 1 or n == 0:
                return 1
            return n * fact(n-1)

        print(fact(1))  # 1
        print(fact(2))  # 2
        print(fact(3))  # 6
        print(fact(4))  # 24
        print(fact(5))  # 120


    说明：
        1. 把函数当作参数传递，此时实参传递函数名，不能传递 函数名() 这就等于把函数调用了执行了
            另外在函数使用形参接受了函数名，此时这个形参就是函数名，可以进行函数调用

        2. 把函数当作返回值：1.要么 return 函数名() 这样就等于把函数执行后的返回值再返回出去
                            2. 要么 return 函数名  此时外部结束返回值的变量就是函数名，可以像函数那样调用

    这样把函数当作参数传递或者返回的函数称为高阶函数
    在python中有几个内置的告诫函数

    1. map函数
        map(function, iterable, ...)
            function：函数
            iterable：一个或多个序列

        作用：map将传入的函数依次作用到序列的每个元素，并把结果作为新的序列返回，如果多个序列，则要求每个序列长度相等   一般做数据转换，或者数据映射

        def func1(x):
            return x**2

        list1 = [1, 2, 3, 4, 5, 6, 7, 8]
        result1 = list(map(func1, list1))
        print(result1)  # [1, 4, 9, 16, 25, 36, 49, 64]
        result2 = list(map(lambda x: x**2, list1))           由于func1只有一条语句，因此可以使用lambda进行替换
        print(result2)  # [1, 4, 9, 16, 25, 36, 49, 64]

        1   2   3   4   5   6   7   8

                x**2
        1   4   9   16  25  36  49  64

        由于map函数是进行数据转换，因此执行前后序列里元素个数不会发生变换


    2. filter函数
        filter(function, iterable)
            function：判断函数。
            iterable ：可迭代对象

        作用：用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新序列    主要用于筛选数据

        list1 = [1, 2, 3, 4, 5, 6, 7, 8]
        result3 = list(filter(lambda x: x % 2 == 0, list1))
        print(result3)  # [2, 4, 6, 8]
        例如：上述通过传入一个匿名函数筛选列表中偶数，形成新的列表
        由于 filter函数是用于过滤的，因此传入filter的函数其函数体返回值或者表达式需要是一个布尔类型，filter根据这个布尔条件进行筛选
        由于filter函数是用于过滤的所以，执行过后其结果序列小于等于原序列个数


    3. reduce函数
        reduce(function,sequence[,initial]=>value)
            function：函数
            iterable：一个或多个序列

        作用：这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，最终返回单个累积值
        也就是，reduce会将序列每个元素进行操作，最后返回一个元素

        from functools import reduce
        result4 = reduce(lambda x, y: x + y, list1)
        print(result4)  # 36

        如上， lambda x, y: x + y 是求和，那它会作用到序列每一个元素，最终结果就是元素求和
        from functools import reduce 这是是导包语句，reduce函数放在了functools文件里，需要导入到当前文件，这里后面会讲解，
        如果想使用reduce就必须 from functools import reduce

        注意：序列经过reduce后，只会计算出一个结果，并reduce中传递的函数 其参数必须是两个

    4. sorted函数
        sorted(iterable,  key=None, reverse=False)
            iterable:可迭代对象。
            key:主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
            reverse :排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

        主要用于排序，会生成新的序列

        print(sorted(list1, reverse=True))  # [8, 7, 6, 5, 4, 3, 2, 1]
        L = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
        print(sorted(L, key=lambda x: x[1]))  # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
        students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
        print(sorted(students, key=lambda s: s[2]))  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

        元素是一个值的sorted函数可以不传递函数
        元素是多个值的，例如字典、列表里存储元组如上L，students可以传递函数，这个函数只用来指明按照哪个值进行排序的









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


def user_info(name, age, gender):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


user_info('TOM', 20, '男')  # 您的名字是TOM, 年龄是20, 性别是男
user_info(20, 'TOM', '男')  # 您的名字是20, 年龄是TOM, 性别是男

user_info(name='Tom', age=20, gender='男')  # 您的名字是TOM, 年龄是20, 性别是男
user_info(gender='男', age=20, name='Tom')  # 您的名字是TOM, 年龄是20, 性别是男

user_info('Tom', age=20, gender='男')  # 您的名字是TOM, 年龄是20, 性别是男


def user_info(name, age, gender='男'):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


user_info('TOM', 20)  # 您的名字是TOM, 年龄是20, 性别是男
user_info('Rose', 18, '⼥')  # 您的名字是Rose, 年龄是18, 性别是⼥


def get_all_sum(*args):
    sum = 0
    for num in args:
        sum += num
    print(f"{len(args)}个数的和是：{sum}")


get_all_sum(1)  # 1个数的和是：1
get_all_sum(1, 2)  # 2个数的和是：3
get_all_sum(1, 2, 3)  # 3个数的和是：6
get_all_sum(1, 2, 3, 4)  # 4个数的和是：10


def user_info(**kwargs):
    print(kwargs)


user_info(name='TOM', age=18, id=110)  # {'name': 'TOM', 'age': 18, 'id': 110}


print(id(1))  # 1507308431664


var_c = 10
var_list = [10]


def var(c, b):
    c = 20
    b.append(20)


var(var_c, var_list)
print(var_c)  # 10
print(var_list)  # [10, 20]


def sum_func(a1, b1, c1):
    return a1 + b1 + c1


sum_lambda = lambda a1, b1, c1: a1 + b1 + c1
print(sum_func(1, 2, 3))  # 6
print(sum_lambda(1, 2, 3))  # 6
print((lambda a1, b1, c1: a1 + b1 + c1)(1, 2, 3))  # 6


def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)


print(fact(1))  # 1
print(fact(2))  # 2
print(fact(3))  # 6
print(fact(4))  # 24
print(fact(5))  # 120


def func1(x):
    return x**2


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
result1 = list(map(func1, list1))
print(result1)  # [1, 4, 9, 16, 25, 36, 49, 64]
result2 = list(map(lambda x: x**2, list1))
print(result2)  # [1, 4, 9, 16, 25, 36, 49, 64]

result3 = list(filter(lambda x: x % 2 == 0, list1))
print(result3)  # [2, 4, 6, 8]


from functools import reduce
result4 = reduce(lambda x, y: x + y, list1)
print(result4)  # 36

print(sorted(list1, reverse=True))  # [8, 7, 6, 5, 4, 3, 2, 1]

L = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
print(sorted(L, key=lambda x: x[1]))  # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(sorted(students, key=lambda s: s[2]))  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

