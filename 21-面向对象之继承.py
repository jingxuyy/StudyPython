"""
    继承就是允许一个类（称为子类或派生类）继承另一个类（称为父类或基类）的属性和方法。
    子类可以继承父类的特性，并且可以在此基础上添加自己的新特性。
    这种机制允许代码的重用和层次化的设计。继承，就是字面上意思，继承

    python提供了两种继承方式：
        - 单继承：一个类只能继承一个父类
        - 多继承：一个类可以拥有多个父类

    书写规则：
    class 类名(父类名1,父类名2,...):
        pass

    如果当前类没有写任何父类，那么此类继承于object类
    例如：
    class Person:
        pass

    class Person(object):
        pass

    这两种方式都是默认继承父类object
    在python中所有的类都是直接或者间接继承object类

    实现继承后，子类可以拥有父类的资源（方法和属性），也就是子类可以调用父类的方法和属性
    在封装上说明了，如果一个类拥有私有属性或者方法，那么这个类和属性只能在当前类访问，而在外界不能直接访问
    因此 如果父类A存在私有属性和方法，那么子类B是不能访问A类的私有属性和方法，但是子类可以访问父类的受保护的属性和方法

    因为子类可以调用父类属性和方法，所以继承可以很方便实现资源重用
    子类可以在不修改父类的情况下，添加新的属性和方法，从而使得代码更具可扩展性。这样可以在不影响父类的基础上，为程序添加新的功能。

    例如：
        class Animal:
            name = 'Animal'
            __age = 10

            def speak(self):
                return "Woof!"

            def __work(self):
                return "__work!"

        class Dog(Animal):
            pass

        dog = Dog()
        print(dog.speak())  # Woof!
        print(dog.name)  # Animal

        print(dog.__age)  # 报错
        dog.__work()  # 报错
        子类Dog并没有任何属性，单由于Doa继承了父类Animal，因此子类Dog就相当于拥有了父类的公开的属性和方法：name和speak
        但是私有属性和方法是属于父类独有的不能由子类继承过来，因此：__age和__work()不能访问

        子类继承父类的资源使用方式有两种：
         - 1. 直接使用：
                直接通过子类调用父类的属性和方法使用
         - 2. 重写：即在子类重写声明和父类相同的方法或者属性
                1. 部分修改：
                    若父类方法不能完成当前的需求，那么就要重写，在子类重写声明同名方法，然后在方法内先调用父类方法，然后对父类方法的返回值进行其它操作
                2. 完全修改：
                    若父类的方法和目标需求完全不同，那么重写，在子类重写声明同名方法，然后书写自己的代码，也就是不使用父类的方法

        子类访问顺序问题：
            就近原则：例如，子类和父类同时有同名的方法或者属性，那么子类只会调用自己的方法，当子类没有和父类的同名方法，调用时，会首先在子类查找，发现不存在，那么接下来会查找父类的属性和方法，有则调用，
                            没有就接着找父类，一直找到最高父类object中，若是还没有则报错

            多继承有两种方式：
                不成环：例如
                    C---B--A
                    E---D--A
                这种情况：就是A有两个父类B和D，而B继承C，D继承E

                成环：例如
                    C---B--A
                    C---D--A
                    E--C
                这种情况：就是A有两个父类B和D，而B和D又同时继承于C,C继承E

            那么子类访问父类的资源，怎么寻找
            使用C3算法，例如：不成环情况：
                假设 class A(B, D):
                mro(C) = [C] + merge(mro(object), [object]) = [C] + merge([object] + [object]) = [C] + [object] = [C, object]
                mro(E) = [E] + merge(mro(object), [object]) = [E] + merge([object] + [object]) = [E] + [object] = [E, object]

                mro(B) = [B] + merge(mro(C), [C]) = [B] + merge([C, object], [C]) = [B, C, object]
                mro(D) = [D] + merge(mro(E), [E]) = [D] + merge([E, object], [E]) = [D, E, object]

                mro(A) = [A] + merge(mro(B), mro(D), [B, D]) = [A] + merge([B, C, object], [D, E, object], [B,D]) = [A] + [B, C, D, E, object]
                       = [A, B, C, D, E, object]
                注意：在书写多继承时，其父类在小括号内有先后顺序，其顺序就对应merge()中的顺序

                成环：
                假设 class A(D,B):
                mro(E) = [E, object]
                mro(C) = [C] + merge(mro(E)) = [C, E, object]
                mro(B) = [B] + merge(mro(C),[C]) = [B] + merge([C, E, object], [C]) = [B, C, E, object]
                mro(D) = [D] + merge(mro(C),[C]) = [D] + merge([C, E, object], [C]) = [D, C, E, object]
                mro(A) = [A] + merge(mro(D), mro(B), [D, B]) = [A] + merge([D, C, E, object], [B, C, E, object], [D, B])
                       = [A] + [D, B, C, E, object]
                       = [A, D, B, C, E, object]

            mro()计算规则：
                mro(A) = [A] + merge(mro(A的父类1), mro(A的父类2), ..., mro(A的父类n), [A的父类1, A的父类2, ...., A的父类n])
                merge规则：按顺序依次遍历每个列表，
                            1. 取第一个列表头部元素，查看剩下所有列表头部元素是否和当前元素相同，若相同，则当前元素放入最终访问顺序列表，各个列表删除此元素
                            2. 取第二个列表头部元素，重复第一步
                            如果第一步取出的列表头元素和其它剩下所有列表头部元素不相同则进行第三步
                            3. 依次检查所有和当前元素，首部元素不同的列表，是否存在当前的元素
                            4. 不存在，则当前元素放入最终访问顺序列表，并且删除那些相同头部的首元素
                            5. 存在，则说明继承关系存在错误，报错

"""


# class Animal:
#     name = 'Animal'
#     __age = 10
#
#     def speak(self):
#         return "Woof!"
#
#     def __work(self):
#         return "__work!"
#
#
# class Dog(Animal):
#     pass
#
#
# dog = Dog()
# print(dog.speak())  # Woof!
# print(dog.name)  # Animal

# print(dog.__age)  # 报错
# dog.__work()  # 报错

# class C:
#     pass
# class B(C):
#     pass
#
# class E:
#     pass
# class D(E):
#     pass
#
# class A(B, D):
#     pass
#
# print(A.mro())  # [<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class 'object'>]

class E:
    pass

class C(E):
    pass
class B(C):
    pass


class D(C):
    pass

class A(D, B):
    pass

print(A.mro())  # [<class '__main__.A'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.E'>, <class 'object'>]