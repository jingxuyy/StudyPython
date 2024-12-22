
"""
    列表数据类型克服了字符串类型不易操作问题，接下来讲解第三个存储多个元素的数据类型：元组
    解决场景：
        需要一个容器存储多个元素，但是不允许修改，但是容易获取、查看等操作：
            首先想到字符串，但是字符串获取元素只能一个一个字符获取，不是很方便，
            因此产生了元组

    元组：
        ⼀个元组可以存储多个数据，元组内的数据是不能修改的。
    格式：
        使用一对小括号包裹元素，多个元素之间使用逗号隔开
        (元素1, 元素2, ......, 元素n)


    元组的性质:
        - 1. 元组是序列可以存储多个元素
        - 2. 元组是有序的，因此，列表一样存在下标，第一个元素对应下标为0，第二个为1，......
        - 3. 元组是不可变数据类型，因此不能对元组本身进行增删改操作

    元组切片：
        序列+有序 = 元素有下标 = 可以切片  切片规则 和列表切片规则相同


    增删改查：

        增：元组是不可变数据类型，无新增操作

        删：元组是不可变数据类型，无删除操作

        改：元组是不可变数据类型，无修改操作

        查：
            1. 根据下标查询元素
                元组名[下标]
                    例如：
                        tuple1 = ('aa', 'bb', 'cc', 'bb')
                        print(tuple1[0])  # aa
            2. 根据元素查找下标
                index(元素)
                    例如：
                        print(tuple1.index('aa'))  # 0
            3. 统计某个元素出现的次数
                count(元素)
                    例如：
                        print(tuple1.count('bb'))  # 2
            4. 统计元组里元素的个数，也就是元组的长度
                len(元组)
                    例如：
                        print(len(tuple1))  # 4

        判断： 和列表相同
            1. in 存在
            2. not in 不存在

    因为元组也是序列容器，因此，其元素也可以是其他数据类型，例如 数字、字符串、列表、元组 以及后面学习的其它数据类型
        (1, 1.2, 'python', [1,2,3], (11,23))
    如果元组的某个元素是可变数据类型，那么这个元素是可以改变的：
        例如：
            tuple2 = ('python', 'java', 'c', [1, 2, 3])
            print(tuple2)  # ('python', 'java', 'c', [1, 2, 3])
            tuple2[3].append(100)
            print(tuple2)  # ('python', 'java', 'c', [1, 2, 3, 100])
            tuple2[3].remove(2)
            print(tuple2)  # ('python', 'java', 'c', [1, 3, 100])
        此时元组tuple2的最后一个元素是可变数据类型列表，可以正常对这个列表进行增删改，但是不能删除这个列表
        因为这个列表是tuple2里的元素，而tuple2是不可变数据类型，其元素不可增删改，删除就违反了不可删
        而tuple2的最后一个元素看起来是可以增删改，其实这是因为最后一个元素是列表，是列表本身的性质
        从元组角度看 这个列表的增删改，列表增加了元素，列表是可变数据类型，所以增加是在原本列表增加元素，所以在元组角度来看，最后一个元素是列表，任然是之前的列表，删除、修改同理


    注意：
        声明一个元素的字符串：'a'
        声明一个元素的列表：['a']
        声明一个元素的元组：('a', )
    在声明一个元素的元组时，一定要在末尾写上逗号，否则 ('a')会被python识别为算术运算的括号
        例如：
            print(type(('a')))  # <class 'str'>
            print(type(('a',)))  # <class 'tuple'>


    元组的算术运算：
        1. 加法： 两个元组相加，将进行合并生成一个新的元组
        2. 数乘： 相当于多个加法

    遍历：
        1. for循环遍历
        2. while循环遍历


    元组总结：
        形式： (元素1, 元素2, ......, 元素n)
        单个元素的元素 (元素, )
    性质：
        1. 有序有下标，可切片
        2. 是不可变数据类型
    常用函数：增删改成
        增删改：无
        查：
            1. 根据下标查询元素
                元组名[下标]

            2. 根据元素查找下标
                index(元素)

            3. 统计某个元素出现的次数
                count(元素)

            4. 统计元组里元素的个数，也就是元组的长度
                len(元组)
        判断：
            1. in
            2. not in
        算术运算：
            1. 加法
            2. 数乘
        遍历：
            1. for循环遍历
            2. while循环遍历



"""

tuple1 = ('aa', 'bb', 'cc', 'bb')
print(tuple1[0])  # aa
print(tuple1.index('aa'))  # 0
print(tuple1.count('bb'))  # 2
print(len(tuple1))  # 4

tuple2 = ('python', 'java', 'c', [1, 2, 3])
print(tuple2)  # ('python', 'java', 'c', [1, 2, 3])
tuple2[3].append(100)
print(tuple2)  # ('python', 'java', 'c', [1, 2, 3, 100])
tuple2[3].remove(2)
print(tuple2)  # ('python', 'java', 'c', [1, 3, 100])

print(type(('a')))  # <class 'str'>
print(type(('a',)))  # <class 'tuple'>


