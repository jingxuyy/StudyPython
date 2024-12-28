"""
    文件操作：就是把数据写到文件中，或者将已有的文件读取到程序中

    1. 打开文件
        在python中使用open()函数来打开一个文件
        打开文件后才能读取文件内容
        open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
        参数file表示文件路径，可以使用相对路径或者绝对路径
        mode表示以什么模式打开文件
        常见的模式：
            mode = 'r'   表示只读模式
            mode = 'w'   写模式打开文件  文件不存在则自动创建  使用这种模式，如果向文件写入数据，会默认将原本存在的数据覆盖
            mode = 'a'   追加模式打开文件  文件不存在则自动创建 使用这种模式，如果向文件写入数据，会在原有文件末尾进行追加写
            mode = 'rb'  以二进制形式打开文件  一般用这种模式打开非文本文件，例如图片、视频等
            mode = 'wb'  以二进制形式打开文件  一般用这种模式打开非文本文件，例如图片、视频等 可以写入
        # 以只读模式打开文件
        file = open('example.txt', 'r')
        # 以写入模式打开文件（如果文件不存在则创建）
        file = open('example.txt', 'w')
        # 以追加模式打开文件（如果文件不存在则创建）
        file = open('example.txt', 'a')
        # 以二进制模式打开文件
        file = open('example.jpg', 'rb')

        encoding 表示打开文件使用的编码，常用utf-8或者gbk  需要写入文件和打开文件编码相同，否则会出现乱码

    2. 关闭文件
        close()
        注意：当打开文件后，对文件进行一系列操作后，需要把文件进行关闭

        file = open('example.txt', 'w')
        .......
        .......
        file.close()

    3. 读文件
        - read(num)  或者  read() 表示读取文件内容，num表示字节数，表示当前一次读取多少字节，如果不传则默认一次读取文件里所有内容
        例如：
            file_read = open('洛神赋.txt', mode='r', encoding="utf-8")
            print(file_read.read())
            # 其形也，翩若惊鸿，婉若游龙。
            # 荣曜秋菊，华茂春松。
            # 仿佛兮若轻云之蔽月，飘飘兮若流风之回雪。
            # 远而望之，皎若太阳升朝霞；迫而察之，灼若芙蕖出渌波。
            # ......
            print(file_read.read(10))  # 其形也，翩若惊鸿，婉
            file_read.close()

        - readlines()    按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
        例如：
            print(file_read.readlines())
            file_read.close()
            # ['其形也，翩若惊鸿，婉若游龙。\n', '荣曜秋菊，华茂春松。\n', '仿佛兮若轻云之蔽月，飘飘兮若流风之回雪。\n', '远而望之，皎若太阳升朝霞；迫而察之，灼若芙蕖出渌波。\n', .......]
        注意使用readlines()函数读取，一次读取文件所有内容，其结果是一个列表，列表里的元素是文件中每一行数据，并且还包括换行符

        - readline()   一次读取一行内容
        例如：
            print(file_read.readline())  # 其形也，翩若惊鸿，婉若游龙。
            file_read.close()


        利用循环 读取文件内容
        例如：
            for txt in file_read:
                print(txt)
            # 其形也，翩若惊鸿，婉若游龙。
            #
            # 荣曜秋菊，华茂春松。
            #
            # 仿佛兮若轻云之蔽月，飘飘兮若流风之回雪。
            #
            # 远而望之，皎若太阳升朝霞；迫而察之，灼若芙蕖出渌波。
            #
            # 襛纤得衷，修短合度。
            file_read.close()
        打开文件后，获取的变量也是可迭代的，即可以使用for循环遍历，每一次遍历将会得到文件中每一行内容，注意：每一行文本本身就有换行符，然后print函数也有换行符，所以打印输出会出现空白行

        文件上下文管理器：使用with语句打开文件，在使用完文件后，会自动将文件进行关闭，这样可以省略人为手写close语句
        建议：python操作文件都是用上下文管理器
        形式：
            with open("文件", mode="模式", encoding="编码") as file:
                文件操作语句....
                ......
            上述是使用file变量名接收打开的文件，这个不固定
        例如：
            with open("洛神赋.txt", encoding="utf-8", mode="r") as file:
                for txt in file:
                    print(txt)

            # 其形也，翩若惊鸿，婉若游龙。
            #
            # 荣曜秋菊，华茂春松。
            # ......

        - 打开二进制文件并输出
            with open("OIP-C.jpg", mode="rb") as file:
                for txt in file:
                    print(txt)



    4. 文件写入：
        文件写入时，打开文件不能使用mode=r，和 mode=rb这是只读模式
        可以使用 mode=w或者mode=a或者mode=wb

        - write(内容)
        注意write函数会先把数据写入缓冲区，当缓冲区满了，才会把数据写到文件里
        可以使用 flush()方法强制将缓冲区内容写入到文件里

        例如：
            with open("写入文件.txt", mode='w', encoding="utf-8") as file:
                file.write('莫斗婵娟弓样月，只坐蛾眉，消得千谣诼。臂上宫砂那不灭，古来积毁能销骨。\n')
                file.write('手把齐纨相诀绝，懒祝西风，再使人间热。镜里朱颜犹未歇，不辞自媚朝和夕。\n')
                file.flush()
        如果把上述代码多执行几次，其文件内容依然是这两句，因为不是追加写

            # 追加写
            with open("写入文件.txt", mode='a', encoding="utf-8") as file:
                file.write('莫斗婵娟弓样月，只坐蛾眉，消得千谣诼。臂上宫砂那不灭，古来积毁能销骨。\n')
                file.write('手把齐纨相诀绝，懒祝西风，再使人间热。镜里朱颜犹未歇，不辞自媚朝和夕。\n')
                file.flush()

        写文件时候，若文件不存在，会自动创建


    利用文件读 文件写  可以实现一个文件复制功能


"""

