
"""
    在Python中运算符分为：
        - 1. 算术运算符
        - 2. 赋值运算符
        - 3. 复合赋值运算符
        - 4. 比较运算符
        - 5. 逻辑运算符

    1. 算术运算符：即数学运算
        运算符         描述          实例
          +            加            1 + 1 输出结果为 2
          -            减            1-1 输出结果为 0
          *            乘            2 * 2 输出结果为 4
          /            除            10 / 2 输出结果为 5
          //          整除           9 // 4 输出结果为2
          %           取余           9 % 4 输出结果为 1
          **          指数           2 ** 4 输出结果为 16，即 2 * 2 * 2 * 2
          ()          ⼩括号         ⼩括号⽤来提⾼运算优先级，即 (1 + 2) * 3 输出结果为 9

        算术运算符 除法有三种：
            - 除 / 这个就是算术正常除法
            - 整除 // 这个是除法后只保留商
            - 取余 % 这个是除法后只保留余数
        注意：
            只要涉及除法，其结果都是浮点数

    2. 赋值运算符
        运算符         描述          实例
          =            赋值       将 = 右侧的结果赋值给等号左侧的变量

        赋值可以：
            - 单变量赋值，一次给一个变量赋值
            - 多变量不等赋值，一次给多个变量赋值，且每个变量值不必相同
            - 多变量相等赋值， 一次给多个变量赋值，每个变量值相等

            例如：
                # 单变量赋值
                num = 1

                # 多变量不等赋值
                a = b = 10

                # 多变量不等赋值
                num1, float1, str1 = 10, 0.5, 'hello world'

    3. 复合赋值运算符
        运算符                 描述              实例
          +=            加法赋值运算符     c += a 等价于 c = c + a
          -=            减法赋值运算符     c -= a 等价于 c = c- a
          *=            乘法赋值运算符     c *= a 等价于 c = c * a
          /=            除法赋值运算符     c /= a 等价于 c = c / a
          //=           整除赋值运算符     c //= a 等价于 c = c // a
          %=            取余赋值运算符     c %= a 等价于 c = c % a
          **=           幂赋值运算符      c ** = a 等价于 c = c ** a

        就是把，赋值和算术运算符结合起来，注意：先算术再赋值

    4. 比较运算符
        运算符                                     描述                                                          实例
         ==             判断相等。如果两个操作数的结果相等，则条件结果为真(True)，否则条件结果为假(False)        如a=3,b=3，则（a == b) 为 True
        !=              不等于 。如果两个操作数的结果不相等，则条件为真(True)，否则条件结果为假(False)          如a=3,b=3，则（a == b) 为 True如a=1,b=3，则(a != b) 为 True
        >               运算符左侧操作数结果是否⼤于右侧操作数结果，如果⼤于，则条件为真，否则为假                   如a=7,b=3，则(a > b) 为 True
        <               运算符左侧操作数结果是否⼩于右侧操作数结果，如果⼩于，则条件为真，否则为假                   如a=7,b=3，则(a < b) 为 False
        >=              运算符左侧操作数结果是否⼤于等于右侧操作数结果，如果⼤于，则条件为真，否则为假             如a=7,b=3，则(a < b) 为 False如a=3,b=3，则(a >= b) 为 True
        <=              运算符左侧操作数结果是否⼩于等于右侧操作数结果，如果⼩于，则条件为真，否则为假             如a=3,b=3，则(a <= b) 为 True

        注意：比较运算符的结果是布尔类型bool  可以两个条件一起比较，例如   1<num<2

    5. 逻辑运算符
        运算符             逻辑表达式                               描述                                                  实例
        and               x and y       布尔"与"：如果 x 为 False，x and y 返回False，否则它返回 y 的值。          True and False， 返回False。
        or                x or y        布尔"或"：如果 x 是 True，它返回 True，否则它返回 y 的值。                  False or True， 返回True。
        not                not x        布尔"⾮"：如果 x 为 True，返回 False 。如果 x为 False，它返回 True。   not True 返回 False, not False 返回 True

    数字之间的逻辑运算：
        - and运算符，只要有⼀个值为0，则结果为0，否则结果为最后⼀个⾮0数字
        - or运算符，只有所有值为0结果才为0，否则结果为第⼀个⾮0数字
"""

# 单变量赋值
num = 1
print(num)

# 多变量不等赋值
a = b = 10
print(a)
print(b)

# 多变量不等赋值
num1, float1, str1 = 10, 0.5, 'hello world'
print(num1)
print(float1)
print(str1)



a = 100
a += 1
# 输出101 a = a + 1,最终a = 100 + 1
print(a)

b = 2
b *= 3
# 输出6 b = b * 3,最终b = 2 * 3
print(b)
c = 10
c += 1 + 2
# 输出13, 先算运算符右侧1 + 2 = 3， c += 3 , 推导出c = 10 + 3
print(c)


a = 7
b = 5
print(a == b)  # False
print(a != b)  # True
print(a < b)  # False
print(a > b)  # True
print(a <= b)  # False
print(a >= b)  # True


a = 1
b = 2
c = 3
print((a < b) and (b < c))  # True
print((a > b) and (b < c))  # False
print((a > b) or (b < c))  # True
print(not (a > b))  # True
