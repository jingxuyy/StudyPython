
"""
    字符串是一个序列，由多个字符元素组成
    现在如果需要用一个序列存储一些不同的自行车：trek, cannondale, redline, specialized
    使用字符串存储：
        bicycles = 'trekcannondaleredlinespecialized'
    此时如果需要打印trek必须要要对字符串进行切片，非常麻烦，而且字符串是不可变数据类型，无法真正的增加和删除

    而 列表 这一数据类型能够很好的解决这个问题
    列表的声明方式：
        使用一对中括号包裹，每个元素之间使用逗号隔开
            变量名 = [元素1, 元素2, 元素3, ......, 元素n]
        例如：
            bicycles = ['trek', 'cannondale', 'redline', 'specialized']
        列表里的元素可以是任何其它数据类型

    列表的性质：
        - 1. 列表是序列，可以存储多个元素
        - 2. 列表是有序的，因此，列表和字符串一样存在下标，第一个元素对应下标为0，第二个为1，......
        - 3. 列表是可变数据类型，因此，可以在列表本身进行修改
        - 4. 将同一个列表赋值给两个变量，任何变量对列表修改都会影响到另一个
            例如：
                a = [1,2,3]
                b = a
                此时，如果对b进行增删，a也会跟着改变，因为 a和b都是指向同一个列表
                若：
                a = [1,2,3]
                b = [1,2,3]
                此时 a,和b没有关联

    列表切片：
        序列+有序 = 元素有下标 = 可以切片  切片规则 和字符串切片规则相同


    增删改查：

        查：
            1. 根据下标直接查询
                列表名[下标]
                例如：
                    name_list = ['Tom', 'Lily', 'Rose']
                    print(name_list[0])  # Tom
                    print(name_list[1])  # Lily
                    print(name_list[2])  # Rose

            2. index(sub, start=None, end=None) 和字符串查找的index相同，查找到则返回对应下标，否则报错
                例如：
                    print(name_list.index('Lily'))  # 1

            3. count(元素)  统计 元素 在列表中出现的次数
                例如：
                    print(name_list.count('Lily'))  # 1

            4. len(列表)  返回列表的元素个数，即列表长度
                例如：
                    print(len(name_list))  # 3


        增： 注意列表是可变数据类型，因此增加会在原始的列表上增加元素
            1. append(元素)  在列表末尾增加元素
                例如：
                    name_list.append('xiaoming')
                    print(name_list)  # 结果：['Tom', 'Lily', 'Rose', 'xiaoming']
                注意：append给列表增加元素时，会将传入的参数只当作一个元素，添加到原列表末尾
                    例如：
                        name_list.append(['xiaofang', 'xiaohong'])
                        print(name_list)  # ['Tom', 'Lily', 'Rose', 'xiaoming', ['xiaofang', 'xiaohong']]
                    从结果可以看到，将['xiaofang', 'xiaohong']这个列表使用append加入到原列表，会当作原列表的一个元素，只不过这个元素是一个列表罢了

            2. extend(序列)：列表结尾追加数据，如果数据是⼀个序列，则将这个序列的数据逐⼀添加到列表。
                例如：
                    name_list = ['Tom', 'Lily', 'Rose']
                    name_list.extend('xiaoming')
                    print(name_list)  # 结果：['Tom', 'Lily', 'Rose', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g']
                    name_list.append(['xiaofang', 'xiaohong'])
                    name_list.append(['xiaofang', 'xiaohong'])
                    print(name_list)  # ['Tom', 'Lily', 'Rose', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g', ['xiaofang', 'xiaohong']]
                字符串也是序列，由一个个字符组成，extend会将字符串这个序列拆开加入到原列表
                而列表['xiaofang', 'xiaohong']是一个序列，extend会将这个列表序列拆开得到一个个元素（字符串）再加入到原列表中
                extend函数添加时，对序列只会拆开一次，得到其元素再逐个加入

                因此如果想添加元素到列表中，若不想拆开添加，则使用append函数，否则使用extend函数

            3. insert(下标，数据)：指定位置新增数据。
                例如：
                    name_list = ['Tom', 'Lily', 'Rose']
                    name_list.insert(1, 'xiaoming')
                    print(name_list)  # ['Tom', 'xiaoming', 'Lily', 'Rose']
                和 append相同，只不过 insert可以指定位置


        删：
            1. pop()：删除指定下标的数据(默认为最后⼀个)，并返回该数据。
                例如：
                    name_list = ['Tom', 'Lily', 'Rose']
                    del_name = name_list.pop(1)
                    print(del_name)  # 结果：Lily
                    print(name_list)  # 结果：['Tom', 'Rose']
                    print(name_list.pop())  # Rose
                    print(name_list)  # ['Tom']
                pop函数在不指定删除哪个位置的情况下，默认删除最后一个元素，并且pop函数的返回值就是被删除的元素

            2. remove(元素)：移除列表中某个数据的第⼀个匹配项。
                例如：
                    name_list = ['Tom', 'Lily', 'Rose']
                    name_list.remove('Rose')
                    print(name_list)  # 结果：['Tom', 'Lily']
                remove是根据值删除列表中的元素，没有返回值, 如果想要删除的值不存在于列表中，则报错

            3. clear()：清空列表
                例如：
                    name_list.clear()
                    print(name_list)  # []
                相当于删除列表中的所有元素，只剩下一个空列表


        改：
            1. 根据列表下标修改元素
                例如：
                    name_list = ['Tom', 'Lily', 'Rose']
                    name_list[0] = 'aaa'
                    print(name_list)  # 结果：['aaa', 'Lily', 'Rose']

            2. reverse() 原地反转
                例如：
                    num_list = [1, 5, 2, 3, 6, 8]
                    num_list.reverse()
                    print(num_list)  # 结果：[8, 6, 3, 2, 5, 1]
                这里原地反转，就是修改了原本列表

            3. sort(key=None, reverse=False) 排序
                参数 key 目前用不到
                参数 reverse 默认值是False表示，列表里的元素按照升序排序，若是True则是倒序排序
                例如：
                    num_list = [1, 5, 2, 3, 6, 8]
                    num_list.sort()  # 结果：[1, 2, 3, 5, 6, 8]
                    print(num_list)
                    num_list.sort(reverse=True)
                    print(num_list)  # [8, 6, 5, 3, 2, 1]

            4. copy() 复制
                例如：
                    name_list = ['Tom', 'Lily', 'Rose']
                    name_li2 = name_list.copy()
                    print(name_li2)  # 结果：['Tom', 'Lily', 'Rose']

        判断：
            1. in 判断存在
                例如：
                    name_list = ['Tom', 'Lily', 'Rose']
                    print('Lily' in name_list)  # 结果：True
                    print('Lilys' in name_list)  # 结果：False

            2. not in 判断不存在
                例如：
                    name_list = ['Tom', 'Lily', 'Rose']
                    print('Lily' not in name_list)  # 结果：False
                    print('Lilys' not in name_list)  # 结果：True



    可变与不可变类型一点区别：
       - 1. a = 'abc'
            b = a
            此时改变b
            b = 'ccc'
            输出：
            print(a)      --------------> abc
            print(b)      --------------> ccc
            可以看见，修改b不会影响a

       - 2. a = ['aa', 'bb', 'cc']
            b = a
            此时改变b
            b[0] = 'dd'
            输出：
            print(a)    --------------> ['dd', 'bb', 'cc']
            print(b)    --------------> ['dd', 'bb', 'cc']
            可以看见，修改b会影响到a


    列表遍历：
        - 1. for循环遍历
            name_list = ['Tom', 'Lily', 'Rose']
            for name in name_list:
                print(name, end=" ")  # Tom Lily Rose

        - 2. while循环遍历
            i = 0
            while i < len(name_list):
                print(name_list[i], end=" ")  # Tom Lily Rose
                i += 1


    列表嵌套：
        列表里的元素可以其它任何数据类型，所以列表元素可以是数字，字符串，列表，以及后面学到的其它数据类型
        例如：
            name_list = [['⼩明', '⼩红', '⼩绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四','王五']]
            a = name_list[0]
            b = name_list[1]
            c = name_list[2]
            列表name_list中的元素是列表，注意，此时取出来的元素a、b、c任然是列表即可，其它按照列表操作即可

    创建纯数字列表：
        使用range()函数
        range(start, end, step)
            start 开始
            end   结束
            step  步长
        会产生一个序列，这个序列里都是数字，第一个数字是 start， 第二个是 start+step，......， 注意最终序列里不包含 end 数字，左闭右开
        step默认值是1
        start默认值是0

        range函数返回值类型是一个类（这个知识点后面会讲解） 可以直接使用for循环遍历，当作列表使用
        也可以使用 list()函数将range()函数返回值直接转成列表
        type(list(range(1,10)))      ----------------> list

    列表算术运算：
        - 1. 加法  [1, 2, 3] + [4, 5, 6] = [1, 2, 3, 4, 5, 6]
        - 2. 乘法  [1, 2, 3] * 3 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        和字符串相同




    列表总结：
        - 1. 形式：
            [元素1, 元素2, ......, 元素n]
            多个元素使用逗号隔开，每个元素可以是不同的数据类型
            在没有特殊需求情况下，同一个列表里的元素应该都是同一个数据类型

        - 2. 性质：
            1. 是一个序列
            2. 有序-->有下标
            3. 可以切片 列表[::-1] 反转
            4. 是可变数据类型，可以对原始列表进行增删

        - 3. 常用函数，增删改查
            1. 查：
                1.1 根据下标查询元素
                    列表名[下标]
                1.2 根据元素查询下标
                    列表名.index(元素)
                1.3 统计元素出现的次数
                    列表名.count(元素)
                1.4 统计列表长度
                    len(列表)
            2. 增：
                2.1 在末尾增加元素
                    append(元素)
                2.2 在末尾添加序列，并将序列中每个元素添加到列表
                    extend(序列)
                2.3 在任意位置添加元素
                    insert(下标，元素)
            3. 删：
                3.1 删除指定下标元素
                    pop() 或者  pop(下标)
                    pop会将删除的元素返回
                3.2 根据元素删除列表里相同的元素
                    remove(元素)
                3.3 清空列表
                    clear()
            4. 改：
                4.1 根据下标修改元素
                    列表名[下标] = 元素
                4.2 列表原地反转
                    reverse()
                4.3 列表元素原地排序
                    sort(reverse=False)  升序
                    sort(reverse=True)   降序
                4.4 复制
                    copy()
        - 4. 列表遍历：
            1. for循环遍历
            2. while循环遍历
        - 5. 创建纯数字列表
            list(range(n))
        - 6. 列表算术运算：
            1. 加法
            2. 数乘
        - 7. 列表判断
            1. in 判断存在
            2. not in 判断不存在



"""