# file_read = open('洛神赋.txt', mode='r', encoding="utf-8")
# print(file_read.read())
# 其形也，翩若惊鸿，婉若游龙。
# 荣曜秋菊，华茂春松。
# 仿佛兮若轻云之蔽月，飘飘兮若流风之回雪。
# 远而望之，皎若太阳升朝霞；迫而察之，灼若芙蕖出渌波。
# ......
# print(file_read.read(10))  # 其形也，翩若惊鸿，婉

# print(file_read.readlines())
# ['其形也，翩若惊鸿，婉若游龙。\n', '荣曜秋菊，华茂春松。\n', '仿佛兮若轻云之蔽月，飘飘兮若流风之回雪。\n', '远而望之，皎若太阳升朝霞；迫而察之，灼若芙蕖出渌波。\n', .......]

# print(file_read.readline())  # 其形也，翩若惊鸿，婉若游龙。

# for txt in file_read:
#     print(txt)
# 其形也，翩若惊鸿，婉若游龙。
#
# 荣曜秋菊，华茂春松。
#
# 仿佛兮若轻云之蔽月，飘飘兮若流风之回雪。
#
# 远而望之，皎若太阳升朝霞；迫而察之，灼若芙蕖出渌波。
#
# 襛纤得衷，修短合度。
# file_read.close()


# with open("洛神赋.txt", encoding="utf-8", mode="r") as file:
#     for txt in file:
#         print(txt)

# 其形也，翩若惊鸿，婉若游龙。
#
# 荣曜秋菊，华茂春松。
# ......

# with open("OIP-C.jpg", mode="rb") as file:
#     for txt in file:
#         print(txt)    b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x......

#

# 覆盖写
with open("写入文件.txt", mode='w', encoding="utf-8") as file:
    file.write('莫斗婵娟弓样月，只坐蛾眉，消得千谣诼。臂上宫砂那不灭，古来积毁能销骨。\n')
    file.write('手把齐纨相诀绝，懒祝西风，再使人间热。镜里朱颜犹未歇，不辞自媚朝和夕。\n')
    file.flush()

# 追加写
with open("写入文件.txt", mode='a', encoding="utf-8") as file:
    file.write('莫斗婵娟弓样月，只坐蛾眉，消得千谣诼。臂上宫砂那不灭，古来积毁能销骨。\n')
    file.write('手把齐纨相诀绝，懒祝西风，再使人间热。镜里朱颜犹未歇，不辞自媚朝和夕。\n')
    file.flush()




