
"""
    字典数据类型使用频率和列表、字符串一样多
    字典也可以存储多个元素，但是和列表、元组不同的是，字典里的每个元素都是键值对形式，即 每个元素由两部分组成，key和value其中，key和value使用冒号隔开，多个元素使用逗号隔开
    字典使用一对大括号包裹，其形式：
        {key1 : value1, key2 : value2, ......, keyn : valuen}
    例如：
        dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
    字典里key和value可以是其他任意数据类型，但是，一般key都是不可变数据类型，一般使用字符串，value随意

    字典性质：
        - 1. 字典无序、无下标、不可切片
        - 2. 字典是可变数据类型，可增删查改
        - 3. 字典的key在同一个字典内不允许重复

    字典切片：
        由于字典没有下标，因此不可切片

    注意：字典里的key相当于下标，因此可以通过key获取对应的value

    增删改查：

        增： 字典元素是一个键值对，因此，新增就是增加一个键值对
            字典名[key] = value
            例如：
                dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
                dict1['id'] = 110
                print(dict1)  # {'name': 'Rose', 'age': 20, 'gender': '男', 'id': 110}

        删：
            1. del 字典名[key]
               例如：
                   del dict1['gender']
                   print(dict1)  # {'name': 'Tom', 'age': 20, 'id': 110}
            2. clear() 清空
                例如：
                    dict1.clear()
                    print(dict1)  # {}
        查：
            1. 通过key查找value
                字典名[key]
                例如：
                    dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
                    print(dict1['name'])  # Tom

            2. get(key, 默认值) 通过key在字典里查找value,如果没找到 默认返回None，也可以修改默认值，返回自定义默认值
                例如：
                    dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
                    print(dict1.get('name'))  # Tom
                    print(dict1.get('id', 110))  # 110
                    print(dict1.get('id'))  # None
            3. keys() 返回字典里所有的key组成的列表
                例如：
                    dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
                    print(dict1.keys())  # dict_keys(['name', 'age', 'gender'])
            4. values() 返回字典里所有value组成的列表
                例如：
                    print(dict1.values())  # dict_values(['Tom', 20, '男'])
            5. items() 返回字典里所有的键值对，返回的是一个列表，列表元素是元组，元组里的元素键值对
                例如：
                    print(dict1.items())  # dict_items([('name', 'Tom'), ('age', 20), ('gender', '男')])
            6. len(字典) 返回字典长度
                例如：
                    print(len(dict1))  # 3


        改：
            字典名[key] = value
            注意：当key在原字典里存在，就是修改，否则是新增操作
            例如：
                dict1['age'] = 22
                print(dict1)  # {'name': 'Tom', 'age': 22, 'gender': '男'}

        判断：
            1. in     判断 key 是否存在
            2. not in 判断 key 是否不存在

    字典遍历：
        同理既可以while循环遍历，也可以for循环遍历，但一般字典使用for遍历

        1. 遍历字典的key:
            dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
            for key in dict1.keys():
                print(key, end=" ")  # name age gender
        2. 遍历字典的value:
            for value in dict1.values():
                print(value, end=" ")  # Tom 20 男
        3. 遍历字典的键值对：
            for key, value in dict1.items():
                print(f"key={key},value={value}")
            # key=name,value=Tom
            # key=age,value=20
            # key=gender,value=男

    这里提一下：
        元组装包和拆包
        1. 装包：
            元组： ('a', 'b', 'c') 这是一个元组
            tuple1 = ('a', 'b', 'c')
            print(type(tuple1))  -------------> tuple

            如果 将多个分散的数据赋值给 一个 变量 那么 python 会自动装包  先将这些分散的数据放入到一个元组，然后将元组赋值给这个变量
            tuple2 = 'a', 'b', 'c'
            print(type(tuple2))  -------------> tuple

            装包就是自动将多个元素封装成元组

        2. 拆包：
            元组： ('a', 'b', 'c') 这是一个元组
            tuple1 = ('a', 'b', 'c')
            print(type(tuple1))  -------------> tuple

            如果将这个元组赋值给多个变量（是和元组里元素相同的个数） 那么 python 会将原元组拆开，按照顺序分别给多个变量一一赋值
            ch1, ch2, ch3 = ('a', 'b', 'c')
            print(ch1) -----------> a
            print(ch2) -----------> b
            print(ch3) -----------> c

            拆包就是将元组自动拆成多个元素赋值给多个变量

            例如：
                for key, value in dict1.items():
                    print(f"key={key},value={value}")
                使用了拆包，dict1.items()中每个元素都是元组，拆包赋值给了key, value

                如果不使用拆包
                for item in dict1.items():
                    print(f"key={item[0]},value={item[1]}")

        因此元组的拆包、装包能够给编程带来一定程度上的方便

    字典嵌套：
        和前面数据类型不同，字典嵌套会大量使用，非常适合存储有结构的数据例如：
            student_score = {
                "小米" : {"语文":77, "数学":66, "英语":33},
                "小芳" : {"语文":80, "数学":75, "英语":70},
                "小明" : {"语文":88, "数学":90, "英语":75},
            }
        只要知道每一次取出的元素类型是什么，就可以轻松操作


    字典总结：
        形式：每一个元素都是一个键值对，键值对之间使用冒号隔开
            {key1 : value1, key2 : value2, key3 : value3, ......, keyn : valuen}

        性质：
            1。 无序、无下标
            2. 不可切片
            3. 可变数据类型
            4. key不允许重复

        常用函数：增删查改：
            1. 增：
                字典名[key] = value
                要保证原字典不存在key，否则就是修改
            2. 改：
                字典名[key] = value
                要保证原字典存在key，否则就是新增
            3. 删：
                1. del 字典名[key]
                2. clear() 清空
            4. 查：
                1. 根据key查找value
                    字典名[key]
                2. get(key)
                    根据key查找value,如果不存在则返回None,可以修改默认返回值
                3. keys()
                    返回字典里所有的key组成列表
                4. values()
                    返回列表，列表的元素是字典里的所有value
                5. items()
                    返回列表，列表里元素是一个个元组，元组内容是字典元素的键值对
                6. len()
                    返回字典长度
            判断key：
                1. in      判断key是否存在字典里
                1. not in  判断key是否不存在字典里

        字典遍历：
            1. while遍历
            2. for遍历
            - 配合 keys()遍历 字典的所有key
            - 配合 values()遍历 字典的所有value
            - 配合 items()遍历 字典的所有键值对

        字典没有算术运算

        元组：
            1. 装包
            2. 拆包



"""


dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict1['id'] = 110
print(dict1)  # {'name': 'Rose', 'age': 20, 'gender': '男', 'id': 110}

del dict1['gender']
print(dict1)  # {'name': 'Tom', 'age': 20, 'id': 110}

dict1.clear()
print(dict1)  # {}

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1['name'])  # Tom

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.get('name'))  # Tom
print(dict1.get('id', 110))  # 110
print(dict1.get('id'))  # None

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.keys())  # dict_keys(['name', 'age', 'gender'])
print(dict1.values())  # dict_values(['Tom', 20, '男'])
print(dict1.items())  # dict_items([('name', 'Tom'), ('age', 20), ('gender', '男')])

dict1['age'] = 22
print(dict1)  # {'name': 'Tom', 'age': 22, 'gender': '男'}

print(len(dict1))  # 3


dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for key in dict1.keys():
    print(key, end=" ")  # name age gender
print()
for value in dict1.values():
    print(value, end=" ")  # Tom 20 男
print()
for key, value in dict1.items():
    print(f"key={key},value={value}")
# key=name,value=Tom
# key=age,value=20
# key=gender,value=男

