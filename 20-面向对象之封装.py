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

            注意：__str__和__repr__如果有返回值，则返回值必须是str

            2. __call__方法
            只要实现了这个方法，则此类创建的对象就能像函数一样通过小括号调用，这在一些特殊的情况下能用到
            一般情况：
            class Person(object):
                def __init__(self, name, age):
                    self.name = name
                    self.age = age

            p = Person("三三", 22)
            p()  # 报错

            class Person(object):
                def __init__(self, name, age):
                    self.name = name
                    self.age = age

                def __call__(self, *args, **kwargs):
                    print("被调用了")


            p = Person("三三", 22)
            p()  # 被调用了
            其中__call__方法可以传递任意参数的

            3. 对象索引操作
            list、str、tuple等对象都拥有索引，可以根据索引获取元素
            自定义的类也可以实现索引操作，涉及三个内置方法：
            __setitem__  根据索引设置值
            __getitem__  根据索引获取值
            __delitem__  根据索引删除值

            例如：
            class Person(object):
                def __init__(self, name, age):
                    self.name = name
                    self.age = age
                    self.__item = []  # 定义一个列表用来存储数据

                def __setitem__(self, key, value):
                    self.__item.insert(key, value)

                def __getitem__(self, item):
                    return self.__item[item]

                def __delitem__(self, key):
                    self.__item.pop(key)

            p = Person("三三", 22)
            p[0] = 1  # 在索引0的地方存储数据1  执行此行代码 就会调用__setitem__ 方法
            p[1] = 2  # 在索引1的地方存储数据2
            p[2] = 3  # 在索引2的地方存储数据3

            print(p[0])  # 1  获取数据 会执行__getitem__方法
            print(p[1])  # 2
            print(p[2])  # 3

            del p[0]    # 删除数据 会执行 __delitem__方法
            print(p[0])  # 2

            4. 切片操作
            既然对象可以进行索引操作，则也可以进行切片
            其实切片操作就是获取元素，并且可以一次获取多个数据
            因此，类实现了
            __setitem__  根据索引设置值
            __getitem__  根据索引获取值
            __delitem__  根据索引删除值
            也就拥有了切片操作

            class Person(object):
                def __init__(self, name, age):
                    self.name = name
                    self.age = age
                    self.__item = []

                def __setitem__(self, key, value):
                    self.__item.insert(key, value)

                def __getitem__(self, item):
                    return self.__item[item]

                def __delitem__(self, key):
                    self.__item.pop(key)

                def __str__(self):
                    return str(self.__item)

            p = Person("三三", 22)
            p[0] = 1
            p[1] = 2
            p[2] = 3
            p[3] = 4
            p[4] = 5
            p[5] = 6

            print(p)  # [1, 2, 3, 4, 5, 6]
            print(p[1:3])  # [2, 3]
            print(p[-1:-3:-1])  # [6, 5]
            print(p[::-1])  # [6, 5, 4, 3, 2, 1]

            5. 比较操作
            在数值对象里比如：int和float可以进行大小、相等等比较操作，因此自定义类也可以实现这些
            要实现的内置方法为：
            __eq__ 等于
            __ne__ 不等于

            __lt__ 小于
            __gt__ 大于

            __le__ 小于等于
            __ge__ 大于等于
            这是三组相反的比较操作
            注意：实现这些内置比较方法，是要规定比较规则，例如对于一个人的对象，规定比较对象大小规则是，年龄大的大
            另外：对于相反的操作
                例如：等于和不等于，只需要在类中实现一个即可，当对象调用另一个会将结果取反
            因此，一般来说，这六个内置方法只需要实现三个即可
            例如：
                class Person(object):
                    def __init__(self, name, age):
                        self.name = name
                        self.age = age

                    def __eq__(self, other):
                        return self.age == other.age

                    def __lt__(self, other):
                        return self.age > other.age

                    def __le__(self, other):
                        return self.age >= other.age

                p1 = Person("三三", 22)
                p2 = Person("四四", 22)
                p3 = Person("五五", 20)
                p4 = Person("六六", 30)

                print(p1 == p2)  # True
                print(p1 != p2)  # False
                print(p1 >  p2)  # False
                print(p1 <  p2)  # False
                print(p1 >= p2)  # True
                print(p1 <= p2)  # True

                print(p2 == p3)  # False
                print(p2 != p3)  # True
                print(p2 >  p3)  # False
                print(p2 <  p3)  # True
                print(p2 >= p3)  # False
                print(p2 <= p3)  # True

                print(p3 == p4)  # False
                print(p3 != p4)  # True
                print(p3 >  p4)  # True
                print(p3 <  p4)  # False
                print(p3 >= p4)  # True
                print(p3 <= p4)  # False

            6. 遍历操作
            例如：字符串、列表、元组等等都可以进行遍历
            补充：在python中凡是可以使用for进行遍历的对象都是可迭代对象
                另外迭代器也可以遍历
                但是：可迭代对象不一定是迭代器，

            在之前索引操作，使用了三个内置方法
            其实，当一个类实现了内置方法
            __getitem__则这个类创建的对象就是可迭代对象
            也就是可以使用for进行遍历
            底层，没遍历一次，都会调用一次__getitem__方法
            例如：
                class Person(object):
                    __count = -1

                    def __init__(self, name, age):
                        self.name = name
                        self.age = age

                    def __getitem__(self, item):
                        if Person.__count < 6:
                            Person.__count += 1
                            return Person.__count
                        else:
                            raise StopIteration()

                p = Person("三三", 22)
                for num in p:
                    print(num, end=" ")  # 0 1 2 3 4 5 6
            注意：使用for遍历，python会自动调用__getitem__方法，因此__getitem__方法里必须有终止条件
                否则的话，for遍历会进入死循环，
                另外如果想正常终止for循环，需要在终止条件下抛出StopIteration异常即raise StopIteration()
                异常内容在之后讲解，这里只需要知道在不终止程序接下来运行的情况下，结束for循环需要书写raise StopIteration()

            在python 如果一个类 实现了内置方法
            __iter__
            那么这个类创建的对象也是可迭代对象,因为内置方法__iter__要求返回值是一个迭代器对象
            注意实现了__iter__必须返回迭代器，如果仅仅实现了__iter__那么此时的对象虽然是可迭代对象，但是不能使用for遍历
            另外__iter__和__getitem__同时实现，那么遍历时会忽略__getitem__方法，也就是不通过__getitem__进行遍历

            一般来说：
            __iter__和__next__方法进行配合使用

            说明：
                1. 当一个类仅仅实现了__getitem__方法，那么这个类创建出来的对象是可迭代对象
                2. 当一个类仅仅实现了__iter__方法，那么这个类创建出来的对象是可迭代对象
                3. 当一个类同时实现了__next__方法和__iter__方法，那么这个类创建出来的对象是迭代器对象

            由于一个类同时实现了__next__方法和__iter__方法，那么这个类创建出来的对象是迭代器对象
            所以此时__iter__方法的返回值返回本身self即可，因为此时本身就是迭代器

            当使用for进行遍历时，会先调用__iter__获得迭代器，然后再依次调用__next__方法，使用__next__方法访问数据，就类似于__getitem__方法

            class Person(object):
                __count = -1
                def __init__(self, name, age):
                    self.name = name
                    self.age = age

                def __getitem__(self, item):
                    if Person.__count < 6:
                        Person.__count += 1
                        return Person.__count
                    else:
                        raise StopIteration()

                def __iter__(self):
                    return self

                def __next__(self):
                    if Person.__count < 7:
                        Person.__count += 1
                        return Person.__count
                    else:
                        raise StopIteration()

            p = Person("三三", 22)
            for num in p:
                print(num, end=" ")  # 0 1 2 3 4 5 6 7

            可以看见当__getitem__和 （__iter__，__next__）方法同时出现，使用for遍历，默认调用的是 next方法
            注意：可以看见为了终止for遍历，代码中都抛出了StopIteration异常，但是程序任然可以执行不报错，这是因为for循环进行了捕获处理
            另外实现了__next__方法，也可以通过对象.next()方法直接调用

        介绍一个描述器：property属性
        在类的封装性质上，对于私有属性，外界不能直接访问，需要在类中提供公开的操作属性的方法
        一般来说：修改操作、增加操作、删除操作
        例如：
            class Person(object):
                def __init__(self, name, age):
                    self.__name = name
                    self.__age = age

                def get_age(self):
                    return self.__age

                def set_age(self, value):
                    if value<0 or value >130:
                        print("修改失败")
                    else:
                        self.__age = value

                def remove_age(self):
                    del self.__age
                    print('删除成功')

            p = Person("三三", 22)
            print(p.get_age())  # 22
            p.set_age(-2)  # 修改失败
            p.set_age(23)
            print(p.get_age())  # 23
            p.remove_age()  # 删除成功

            但是先不说删除操作，对于属性一般都需要获取和修改操作
            那么外界获取对象属性或者修改必须要调用公开方法，虽然公开的方法可以做一些数据校验
            但是调用时很麻烦，不能使用 对象.属性 进行获取和修改

            那么能不能存在一种方案 让私有属性能够像公有属性一样调用和修改，又能像私有属性提供公开方法保护私有属性呢？

            在python中提供了 property属性，准确的说是property装饰器
            要求：对于属性公开的方法，其方法名要和属性名相同（不是必须，但是需要遵守）

            class Person(object):
                def __init__(self, name, age):
                    self.__name = name
                    self.__age = age

                @property
                def age(self):
                    return self.__age

                @age.setter
                def age(self, value):
                    if value<0 or value >130:
                        print("修改失败")
                    else:
                        self.__age = value

                @age.deleter
                def age(self):
                    del self.__age
                    print('删除成功')

            p = Person("三三", 22)
            print(p.age)  # 22
            p.age = 10
            print(p.age)  # 10

            这样看起来是直接赋值，其实是调用了age方法
             @property
                def age(self):
                    return self.__age
            这句就是将 函数名age和@property进行了绑定 同时也和属性名__age进行了绑定
            因此下面删除、修改方法可以使用@age.deleter和@age.setter

            注意：为了防止出现错误：要求，所有对属性进行增删改的函数，其函数名都和属性同名 使用 @property表明此方法用于访问  @属性名.setter表明此方法用于修改   @属性名.deleter表明此方法用于删除


            也有第二种用法：
            class Person(object):
                def __init__(self, name, age):
                    self.__name = name
                    self.__age = age

                def get_age(self):
                    return self.__age

                def set_age(self, value):
                    if value<0 or value >130:
                        print("修改失败")
                    else:
                        self.__age = value

                def del_age(self):
                    del self.__age
                    print('删除成功')

                age = property(get_age, set_age, del_age)

            p = Person("三三", 22)
            print(p.age)  # 22
            p.age = 10
            print(p.age)  # 10

            此方法不要求属性增改的函数名
            注意：属性名 = property(xx, xx, xx)
                其形参第一个必须是获取属性的方法名、第二个为修改方法的方法名、第三个是删除方法的方法名
                另外 属性名就是用来提供外界访问的属性名


            生命周期的内置方法
            在python中每个对象都有自己的生命周期，当一个对象被创建后、使用后、如果之后这个对象不再使用，那么会被python销毁

            __new__
            用于创建对象时，给当前对象分配内存

            __init__
            用于对象创建后，给对象属性进行赋值

            __del__
            用于销毁对象

            在创建对象时，python会自动调用__new__方法，然后调用__init__方法，销毁时自动调用__del__不需要自己管理
            用的最多是__init__方法，给对象属性进行赋值


            python的垃圾回收机制
            1. 引用计数器
                - 当一个对象被创建成功时，并且赋值给一个变量，那么这个变量的引用计数器+1
                    例如：
                        p = Person() # 引用计数器+1
                        p2 = p  # 引用计数器再+1
                        此时Person()对象引用计数器为2

                        s = Student()
                        p = s
                        p2 = s
                        由于 p和 p2都指向了 s
                        因此此时Person()对象引用计数器为0
                        当触发垃圾回收时，Person()对象会被当作垃圾回收

                    引用计数器解决不了循环引用问题，导致不再使用的垃圾对象不能被回收
                    例如：
                        class Person:
                            def __init__(self):
                                self.s=None

                        class Student:
                            def __init__(self):
                                self.p=None

                        p1 = Person()
                        s1 = Student()
                        p1.s = s1
                        s1.p = p1

                        p1 = s1 = None
                        此时  Person()和Student()对象内部属性互相引用，而p1和s1已经被删除，因此造成Person()和Student()对象循环引用

            2. 垃圾回收机制（略）


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

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# p = Person("三三", 22)
# p()

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __call__(self, *args, **kwargs):
#         print("被调用了")
#
#
# p = Person("三三", 22)
# p()  # 被调用了


