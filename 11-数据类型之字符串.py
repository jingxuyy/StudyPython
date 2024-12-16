
"""
    在Python中数据类型有：
        - 1. 整数
        - 2. 小数
        - 3. 布尔
        - 4. 字符串
        - 5. 列表
        - 6. 元组
        - 7. 集合
        - 8. 字典
    其中 整数、小数、布尔见名之意，且都是单个值，而 字符串、列表、元组、集合和字典都是序列，且都是用来存储多个元素

    字符串：
        在python中，字符串使用：
            - 1. 一对单引号
            - 2. 一对双引号
            - 3. 三对三引号 或者 三对双引号
            包含在一起的数据

            例如：
                str1 = 'This is a string.'
                print(type(str1))                      --------->  <class 'str'>
                str2 = "This is also a string."
                print(type(str2))                      --------->  <class 'str'>
                str3 = '''This is also a string.'''
                print(type(str3))                      --------->  <class 'str'>

            但是在Python一般使用一对双引号或者单引号来表示字符串，而三对单引号或者双引号是用来最为文档注释的

            注意：
                如果字符串本身内容就包含单引号，此时字符串应该使用双引号进行包裹，否则会造成错误
                    例如：
                        c = 'I'm Tom'  错误，Python只会进行配对，第一个单引号和第二个单引号配对成功，认为I是字符串，而最后一个单引号没有成功配对，报错
                        此时应该使用双引号：
                        c = "I'm Tom"
                同理，如果字符串本身有双引号，则使用单引号包裹

                不过如果在有单引号字符串里仍坚持使用单引号，也可以此时需要将字符串里本身单引号转义即可
                    例如：
                        c = 'I\'m Tom'    此时\'表示这个'只是一个'不起到字符串作用
                同理，如果字符串本身有双引号，坚持使用双引号，此时字符串本身里的双引号要转义

        字符串输出：就是之前的格式化输出，%s和f""
            注意：input()函数的结果是字符串

        这里提前提一下函数的一个基本知识：
            函数可以从结果返回分成两个类型：
                - 1. 有返回值函数
                    - 有返回值函数，指的是执行后会产生一个结果，可以使用变量来接收这个结果
                        例如之前学到的：type()函数，会返回数据类型  range(n)函数会返回一个序列  input()函数，会将用户输入的内容转成字符串返回
                - 2. 无返回值函数
                    - 无返回值函数，指的是函数执行后没有结果返回，也可以用变量接收，不过值永远是 None没有任何作用
                        例如：print()函数，默认在控制台打印输出信息

        字符串是一个序列，因为是序列说明字符串是多个数据组合在一起的
            字符串是一个个字符组在一起的
            例如： str = Python    字符串str是由 P y t h o n按顺序组合在一起的

        字符串特点1：
            - 有序：即有左右顺序，例如Python，P永远在y的前面......
            正因为字符串有序，所以字符串存在下标（索引）
            字符串下标从左到右是从0开始的，例如字母P的下标是0，y的下标是1，......

            因为字符串有序，所以存在下标，所以可以根据下标取元素，（元素：指的是序列中的基本单位，在英语单词里就是字母等、汉字就是一个字）
            格式：
                字符串变量名[下标] 或者 字符串[下标]
                例如：
                    打印字符串Python中下标为0和3的字符串（Python语法中没有单个字符一说，因此单个字符仍然是字符串）
                    str6 = 'Python'
                    print(str6[0])
                    print(str6[3])

            字符串有序，所以有下标，所以可以进行切片操作

            注意：字符串切片操作是非常重要的操作：
            切片是指：从原字符串中获取指定位置，长度的子字符串
            格式：
                字符串变量名[开始下标:结束下标:步长] 或者 字符串[开始下标:结束下标:步长]
            例如：
                在str6 = 'Python' 字符串中获取子字符串 'yth' 并打印
                print(str6[1:4:1])

            注意：[开始下标:结束下标:步长] 其中包括开始下标的元素不包括结束下标的元素，也就是左闭右开区间
            一些情况：
                - 1. [开始下标:结束下标:步长] 当
                                            开始下标=0
                                            结束下标=字符串长度
                                            步长=1
                                         时 开始下标、结束下标、步长都可以省略，即 字符串变量名[::] 即获得的子字符串和原字符串一样
                    print(str6[::])  ------------> Python

                - 2. [开始下标:结束下标:步长] 当
                                            步长=1
                                          :步长 可以省略，因为默认步长为1 也就是 字符串变量名[开始下标:结束下标:步长] 和 字符串变量名[开始下标:结束下标] 效果一样
                    print(str6[1:4])  ------------> yth
                    print(str6[1:4:1])  ------------> yth

                - 3. [开始下标:结束下标:步长] 当
                                            开始下标=0
                                          开始下标 可以省略，开始下标默认值为1 也就是 字符串变量名[:结束下标:步长] 和 字符串变量名[开始下标:结束下标] 效果一样
                    print(str6[:4])  ------------> Pyth
                    print(str6[0:4])  ------------> Pyth

                - 4. [开始下标:结束下标:步长] 当
                                            结束下标=字符串长度
                                          结束下标 可以省略，结束下标默认值是字符串长度，也就是会取到字符串末尾  字符串变量名[开始下标:] 和 字符串变量名[开始下标:结束下标] 效果一样
                    print(str6[2:6])  ------------> thon
                    print(str6[2:])  ------------> thon

                即：
                    当切片时，需要从下标0开始，则 开始下标 可以省略；如果要切片到最后，则 结束下标 可以省略；如果切片的步长是1，则 :步长 可以省略

            步长：默认值是1，表示切片时每次增加1，
                例如
                    开始下标是1，结束下标是8则 切到的子字符串在原字符串的位置是 1，2，3，4，5，6，7
                若步长为2，则：
                    开始下标是1，结束下标是8则 切到的子字符串在原字符串的位置是 1，3，5，7
                    例如：
                        name = "ada lovelace"
                        print(name[1:8:1])  ------------> da love
                        print(name[1:8:2])  ------------> d oe
                    注意：在字符串里无论是空格还是其它都是字符串

                如果想取字符串最后一个字符子串：
                    - 1. print(name[11])  从左往右数下标，下标从0开始，所以最后一个元素下标就是 字符串总长度-1
                    - 2. print(name[-1])  或者从右往左数，注意从右往左数，第一个元素下标是 -1

                字符串下标从左往右下标依次是 0 1 2 3 .... 字符串长度-1
                字符串下标从右往左下标依次是 -1 -2 -3 -4 .... -字符串长度

                注意切片的依据是 开始下标 + 步长  ----> 结束下标  直到 开始下标 + 步长 的和等于 结束下标
                    如果 开始下标 > 结束下标 且 步长 > 0  则 开始下标 + 步长 的和永远不等于 结束下标 切片结果为 空
                    print(name[6:2]) ------------>

                由于 字符串有从左往右的下标，也有从右往左的下标，因此也可以使用 负数的开始下标，负数结束下标，步长进行切片
                    但两种切片都一样，这里不一一举例，
            切片总结：
                字符串变量名[开始下标:结束下标:步长] 或者 字符串[开始下标:结束下标:步长]
                这里的： 开始下标、结束下标、步长 既可以都是正数也可以都是负数，只需要保证一个条件：<<开始下标 + 步长 经过若干次相加 其值能够等于 结束下标>>

                提一下：[::-1] 的切片结果是将字符串倒序了
                    例如：
                         print(name)  ------------> ada lovelace
                         print(name[::-1]) ------------> ecalevol ada

    字符串是序列，且字符串有序  -----> 字符串有下标  ----->  字符串可以切片

            字符串特点2：
                字符串是不可变数据类型：
                    也就是，当声明一个字符串，则字符串就固定下来了，字符串里的内容是不可以改变的，上面说的切片，看起来是对原字符串进行了截取，但实质上每一次切片都生成了新的字符串，对原字符串没有影响

    序列的通用操作：增删改查
        - 1. 增：字符串新增操作，由于字符串是不可变数据类型，因此不能在原有字符串上进行新增操作，因此字符串没有增操作
        - 2. 删：字符串是不可变数据类型，不能对字符串里的元素进行删除，但是可以将整个字符串删除，这个稍后讲解
        - 3. 改：同理字符串是不可变数据类型，不能修改原本字符串，没有修改操作
        - 4. 查：字符串可以根据下标查元素，即上面讲解的 字符串[下标]  范围：0<= 下标 < 字符串长度  其它则程序报错

    由于字符串在程序开发中经常使用，而又因为其是不可变数据类型，不可以在原本字符串上操作，因此为了方便，字符串本身提供了很多方法用来 操作”修改“字符串，这些操作都是生成新的字符串

    查：
        - 1. find('子字符串') 函数：在 原字符串 查找 子字符串 的位置
            find(self, sub, start=None, end=None)
            其中：
                self 参数：这里不用管
                sub 表示要在原字符串查找的子字符串
                start=None 表示查找时在原字符串的开始位置（开始下标） 默认值为None表明从下标0开始查找
                end=None   表示查找时在原字符串的结束位置（结束下标） 默认值为None表明结束下标为字符串长度-1

            格式 :
                1. 原字符串.find('子字符串')
                2. 原字符串.find('子字符串', start=1)
                3. 原字符串.find('子字符串', end=3)
                4. 原字符串.find('子字符串', start=1, end=3)

            返回结果：
                1. 成功查到：
                    1）原字符串里只存在一个子字符串 返回子字符串在原字符串首个字符下标
                        例如：
                            name = 'ada lovelace'
                            print(name.find('ada'))  -------> 0   因为子字符串 'ada' 出现在name字符串里，且首个字符下标在原字符name下标为0 所以返回0
                            print(name.find('love')) -------> 4   'love' 出现在name字符串里，且首个字符下标在原字符name下标为4 所以返回4 （别忘了空格也是一个元素）
                    2）原字符串里存在多个子字符串 只返回子字符串在原字符串第一次出现时首个字符下标
                        例如：
                            print(name.find('a'))  -------> 0
                            print(name.find('l'))  -------> 4
                2. 没有查到（即不存在指定的子字符串），则返回 -1 表明没有：
                    例如：
                        print(name.find('adad'))  -------> -1
                        print(name.find('ll'))  -------> -1

            带有 start 和 end 参数的find函数使用同理，只不过起始和结束下标不同，不再演示

        - 2. index('子字符串')
            index(self, sub, start=None, end=None)
            此函数和上面 find函数功能和参数一模一样，只有一个不同点

            不同点：
                find函数查不到时返回值是 -1
                index函数查找不到时 程序会报错

                name = 'ada lovelace'
                print(name.index('adad'))  -------> ValueError: substring not found

        - 3. rfind('子字符串')  和find相同，不过会返回从左数第一个子字符串下标，也就是返回查找到 最后一次出现在原字符串的子字符串所在的下标
        - 4. rindex('子字符串') 同理

        - 5. count('子字符串')
            count(self, sub, start=None, end=None)
                参数和find同理
            作用：统计子字符串在原字符串出现的次数，没有则返回0
                例如：
                    print(name.count('a'))  -------> 3
                    print(name.count('love'))  -------> 1
                    print(name.count('abc'))  -------> 0


    改：虽说是改，其实都是生成新的字符串，而不是修改原字符串
        - 1. replace 函数：替换
            replace(self, old, new, maxreplace=-1)
            其中：
                old 表示原字符串里需要被替换的 旧子字符串
                new 表示用new表示的字符串将旧子字符串替换掉
                maxreplace 表示替换次数，默认替换所有相同的旧字符串

            格式：
                原字符串.find('旧子字符串', '新子字符串')
                原字符串.find('旧子字符串', '新子字符串', 次数)

            例如：
                print(name.replace('a', '**'))  -------> **d** lovel**ce
                print(name.replace('ada', 'bbb'))  -------> bbb lovelace
                print(name.replace('a', '**', 2))  -------> **d** lovelace
                print(name.replace('aaa', '**'))  -------> ada lovelace

            在原字符串没找到要被替换的旧字符串，则返回相同的原字符串

        - 2. split 函数：字符串分割，会将字符串按照给定的分割符 分割成列表存储
            split(分割字符, num)
                分割字符：可以指定，也可以不知道
                num：分割的次数

            格式：
                原字符串.split('分隔符字符串')

            例如：
                my_str = "hello world and java and C# and Python"

                # 结果：['hello world ', ' java ', ' C# ', ' Python']
                print(my_str.split('and'))

                # 结果：['hello world ', ' java ', ' C# and Python']
                print(my_str.split('and', 2))

                # 结果：['hello', 'world', 'and', 'java', 'and', 'C#', 'and', 'Python']
                print(my_str.split(' '))

                # 结果：['hello', 'world', 'and java and C# and Python'
                print(my_str.split(' ', 2))

            注意：指定的分隔符字符串不会存储到列表中，如果split函数中的分隔符也可以不指定，则会按照其自身规则进行分割

        - 3. join 函数：将序列按照给定的子字符串进行连接，形成一个字符串
            字符或⼦串.join(序列)
            其中：
                字符或⼦串 指的是连接的子字符串
                序列：序列

            例如：
                这里使用列表举例
                split_str_list = ['hello', 'world', 'and', 'java', 'and', 'C#', 'and', 'Python']

                print(''.join(split_str_list))    -------> helloworldandjavaandC#andPython
                print(' '.join(split_str_list))    -------> hello world and java and C# and Python
                print('**'.join(split_str_list))    -------> hello**world**and**java**and**C#**and**Python

            相当于将其它序列转成了字符串

        - 4. 大小写转换函数：（中文没有大小写，对中文不起作用）
            - capitalize() 将字符串里第一个单词的字母大写， 其它字母转成小写
            - title() 将字符串每个单词⾸字⺟转换成⼤写。 其它不变
            - lower() 将字符串中⼤写转⼩写。
            - upper() 将字符串中⼩写转⼤写。

            例如：
                my_str = "hello world and java and C# and Python"

                print(my_str.capitalize())    -------> Hello world and java and c# and python
                print(my_str.title())    -------> Hello World And Java And C# And Python
                print(my_str.upper())    -------> HELLO WORLD AND JAVA AND C# AND PYTHON
                print(my_str.lower())    -------> hello world and java and c# and python

            像网页登录要求输入验证码，不区分大小写，就可以使用 upper或者lower将用户输入的字符串转成都转成大写或者小写 再比较






"""

