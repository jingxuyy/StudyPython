"""
    回忆：
        声明一个类：
            使用class关键字
            class 类名(object):
                pass

            其中类名需要遵守大驼峰命名规则

        根据类创建对象：
            对象变量名 = 类名()

        关系：类是一个模板，对象是根据类进行创建的实例，可以叫做实例对象，默认情况下，对象拥有类的所有资源

        类中具有资源：
            1. 属性
            2. 方法

            其中，属性分为：类属性和实例属性
                - 类属性：类属性属于类，类属性必须进行初始化赋值，根据当前类创建的所有对象，拥有相同的类属性
                    - 类属性的访问：
                        1. 通过对象访问    对象名.类属性
                        2. 通过类直接访问   类名.类属性
                    - 类属性的修改：
                        只能通过类进行修改：   类名.类属性=值
                        不能通过对象进行修改：
                            例如：对象名.类属性=值
                            执行过后，其意思是向对象增加一个和类属性相同的示例属性

                - 实例属性：实例属性属于每个实例，不同的实例其实例属性的值可以不同
                    - 实例属性定义在 __init__(self):方法中
                    - 实例属性的访问：
                        通过对象访问     对象名.实例属性
                    - 实例属性的修改：
                        只能通过对象进行访问

            方法（即定义在类中的函数）分为：实例方法、类方法、静态方法
                - 实例方法：属于每个实例对象
                    - 定义：def func(self):
                                pass
                    - 实例方法拥有默认的形参，第一个形参默认为self，当实例对象调用此方法时，会把实例对象自动传入到self中

                - 类方法：属于类
                    - 定义： @classmethod
                            def func(cls)
                                pass
                    - 类方法方法拥有默认的形参，第一个形参默认为cls，当类调用此方法时，会把类自动传入到cls中
                    - 类方法需要使用@classmethod装饰器

                - 静态方法：
                    - 定义： @staticmethod
                            def func()
                                pass
                    - 静态方法没有默认形参，
                    - 类方法需要使用@staticmethod装饰器


        python中整数、小数等也是对象  整数对应int类、小数对应float类  字符串对应str类  列表对应list类

        所有类都有元类，所有类其元类直接或者间接都是type类
        type类的元类是type

        注意：类也是一个对象，不过这个对象特殊、拥有创建其它对象的能力

        这些类都是经过元类进行创建的
        例如：int list等类都是通过type类创建

        我们自己定义的类只能创建对象，不能创建类对象



    封装：
        封装是指将数据（属性）和操作数据的方法（方法）捆绑在一起的机制。
        在封装中，对象的内部细节被隐藏起来，只有特定的方法才能访问和操作这些细节。
        这有助于确保数据的安全性和代码的可维护性。

        创建类，将属性和函数定义在类中其实就是一种封装

        第二种封装：隐藏一些类或者对象的属性或者方法，外界只能通过特定的方法来获取或者修改其资源

        封装的实现：
            通过访问控制和访问修饰符来实现。主要有两种访问修饰符：公有属性和方法、私有属性和方法。

            默认情况下在类中定义的所有属性和方法都是公有属性，公有方法或者属性允许这个资源在类外部被访问

        私有属性和私有方法的定义：
            在python中在属性名或者方法名之前添加两个下划线，其意义就是定义为私有属性和方法
            例如：
                class Person:
                    __producer = "xxx"
                    def __init__(self, name, age):
                        self.__name = name   # 私有属性
                        self.__age = age     # 私有属性

                    def __display_info(self):
                        return f"Name: {self.__name}, Age: {self.__age}"   # 私有方法

                # 外部无法直接访问私有属性和方法
                person1 = Person("TiYong", 25)
                # print(person1.__name)  # 这会引发错误，因为__name是私有属性
                # print(person1.__display_info())  # 这会引发错误，因为__display_info()是私有方法
                # print(person1.__producer)

            私有属性和方法不能被类外代码进行访问，因此由此类创建的对象也不能访问，私有属性可以在类中进行访问

            如果想提供私有属性或者方法给外界访问，则可以提供公有方法给外界访问，在公有方法里可以设置数据校验，以保证私有属性的安全性
            例如：
                class Person:
                    def __init__(self, name, age):
                        self.__name = name   # 私有属性
                        self.__age = age     # 私有属性

                    def get_name(self):
                        return self.__name   # 公有方法

                    def set_name(self, new_name):
                        self.__name = new_name   # 公有方法，用于修改私有属性

                    def display_info(self):
                        return f"Name: {self.__name}, Age: {self.__age}"   # 公有方法

                # 通过公有方法访问和修改私有属性
                person1 = Person("TiYong", 30)
                print(person1.get_name())  # 输出: TiYong
                person1.set_name("Toy")
                print(person1.display_info())  # 输出: Name: Toy, Age: 30

        注意：python没有提供真正的私有方法和私有属性，其底层是将私有方法或者私有属性修改了名称，从而实现了外界无法访问

        在python还提供了受保护的访问限制：
            受保护的属性和方法 定义为在公有属性或者方法名前添加一个下划线

        因为python没有真正的私有化，所以需要访问时不要破坏私有性：
            私有属性或者方法：只允许在本类中访问
            受保护的属性或者方法：只允许在本类和其子类中访问
            公有的属性和方法：可以在任意位置访问


        顺便一说：
            1.在python还存在   变量名_  这样的变量，这主要是当前变量名和系统变量名重名了，为了解决冲突将重名的变量名后增加一个下划线（自己编写代码时，应避免这种情况发生）
            2. python中还存在  __变量名__   __方法名__  这样的属性或者方法，是python中内置的方法或者属性，提供了特殊的功能（自己编写代码时，应避免这种情况发生）

        由于私有化：如果有些属性 是只读属性，那么可以将这些属性设置成私有化，然后提供一个读方法即可
        例如：
            class Person(object):
                def __init__(self, name, age):
                    self.__name = name
                    self.__age = age

                def get_name(self):
                    return self.__name

                def get_age(self):
                    return self.__age


            p = Person("五三三", 12)
            print(p.get_name())  # 五三三
            print(p.get_age())  # 12

            p.name = "一一"
            p.age = 20

            print(p.name)  # 一一
            print(p.age)  # 20

            注意：p.name = "一一"和p.age = 20是给p对象增加了两个名为name和age的属性，而不是修改了私有属性
            这个是python类的特点，可以动态添加原本类没有的属性，
            其实这种行为是不好的行为，破坏了类的封装性，在开发中应该避免这种情况出生，
            由于这种赋值方式，如果类中没有对应的实例属性或者类属性，则会自动添加，为了防止这种情况意外发生
            python提供了一个内置属性来控制：
                __slots__
            它是一个列表，列表中可以定义一些属性名，例如 __slots__ = ['a']
            这意味着，此类的对象可以动态添加一个原本没有的实例属性
            所以一般将 __slots__设置为 [类中已定义的所有属性]
            这样除了类中定义的类属性和实例属性，外界不允许动态添加其它属性
            例如：
                class Person(object):
                    __slots__ = ['__name', '__age']
                    def __init__(self, name, age):
                        self.__name = name
                        self.__age = age

                    def get_name(self):
                        return self.__name

                    def get_age(self):
                        return self.__age


                p = Person("五三三", 12)
                print(p.get_name())  # 五三三
                print(p.get_age())  # 12

                p.name = "一一"
                p.age = 20

                print(p.name)  # 报错
                print(p.age)  # 报错


            介绍第二个内置属性：
                __dict__
            它是一个字典，用来存储类的属性和方法，或者是对象的属性和方法
            例如：
                class Person(object):
                    def __init__(self, name, age):
                        self.__name = name
                        self.__age = age

                    def get_name(self):
                        return self.__name

                    def get_age(self):
                        return self.__age


                print(Person.__dict__)  # {'__init__': <function Person.__init__ at 0x00000226CD9C0670>,
                                        # 'get_name': <function Person.get_name at 0x00000226D0F84160>, 'get_age': <function Person.get_age at 0x00000226CDC6C280>}
                p = Person("五三三", 12)
                p.name = "一一"
                p.age = 20
                print(p.__dict__)  # {'_Person__name': '五三三', '_Person__age': 12, 'name': '一一', 'age': 20}
            可以看到实例的__dict__只有私有属性，以及后添加的属性
            而类的__dict__除了声明的属性，还存放着类的一些方法


        一些内置方法：
            1. __str__ 和 __repr__
            一般情况：
                class Person(object):
                    def __init__(self, name, age):
                        self.__name = name
                        self.__age = age

                p = Person("三三", 22)
                print(p)  # <__main__.Person object at 0x000001709FA2FFD0>
            可以看到对象也可以直接打印输出，不过默认情况下打印的信息是  <模块名.类名 object at 对象在内存的地址>
            这样的打印对象其实没有太多的用处
            例如：对于上述Person类，如果打印输出其对象，要求输出信息为有意义的信息，比如 ”我的名字是xx，我的年龄是xx“

            这样就可以使用__str__ 或者 __repr__内置方法，这两个内置方法功能相同，只需要写一个即可，
                它的查找顺序是当打印输出对象时，执行当前类中的__str__方法，如果不存在则查找当前类的__repr__方法，如果不存在，则执行内置默认的__str__方法 则输出就是<模块名.类名 object at 对象在内存的地址>
            示例：
                class Person(object):
                    def __init__(self, name, age):
                        self.name = name
                        self.age = age

                    def __str__(self):
                        return f"我的名字是{self.name}，我的年龄是{self.age}"

                p = Person("三三", 22)
                print(p)  # 我的名字是三三，我的年龄是22
            同理__repr__也是如此，不再演示

            2. __call__方法
            只要实现了这个方法，则此类创建的对象就能像函数一样通过小括号调用，这在一些特殊的情况下能用到
            一般情况：




"""