# class Person(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__item = []
#
#
#     def __setitem__(self, key, value):
#         self.__item.insert(key, value)
#
#     def __getitem__(self, item):
#         return self.__item[item]
#
#     def __delitem__(self, key):
#         self.__item.pop(key)
#
#
# p = Person("三三", 22)
# p[0] = 1
# p[1] = 2
# p[2] = 3
#
# print(p[0])  # 1
# print(p[1])  # 2
# print(p[2])  # 3
#
# del p[0]
# print(p[0])  # 2


# class Person(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__item = []
#
#
#     def __setitem__(self, key, value):
#         self.__item.insert(key, value)
#
#     def __getitem__(self, item):
#         return self.__item[item]
#
#     def __delitem__(self, key):
#         self.__item.pop(key)
#
#     def __str__(self):
#         return str(self.__item)
#
#
# p = Person("三三", 22)
# p[0] = 1
# p[1] = 2
# p[2] = 3
# p[3] = 4
# p[4] = 5
# p[5] = 6
#
# print(p)  # [1, 2, 3, 4, 5, 6]
# print(p[1:3])  # [2, 3]
# print(p[-1:-3:-1])  # [6, 5]
# print(p[::-1])  # [6, 5, 4, 3, 2, 1]


# class Person(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         return self.age == other.age
#
#     def __lt__(self, other):
#         return self.age > other.age
#
#     def __le__(self, other):
#         return self.age >= other.age
#
#
# p1 = Person("三三", 22)
# p2 = Person("四四", 22)
# p3 = Person("五五", 20)
# p4 = Person("六六", 30)
#
# print(p1 == p2)  # True
# print(p1 != p2)  # False
# print(p1 >  p2)  # False
# print(p1 <  p2)  # False
# print(p1 >= p2)  # True
# print(p1 <= p2)  # True
#
# print(p2 == p3)  # False
# print(p2 != p3)  # True
# print(p2 >  p3)  # False
# print(p2 <  p3)  # True
# print(p2 >= p3)  # False
# print(p2 <= p3)  # True
#
# print(p3 == p4)  # False
# print(p3 != p4)  # True
# print(p3 >  p4)  # True
# print(p3 <  p4)  # False
# print(p3 >= p4)  # True
# print(p3 <= p4)  # False


