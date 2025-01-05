"""
    多态是指允许对象在不同的情况下表现出不同的行为。简单地说，多态性意味着相同的方法调用可能会有不同的实现方式，
    具体取决于调用该方法的对象的类型或类的实现

    方法重写是实现多态的一种方式，它允许子类覆盖（重写）父类的方法，以便在子类中实现特定的行为。
    当子类重新定义了与父类同名的方法时，调用这个方法时会执行子类的实现

    例如：
        class Animal:
            def speak(self):
                raise NotImplementedError("Subclass must implement abstract method")

        class Dog(Animal):
            def speak(self):
                return "Woof!"

        class Cat(Animal):
            def speak(self):
                return "Meow!"

        # 多态性的体现
        def animal_sound(animal):
            return animal.speak()

        dog = Dog()
        cat = Cat()

        print(animal_sound(dog))  # 输出: Woof!
        print(animal_sound(cat))  # 输出: Meow!

    由于python的数据类型是在运行时才确定的，因此严格意义上，python没有多态

    抽象类和抽象方法：
    在python中实现抽象类和抽象方法，需要导入abc模块

    抽象方法指的是没有方法体的方法，只是简单做了一个规定，具体实现由子类实现
    可以通过抽象类定义抽象方法，从而强制子类实现这些方法，实现接口的规范化
    抽象类的子类必须实现抽象类里的抽象方法

    抽象类不能创建对象

    例如：
        多人合作开发的时候，定义好抽象类，每个人知道抽象类的接口，就知道别人继承这个类都拥有哪些方法（抽象方法子类必须实现）
        所以自己就知道要调用什么方法

         import ABC, abstractmethod
            class Shape(ABC):
                @abstractmethod
                def draw(self):
                    pass

            class Circle(Shape):
                def draw(self):
                    return "Drawing Circle"

            class Square(Shape):
                def draw(self):
                    return "Drawing Square"

            # 多态性的体现
            def draw_shape(shape):
                return shape.draw()

            # 抽象基类确保子类实现了抽象方法
            # rectangle = Shape()  # 会引发错误，因为 Shape 是抽象基类，不能实例化

            circle = Circle()
            square = Square()

            print(draw_shape(circle))  # 输出: Drawing Circle
            print(draw_shape(square))  # 输出: Drawing Square


    内置属性：
        1. __class__ 输出当前对象是由哪个类创建的
            class A:
                pass

            print(A.__class__)  # <class 'type'>
            a = A()
            print(a.__class__)  # <class '__main__.A'>
            类对象 A 由 type类创建
            a对象由 A类创建

        2. __dict__ 输出一个字典，表明当前对象拥有哪些属性和方法
            class A:
                def __init__(self, name, age):
                    self.name = name
                    self.age = age

                def play(self):
                    print(f"{self.name}={self.age}")

            class B(A):
                def __init__(self, name, age, sex):
                    super().__init__(name, age)
                    self.sex = sex

            print(A.__dict__)  # {'__module__': '__main__', '__init__': <function A.__init__ at 0x000001D43A850670>, 'play': <function A.play at 0x000001D43DDE4160>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
            print(B.__dict__)  # {'__module__': '__main__', '__init__': <function B.__init__ at 0x000001D43AAFC280>, '__doc__': None}
            b = B("三三", 19, "女")
            print(b.__dict__)  # {'name': '三三', 'age': 19, 'sex': '女'}

        3. __slots__
        4. __module__ 查看当前的对象在哪个模块里

"""


# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
#
# # 多态性的体现
# def animal_sound(animal):
#     return animal.speak()
#
#
# dog = Dog()
# cat = Cat()
#
# print(animal_sound(dog))  # 输出: Woof!
# print(animal_sound(cat))  # 输出: Meow!


# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
#
#
# class Circle(Shape):
#     def draw(self):
#         return "Drawing Circle"
#
#
# class Square(Shape):
#     def draw(self):
#         return "Drawing Square"
#
#
# # 多态性的体现
# def draw_shape(shape):
#     return shape.draw()
#
#
# # 抽象基类确保子类实现了抽象方法
# # rectangle = Shape()  # 会引发错误，因为 Shape 是抽象基类，不能实例化
#
# circle = Circle()
# square = Square()
#
# print(draw_shape(circle))  # 输出: Drawing Circle
# print(draw_shape(square))  # 输出: Drawing Square

class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self):
        print(f"{self.name}={self.age}")


class B(A):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex


print(A.__dict__)  # {'__module__': '__main__', '__init__': <function A.__init__ at 0x000001D43A850670>, 'play': <function A.play at 0x000001D43DDE4160>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
print(B.__dict__)  # {'__module__': '__main__', '__init__': <function B.__init__ at 0x000001D43AAFC280>, '__doc__': None}
b = B("三三", 19, "女")
print(b.__dict__)  # {'name': '三三', 'age': 19, 'sex': '女'}

