"""
    集合也是一个序列，能够存放多个元素，和元组相同，操作比较少

    集合最大特点：
        集合里的元素不允许重复

    格式：
        {元素1, 元素2, ......, 元素n}
        使用一对大括号包裹，元素之间使用逗号隔开，字典也是使用一对大括号，不过字典里的元素是键值对形式
        例如：
            s1 = {10, 20, 30, 40, 50}

    注意：
        声明空的字符串：    1. ''  2. str()
        声明空的列表：      1. []  2. list()
        声明空的元组：      1. ()  2. tuple()
        声明空的字典：      1. {}  2. dict()
        声明空的集合：                set()

    声明空的集合需要使用set()函数，因为使用{}声明，默认是字典

    集合性质：
        1. 无下标、无序
        2. 可变数据类型
        3. 数据元素不重复

    集合切片：
        无序、无下标 不能切片

    增删查改：

        增：
            1. add(元素) 增加一个元素
                例如：
                    s1 = {10, 20}
                    s1.add(100)
                    s1.add(10)
                    print(s1)  # {100, 10, 20}
                注意：集合无序，每次打印顺序都可能不一样
            2. update(序列) 增加序列，不可以是单个元素
                例如：
                    s1 = {10, 20}
                    s1.update([100, 200])
                    s1.update('abc')
                    print(s1)  # {'c', 100, 200, 10, 'a', 20, 'b'}

        删：
            1. remove(元素)
                例如：
                    s1 = {10, 20}
                    s1.remove(10)
                    print(s1)  # {20}
            2. discard(元素) 元素不存在不报错
                例如：
                    s1 = {10, 20}
                    s1.discard(10)
                    print(s1)  # {20}
                    s1.discard(10)
                    print(s1)  # {20}
            3. pop() 随机删除一个元素，并且返回这个元素
                例如：
                    s1 = {10, 20, 30, 40, 50}
                    del_num = s1.pop()
                    print(del_num)  # 50
                    print(s1)  # {20, 40, 10, 30}

        查：
            集合没有下标，无序，且没有像字典那样的key所以不能查找

        判断：
            1. in     存在
            2. not in 不存在

    集合也可以做数学上的集合运算
        集合
        s2 = {1, 2, 3, 5}
        s3 = {1, 5, 7, 9}

        1. 集合并集：s2.union(s3)  s2.update(s3)  或者 使用 |
            print(s2.union(s3))  # {1, 2, 3, 5, 7, 9}
            注意：union会生成一个新的集合，update会在原集合上修改

        2. 集合交集 intersection()      或者使用 &
            print(s2.intersection(s3))  # {1, 5}

        3. 集合差集 s2.difference(s3)   或者 -
            print(s2.difference(s3))  # {2, 3}

    集合遍历：
        只能for循环遍历，因为没有下标
        for num in s2:
            print(num, end=" ")  # 1 2 3 5









"""

s1 = {10, 20}
s1.add(100)
s1.add(10)
print(s1)  # {100, 10, 20}

s1 = {10, 20}
s1.update([100, 200])
s1.update('abc')
print(s1)  # {'c', 100, 200, 10, 'a', 20, 'b'}

s1 = {10, 20}
s1.remove(10)
print(s1)  # {20}

s1 = {10, 20}
s1.discard(10)
print(s1)  # {20}
s1.discard(10)
print(s1)  # {20}

s1 = {10, 20, 30, 40, 50}
del_num = s1.pop()
print(del_num)  # 50
print(s1)  # {20, 40, 10, 30}

s2 = {1, 2, 3, 5}
s3 = {1, 5, 7, 9}
print(s2.union(s3))  # {1, 2, 3, 5, 7, 9}
print(s2.intersection(s3))  # {1, 5}
print(s2.difference(s3))  # {2, 3}

for num in s2:
    print(num, end=" ")  # 1 2 3 5
print()