# class Person:
#     __producer = "xxx"
#
#     def __init__(self, name, age):
#         self.__name = name  # 私有属性
#         self.__age = age  # 私有属性
#
#     def __display_info(self):
#         return f"Name: {self.__name}, Age: {self.__age}"  # 私有方法
#
#
# # 外部无法直接访问私有属性和方法
# person1 = Person("TiYong", 25)
# print(person1.__name)  # 这会引发错误，因为__name是私有属性
# print(person1.__display_info())  # 这会引发错误，因为__display_info()是私有方法
# print(person1.__producer)


# class Person:
#     def __init__(self, name, age):
#         self.__name = name  # 私有属性
#         self.__age = age  # 私有属性
#
#     def get_name(self):
#         return self.__name  # 公有方法
#
#     def set_name(self, new_name):
#         self.__name = new_name  # 公有方法，用于修改私有属性
#
#     def display_info(self):
#         return f"Name: {self.__name}, Age: {self.__age}"  # 公有方法
#
#
# # 通过公有方法访问和修改私有属性
# person1 = Person("TiYong", 30)
# print(person1.get_name())  # 输出: TiYong
# person1.set_name("Toy")
# print(person1.display_info())  # 输出: Name: Toy, Age: 30


# class Person(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#
# p = Person("五三三", 12)
# print(p.get_name())  # 五三三
# print(p.get_age())  # 12
#
# p.name = "一一"
# p.age = 20
#
# print(p.name)  # 一一
# print(p.age)  # 20


# class Person(object):
#
#     __slots__ = ['__name', '__age']
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#
# p = Person("五三三", 12)
# print(p.get_name())  # 五三三
# print(p.get_age())  # 12
#
# p.name = "一一"
# p.age = 20
#
# print(p.name)  # 报错
# print(p.age)  # 报错


# class Person(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#
# print(Person.__dict__)  # {'__init__': <function Person.__init__ at 0x00000226CD9C0670>, 'get_name': <function Person.get_name at 0x00000226D0F84160>, 'get_age': <function Person.get_age at 0x00000226CDC6C280>}
#
# p = Person("五三三", 12)
# p.name = "一一"
# p.age = 20
# print(p.__dict__)  # {'_Person__name': '五三三', '_Person__age': 12, 'name': '一一', 'age': 20}


# class Person(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#
# p = Person("三三", 22)
# print(p)  # <__main__.Person object at 0x000001709FA2FFD0>


# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"我的名字是{self.name}，我的年龄是{self.age}"
#
#
# p = Person("三三", 22)
# print(p)  # 我的名字是三三，我的年龄是22


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"我的名字是{self.name}，我的年龄是{self.age}"


p = Person("三三", 22)
print(p)  # 我的名字是三三，我的年龄是22

