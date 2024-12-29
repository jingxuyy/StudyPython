"""
    面向对象

    程序最常见的设计范式
    1. 面向过程
    2. 面向对象

    面向过程：在之前所有编写的代码都是面向过程，如果想实现某种功能，要分析实现这个功能的每一步做些什么，然后将这些步骤封装成函数，然后进行一一调用
    面向对象：是把实现某个功能进行分析，然后分解成一个个对象，实现功能就是用对象进行交互

    ⾯向对象是⼀种抽象化的编程思想，很多编程语⾔中都有的⼀种思想。

    在Python中 万物皆对象，在现实世界也是如此。

    以洗衣服为例：
        1. 找盆 - 放⽔ - 加洗⾐粉 - 浸泡 - 搓洗 - 拧⼲⽔ - 倒⽔ - 漂洗N次 - 拧⼲ - 晾晒。
        2. 打开洗⾐机 - 放⾐服 - 加洗⾐粉 - 按下开始按钮 - 晾晒。

        第一种洗衣服方式就是面向过程：最大特点就是每一步都需要自己实现
        第二种就是面向对象，洗衣机这个对象可以完成洗衣服

    ⾯向对象就是将编程当成是⼀个事物，对外界来说，事物是直接使⽤的，不⽤去管他内部的情况。⽽编程就是设置事物能够做什么事。

    洗⾐机洗⾐服描述过程中，洗⾐机其实就是⼀个事物，即对象，洗⾐机对象哪来的呢？
    ⼯⼈根据设计师设计的功能图纸制作洗⾐机。
    总结：图纸 → 洗⾐机 → 洗⾐服。

    在⾯向对象编程过程中，有两个重要组成部分：类 和 对象。
    类和对象的关系：⽤类去创建⼀个对象。

    也就是类是对象的抽象，类是一个描述，对象是一个实体
    一般来说，在现实生活中，对象都有两个方面进行描述：
    例如，洗衣机：
        功能：洗衣服、脱水等等
        样式：颜色，大小等等

    在python中将对象能实现的功能：即行为，称为 方法
            描述对象的特征的称为 属性
        方法对应python中的函数
        属性对应遍历


    定义一个类型，使用class关键字
    形式：
        class 类名(object):
            .....
            .....

        或者
        class 类名():
            .....
            .....

    注意：
        类名和变量名不同，类名使用大驼峰形式


    例如：
        class Animal(object):
            pass
    上述代码声明了一个Animal类，注意：pass是占位关键字，表示此类内容为空，因为在python中 使用了冒号后面没有内容会报错，为了解决这个可以使用pass占位

    创建对象：
    形式：
        变量名 = 类名()
    例如：
        my_animal = Animal()


    注意：必须先有类才能创建对应的对象

    1.在类中声明方法就是定义函数
    例如：
    class Animal(object):
        def make_sound(self):
            pass

    注意：通常来说类中的函数，其默认会有一个self参数，这个参数代表对象本身，并且传递参数时，是python自动传参

    对象调用方法：
    形式：
        对象名.方法名(参数列表)

    class Animal(object):
        def make_sound(self, sound):
            print(sound)

    my_animal = Animal()
    my_animal.make_sound("汪汪")  # 汪汪

    2.在类中声明属性，也就是声明变量
        这时候需要在 __init__(self)函数里声明才可，其实也可以不在函数里声明，这个后面说
        在__init__(self)函数声明属性  需要  self.属性名=值 形式
        class Animal(object):
            def __init__(self):
                self.name = "狗狗"
                self.age = 3

        my_animal = Animal()
        print(my_animal.age)  # 3
        print(my_animal.name)  # 狗狗

        通过类创建对象后，调用函数 需要 对象名.函数名(参数)
                        调用属性 需要 对象名.属性


        通过一个类可以创建多个对象，每个对象的属于不应该全部相同，因此可以在创建对象是对属性进行赋值
        由于属性在__init__(self)方法里，因此，只需要对此方法增加形参即可

        class Animal(object):
            def __init__(self, name, age):
                self.name = name
                self.age = age

        my_animal1 = Animal("小白", 3)
        my_animal2 = Animal("小黑", 2)
        print(f"这是{my_animal1.name}，今年{my_animal1.age}岁了")  # 这是小白，今年3岁了
        print(f"这是{my_animal2.name}，今年{my_animal2.age}岁了")  # 这是小黑，今年2岁了

        这样就可以根据同一个类创建不同属性的对象
        __init__方法的形参传值，需要在创建对象时  使用类名(参数) 形式


    python类中只有属性和方法，
    1. 方法接收传参
    class A(object):
        def sound(self, name):
            print(name)

    a = A()
    a.sound("姓名")  # 姓名

    2. 方法使用类里的属性
    class A(object):
        def __init__(self, name):
            self.name = name
        def sound(self):
            print(self.name)

    a = A("三三")
    a.sound()  # 三三

    也就是类中的各个方法如果想使用类里的属性，必须用 self.属性


    类里方法：称为成员方法
    类里属性：称为成员属性

    魔法方法：
        在类中 __方法__称为魔法方法
        __init__(self)就是一个魔法方法，它又称为构造方法，主要是用来创建对象的
        在类中要是创建对象，python解释器会首先自动调用 __init__(self)方法，


    类属性：
        属性也可以声明在__init__方法之外，例如：
        class Car(object):
            num_cars = 0  # 类属性

            def __init__(self, make, model, year):
                self.make = make
                self.model = model
                self.year = year

        car1 = Car("小米", "su7", 2024)
        car2 = Car("大米", "su7", 2024)
        print(car1.num_cars)  # 0
        print(car2.num_cars)  # 0

        类属性必须初始化，并且类属性属于类，可以看见创建不同的对象其类属性的值都一样
        并且由于类属性属于类，所以当一个对象修改类属性，其它对象不会收到影响
        car1.num_cars = 20
        car3 = Car("白米", "su7", 2024)
        print(car1.num_cars)  # 20
        print(car3.num_cars)  # 0

    类方法：
        既然有类属性，那么就有类方法，同理，类方法属于类，有这个类创建的对象都拥有此类方法
        形式：
        @classmethod
        def 方法名(cls,参数):
            .....

        class Dog(object):
            num_of_dogs = 0

            def __init__(self, name):
                self.name = name
                Dog.num_of_dogs += 1

            @classmethod
            def get_num_of_dogs(cls):
                return cls.num_of_dogs

        dog1 = Dog("Buddy")
        dog2 = Dog("Max")
        print(Dog.get_num_of_dogs())  # 输出: 2

        其中@classmethod是一个装饰器，表明此方法属于类，装饰器后面讲解

    关于类属性和类方法的使用场景：当有一个属性，每个对象的属性值都一样，那么这个属性可以声明成类属性，例如一个班的学生 其学生所在班级，
                            当一个方法，每个对象的方法内容都一样，则可以声明成类方法

    另外类属性和类方法可以不用通过创建对象调用，由于类属性和类方法都属于类，因此可以直接同类调用  形式：  类名.属性名    类名.方法名(参数)


    3. 静态方法
        有的时候，一些方法只是将其封装到类中，方便管理，但是使用时候，又不需要创建对象，此时可以创建静态方法

        形式：
        @staticmethod
        def 方法名(参数):
            ......

        class Calculator(object):
            @staticmethod
            def sum(x, y):
                return x + y

            @staticmethod
            def div(x, y):
                return x / y

        print(Calculator.sum(1, 5))  # 6
        print(Calculator.div(1, 5))  # 0.2

        静态方法调用时不需要创建对象，使用 类名.方法名(参数) 即可



"""