# class Person(object):
#
#     __count = -1
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __getitem__(self, item):
#         if Person.__count < 6:
#             Person.__count += 1
#             return Person.__count
#         else:
#             raise StopIteration()
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if Person.__count < 7:
#             Person.__count += 1
#             return Person.__count
#         else:
#             raise StopIteration()
#
#
# p = Person("三三", 22)
#
# for num in p:
#     print(num, end=" ")


# class Person(object):
#
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, value):
#         if value<0 or value >130:
#             print("修改失败")
#         else:
#             self.__age = value
#
#     def remove_age(self):
#         del self.__age
#         print('删除成功')
#
#
#
#
# p = Person("三三", 22)
#
# print(p.get_age())
# p.set_age(-2)
# p.set_age(23)
# p.remove_age()


# class Person(object):
#
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if value<0 or value >130:
#             print("修改失败")
#         else:
#             self.__age = value
#
#     @age.deleter
#     def age(self):
#         del self.__age
#         print('删除成功')
#
#
#
#
# p = Person("三三", 22)
#
# print(p.age)  # 22
# p.age = 10
# print(p.age)  # 10
# print(p.__dict__)


class Person(object):


    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value<0 or value >130:
            print("修改失败")
        else:
            self.__age = value

    def del_age(self):
        del self.__age
        print('删除成功')

    age = property(get_age, set_age, del_age)




p = Person("三三", 22)

print(p.age)  # 22
p.age = 10
print(p.age)  # 10



