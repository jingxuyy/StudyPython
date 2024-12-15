
"""
    循环语句之for

    同理和while循环一样，执行循环。for循环能完成的while循环也能完成，反之依然
    只是在一些情况下while循环方便一些，在另一些情况下for循环方便一些

    格式：
        for item in 序列:
            循环执行语句1
            循环执行语句2
            循环执行语句3
            ......

    序列：指的是可以遍历的集合，在当前知识点的情况下：字符串就是序列，字符串是一个个字符组在一起的序列
    item：是临时变量用来存储在序列里取出来的元素

    例如：
        name = 'Python'
        for character in name:
            print(character, end=' ')      ---------> P y t h o n

    for 循环不需要条件，它依次循环遍历 序列，直到遍历完序列的所有元素就停止循环

    如果想让for循环指定次数：
        例如：打印50次Python，此时需要借助range()函数
        例如：range(n)函数会产生一个序列，这个序列的内容是从0到n-1个数的序列
            这样当for遍历完range(n)就执行了n次循环

    同理for循环也可以嵌套

"""

name = 'Python'
for character in name:
    print(character, end=' ')

"""
    打印50次Python
"""
for i in range(50):
    print('Python')

"""
    案例：
        计算1-100累加和
"""
sum = 0
for i in range(101):
    sum += i
print(f"1-100的和为{sum}")

"""
    案例：
        计算1-100偶数累加和
"""
sum = 0
for i in range(101):
    if i % 2 == 0:
        sum += i
print(f"1-100的和为{sum}")