# class Animal(object):
#     pass
#
#
# my_animal = Animal()


# class Animal(object):
#
#     def make_sound(self, sound):
#         print(sound)
#
# my_animal = Animal()
# my_animal.make_sound("汪汪")  # 汪汪


# class Animal(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# my_animal1 = Animal("小白", 3)
# my_animal2 = Animal("小黑", 2)
# print(f"这是{my_animal1.name}，今年{my_animal1.age}岁了")  # 这是小白，今年3岁了
# print(f"这是{my_animal2.name}，今年{my_animal2.age}岁了")  # 这是小黑，今年2岁了


# class Car(object):
#     num_cars = 0  # 类属性
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#
# car1 = Car("小米", "su7", 2024)
# car2 = Car("大米", "su7", 2024)
# print(car1.num_cars)  # 0
# print(car2.num_cars)  # 0
#
# car1.num_cars = 20
# car3 = Car("白米", "su7", 2024)
# print(car1.num_cars)  # 20
# print(car3.num_cars)  # 0

# class Dog(object):
#     num_of_dogs = 0
#
#     def __init__(self, name):
#         self.name = name
#         Dog.num_of_dogs += 1
#
#     @classmethod
#     def get_num_of_dogs(cls):
#         return cls.num_of_dogs
#
#
# dog1 = Dog("Buddy")
# dog2 = Dog("Max")
# print(Dog.get_num_of_dogs())  # 输出: 2

# class Calculator(object):
#
#     @staticmethod
#     def sum(x, y):
#         return x + y
#
#     @staticmethod
#     def div(x, y):
#         return x / y
#
#
# print(Calculator.sum(1, 5))  # 6
# print(Calculator.div(1, 5))  # 0.2