name_list = ['Tom', 'Lily', 'Rose']
print(name_list[0])  # Tom
print(name_list[1])  # Lily
print(name_list[2])  # Rose

print(name_list.index('Lily'))  # 1
print(name_list.count('Lily'))  # 1
print(len(name_list))  # 3

name_list.append('xiaoming')
print(name_list)  # 结果：['Tom', 'Lily', 'Rose', 'xiaoming']

name_list.append(['xiaofang', 'xiaohong'])
print(name_list)  # ['Tom', 'Lily', 'Rose', 'xiaoming', ['xiaofang', 'xiaohong']]


name_list = ['Tom', 'Lily', 'Rose']
name_list.extend('xiaoming')
print(name_list)  # 结果：['Tom', 'Lily', 'Rose', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g']
name_list.append(['xiaofang', 'xiaohong'])
print(name_list)  # ['Tom', 'Lily', 'Rose', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g', ['xiaofang', 'xiaohong']]

name_list = ['Tom', 'Lily', 'Rose']
name_list.insert(1, 'xiaoming')
print(name_list)  # ['Tom', 'xiaoming', 'Lily', 'Rose']


name_list = ['Tom', 'Lily', 'Rose']
del_name = name_list.pop(1)
print(del_name)  # 结果：Lily
print(name_list)  # 结果：['Tom', 'Rose']
print(name_list.pop())  # Rose
print(name_list)  # ['Tom']


