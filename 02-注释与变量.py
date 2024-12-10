
"""
    注释：
    1. 在程序中对某些代码进⾏标注说明，这就是注释的作⽤，能够⼤⼤增强程序的可读性。
    2. 注释仅提供给程序员代码信息，不参与代码运行
    3. 注释的分类：
        - 1. 单行注释：表示当前从注释起始位置到本行结束均是注释内容
            使用 # 表示注释开始 # 后面的内容均是注释
            例如：
            # 这是一个单行注释
        - 2. 多行注释：字面意思
            - 1. 使用三对单引号表示多行注释，''' '''里面内容均是注释
            - 2. 使用三对双引号表示多行注释，""" """ 里面内容均是注释
"""

# 单行注释，用于解释下一行或者下一个代码块的作用
print("上面是单行注释")

print("单行注释也可以写在代码后面")  # 这也是单行注释，用于解释当前这一行代码的作用


'''
这是使用三对单引号的多行注释，一般用于解释，下面多行代码或者代码块的作用
'''
print("上面是使用单引号的多行注释")


"""
这是使用三对双引号的多行注释，一般用于解释，下面多行代码或者代码块的作用
"""
print("上面是使用双引号的多行注释")



"""
    变量： 变量是用来存储单个数据信息的，方便后续代码使用
        1. 变量拥有变量名和值
            - 变量名：是程序员起的名字，值是指存储的数据
        2. 变量的命名和使用：
            - 1. 变量命名规则：
                - 1. 由数字、字⺟、下划线组成
                - 2. 不能数字开头
                - 3. 不能使⽤内置关键字
                - 4. 严格区分⼤⼩写
            - 2. 命名习惯（尽量遵守）
                - 1. 见名知意
                - 2. 大驼峰命名：变量名是多个单词组成时，每个单词首字母大写
                - 3. 小驼峰命名：变量名是多个单词组成时，第一个单词首字母小写，其余每个单词首字母大写
                - 4. 下划线命名：变量名是多个单词组成时，每个单词之间使用下划线隔开
            -3. 变量的使用：
                - 赋值：形式   变量名=值   即将右边的值赋值给左边的变量
            
"""

# 声明变量message并赋值
message = "Hello Python Crash Course world!"
print(message)
# 多个单词命名（大驼峰，小驼峰，下划线）
UserName = "吴姗姗"
userName = "吴姗姗"
user_name = "吴姗姗"

"""
    Python的数据类型：
        将一个数据赋值给一个变量，则数据是什么类型，则变量即为什么类型
        
        - 1. 数值：
            - 1. 整型：int 即 1， 2， 3， 4， ......
            - 2. 浮点数：float 即（广义上数学里的小数） 1.1， 0.2， 12.12， ......
        - 2. 字符串 str ：
            - 使用一对单引号或者一对双引号包住的字符，这里的字符泛指所有能表达出来的字符    "Python"
        - 3. 布尔类型 bool :
            - 表示真假，一般用于判断，只有两个取值: True 和 False
            
        上述都是单个存储数据的数据类型，下面是用于存储多个基本数据的数据类型（之后会详细讲解，这里为了完整性提一下）
        - 4. 列表 list ：
            - 使用一对[]，里面的元素使用逗号隔开   [1, 2, 3, 4]
        - 5. 元组 tuple :   
            - 使用一对()，里面的元素使用逗号隔开   (1, 2, 3, 4)
        - 6. 集合 set :   
            - 使用一对{}，里面的元素使用逗号隔开   {1, 2, 3, 4}
        - 7. 字典 dict :
            - 使用一对{}，里面的元素是键值对形式，一个键值对使用冒号: 多个键值对使用逗号隔开   {'name': '吴姗姗', 'age': 26}
"""

"""
    两个常见的函数：
    - 1. print() : 用于打印输出内容到控制台，每一个print()语句输出后，默认换行
    - 2. type()  : 返回当前输入数据的数据类型
"""

# int
print(type(1))

# float
print(type(0.12))

# str
print(type('Python'))

# bool
print(type(True))

# list
print(type([1, 2, 3, 4]))

# tuple
print(type((1, 2, 3, 4)))

# set
print(type({1, 2, 3, 4}))

# dict
print(type({'name': '吴姗姗', 'age': 26}))