# 单引号
str1 = 'This is a string.'
print(type(str1))  # <class 'str'>
# 双引号
str2 = "This is also a string."
print(type(str2))  # <class 'str'>
# 三对单引号
str3 = '''This is also a string.'''
print(type(str3))  # <class 'str'>
# 三对双引号
str4 = """This is also a string."""
print(type(str4))  # <class 'str'>

# 使用转义
str5 = 'I\'m Tom'
print(str5)  # <class 'str'>

# 有返回值函数
object_type = type(str5)
print(object_type)  # I'm Tom

# 无返回值函数
result = print('没有返回值')
print(result)  # None

# 打印字符串Python中下标为0和3的字符串（Python语法中没有单个字符一说，因此单个字符仍然是字符串）
str6 = 'Python'
print(str6[0])  # P
print(str6[3])  # h

# 在str6 = 'Python' 字符串中获取子字符串 'yth' 并打印
print(str6[1:4:1])  # yth

print(str6[::])  # Python

print(str6[1:4])  # yth
print(str6[1:4:1])  # yth

print(str6[:4])  # Pyth
print(str6[0:4])  # Pyth

print(str6[2:6])  # thon
print(str6[2:])  # thon

name = "ada lovelace"
print(name[1:8:1])  # da love
print(name[1:8:2])  # d oe
print(name[11])  # e
print(name[-1])  # e