name_list = ['Tom', 'Lily', 'Rose']
name_list.remove('Rose')
print(name_list)  # 结果：['Tom', 'Lily']

name_list.clear()
print(name_list)  # []

name_list = ['Tom', 'Lily', 'Rose']
name_list[0] = 'aaa'
print(name_list)  # 结果：['aaa', 'Lily', 'Rose']


num_list = [1, 5, 2, 3, 6, 8]
num_list.reverse()
print(num_list)  # 结果：[8, 6, 3, 2, 5, 1]

num_list = [1, 5, 2, 3, 6, 8]
num_list.sort()  # 结果：[1, 2, 3, 5, 6, 8]
print(num_list)
num_list.sort(reverse=True)
print(num_list)  # [8, 6, 5, 3, 2, 1]


name_list = ['Tom', 'Lily', 'Rose']
name_li2 = name_list.copy()
print(name_li2)  # 结果：['Tom', 'Lily', 'Rose']


name_list = ['Tom', 'Lily', 'Rose']
print('Lily' in name_list)  # 结果：True
print('Lilys' in name_list)  # 结果：False

name_list = ['Tom', 'Lily', 'Rose']
print('Lily' not in name_list)  # 结果：False
print('Lilys' not in name_list)  # 结果：True


name_list = ['Tom', 'Lily', 'Rose']
for name in name_list:
    print(name, end=" ")  # Tom Lily Rose

print()

i = 0
while i < len(name_list):
    print(name_list[i], end=" ")  # Tom Lily Rose
    i += 1

print()

list










