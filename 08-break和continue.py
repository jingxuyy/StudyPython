
"""
    如果在循环中满足了其它条件需要退出时，就可以使用break和continue语句

    while 条件1:
        ......
        if 条件2:
            退出循环
        ......

    if i in 序列：
        ......
        if 条件:
            退出循环
        ......

    这里所说的退出循环包括两种意思：
        - 1. 直接退出循环，循环不执行了
        - 2. 退出当前的循环，执行下一次循环
                例如：
                    当while循环需要执行10次时，再执行到第7次循环：
                        - 1. 直接退出循环，循环不执行了 指的是7，8，9，10次循环不执行，直接退出
                        - 2. 退出当前的循环，执行下一次循环 指的是当前第7次循环不执行了，直接执行下面8，9，10次循环
    break: 对应直接退出循环
    continue: 对应退出本次循环，执行接下来的循环
            当代码执行到continue，此时continue之后的所有循环内的代码不再执行，而是直接跳到下一次循环


    注意： break和continue一般都是配合循环语句使用，不能单独使用
"""

"""
    while与break演示
"""
i = 1
while i <= 5:
    if i == 4:
        print(f'吃饱了不吃了')
        break
    print(f'吃了第{i}个苹果')
    i += 1
# 吃了第1个苹果
# 吃了第2个苹果
# 吃了第3个苹果
# 吃饱了不吃了

"""
    while与continue
"""
i = 1
while i <= 5:
    if i == 3:
        print(f'⼤⾍⼦，第{i}个不吃了')
        # 在continue之前⼀定要修改计数器，否则会陷⼊死循环
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1
# 注意：由于continue会跳过continue之下未执行的代码，在while语句内，如果条件改变的语句放在continue之后，会导致一旦执行continue则条件改变的语句再也执行不到，导致死循环
# 因此：1. 要么把条件改变的语句放在主分支和continue分支都能执行到的地方，如下  2. 要么把条件改变的语句在主分支和continue分支都写一份，如上
"""
i = 0
while i < 5:
    i += 1
    if i == 3:
        print(f'⼤⾍⼦，第{i}个不吃了')
        continue
    print(f'吃了第{i}个苹果')
    
"""
i = 0
while i < 5:
    i += 1
    if i == 3:
        print(f'⼤⾍⼦，第{i}个不吃了')
        continue
    print(f'吃了第{i}个苹果')


"""
    for与break演示
"""
str1 = 'Python'
for i in str1:
    if i == 'y':
        print('遇到y不打印')
        break
    print(i)

"""
    for与continue演示
"""
str1 = 'Python'
for i in str1:
    if i == 'y':
        print('遇到y不打印y')
        continue
    print(i)