print(name[6:2])  #

print(name)  # ada lovelace
print(name[::-1])  # ecalevol ada

print(name[:-1])  # ada lovelac
print(name[-4:-1])  # lac
print(name[::-1])  # ecalevol ada

print(name.find('ada'))  # 0
print(name.find('love'))  # 4
print(name.find('a'))  # 0
print(name.find('l'))  # 4

print(name.find('adad'))  # -1
print(name.find('ll'))  # -1

print(name.index('love'))  # 4
# print(name.index('adad'))  # ValueError: substring not found

print(name.count('a'))  # 3
print(name.count('love'))  # 1
print(name.count('abc'))  # 0

print(name.replace('a', '**'))  # **d** lovel**ce
print(name.replace('ada', 'bbb'))  # bbb lovelace
print(name.replace('a', '**', 2))  # **d** lovelace
print(name.replace('aaa', '**'))  # ada lovelace


my_str = "hello world and java and C# and Python"
# 结果：['hello world ', ' java ', ' C# ', ' Python']
print(my_str.split('and'))

# 结果：['hello world ', ' java ', ' C# and Python']
print(my_str.split('and', 2))

# 结果：['hello', 'world', 'and', 'java', 'and', 'C#', 'and', 'Python']
print(my_str.split(' '))

# 结果：['hello', 'world', 'and java and C# and Python'
print(my_str.split(' ', 2))

print(my_str.split())

split_str_list = ['hello', 'world', 'and', 'java', 'and', 'C#', 'and', 'Python']
print(''.join(split_str_list))  # helloworldandjavaandC#andPython
print(' '.join(split_str_list))  # hello world and java and C# and Python
print('**'.join(split_str_list))  # hello**world**and**java**and**C#**and**Python

print(my_str.capitalize())  # Hello world and java and c# and python
print(my_str.title())  # Hello World And Java And C# And Python
print(my_str.upper())  # HELLO WORLD AND JAVA AND C# AND PYTHON
print(my_str.lower())  # hello world and java and c# and python



