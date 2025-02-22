# help()打开交互窗口的函数'

# a=3
# del a  删除a，就是把a释放掉了
# print(a) 所以在这里print会报错


# MAX_AGE=150
# print(MAX_AGE)
# MAX_AGE=300
# print(MAX_AGE)


# x=y=z=100
# print(x)#链式赋值

# a,b,c=1,2,3
# q=1;w=2;e=3
# print(a,b,c)



# x,y=1,2
# x,y=y,x  #变量值互换
# print(x,y)

# a=2; b=3
# a**=b;#a**b=a的b次幂
# print(a)

# type_1 = type("云边有个小卖部")
# type_2 = type(123)
# type_3 = type(11.345)
# print(type_1)
# print(type_2)
# print(type_3)

# b=int(9.8)  相当于强制转换
# print(b)
# d=int("12345678")字符串里面只有数字也可以被强制转换
# print(d)

# a=9.5;b=9.4
# c=round(a)
# d=round(b)
# print(c)
# print(d)   四舍五入函数

# import time#相当于C中导入头文件
# b=int(time.time())
# print(b)
# totalMinutes=b//60
# print(totalMinutes)
# totalDays=totalMinutes//(24*60)
# print(totalDays)
# totalYears=totalDays//365
# print(totalYears)
# #以1970年为基准，time.time()返回的是秒数


# import turtle
# import math
# 定义多个点坐标
# x1,y1=100,100
# x2,y2=100,-100
# x3,y3=-100,-100
# x4,y4=-100,100
#
# 绘制
# turtle.penup()
# turtle.goto(x1,y1)
# turtle.pendown()
# turtle.goto(x2,y2)
#
# turtle.goto(x3,y3)
# turtle.goto(x4,y4)
# #计算起点与终点距离
# distance=math.sqrt((x1-x4)**2+(y1-y4)**2)
#
# turtle.write(distance)
# turtle.done()#让程序在运行完后窗口保持
# a=True
# b=False
# print(a+b)
#
# if("False"):
#     print(a)
# d=10<30 and 50<100
# print(d)#值为1
# print(d-3)
#
#
# f=250
# e=50<f<500#在py中可以这样连用，不像C
# g=50<f and f<500
# print(e,g)


# a='i\nlove\ny'
# b='ni\thao\tma'
# c='i\'m TOM'
# print(a)
# print(b)
# print(c)
# print('hello',end='***')
# print('wisqouj')

# name=input("Enter your name:")
# print('your name is '+name)    #相当于scanf

# getting='hello world'
#  a=len(getting)
#  print(a)
# c=str.upper(getting)
# print(c)
#
# upper_string=getting.upper
# print(upper_string)
# greeting = "Hello, World!"
#
#  使用 str.upper() 将所有字符转换为大写
# upper_string = greeting.upper()
# print(upper_string)

# my_tuple = 3, 5, 7
# print(my_tuple)    # 输出： (3, 5, 7)
#
# a=100
# if a>100:
#     print('>')
# else:
#     print('<')

# x = 5
# match x:
#     case 10:
#         print("x 是 10")
#     case 20:
#         print("x 是 20")
#     case _:
#         print("x 是其它数")
# for i in range(3):
#     print(i)
# else:
#     print("循环正常结束")
#
# # 输出:
# # 0
# # 1
# # 2
# # 循环正常结束
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# count=0
# while count<100:
#     print(count)
#     count+=1
# keys_dict=["姓名","年龄","学校"]
# value_dict=["邱海宏","19","GDUT"]
# my_dict=dict(zip(keys_dict,value_dict))
# print(my_dict)
# #{'姓名': '邱海宏', '年龄': '19', '学校': 'GDUT'}
#
# if "姓名" in my_dict:
#     print("姓名 在字典中")
#
# print(my_dict["学校"])#输出学校的值：GDUT
# # 更新年龄
# my_dict["年龄"] = 35
# # 添加职业
# my_dict["职业"] = "工程师"
#
# name=my_dict.setdefault("姓名","other")
# print(my_dict)
# #{'姓名': '邱海宏', '年龄': 35, '学校': 'GDUT', '职业': '工程师'}
#
# del(my_dict["年龄"])
# print(my_dict)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
#
# # 使用 update 方法
# another_dict = {'e': 5, 'f': 6}
# my_dict.update(another_dict)
# print(my_dict)
#
# # 使用 pop 方法
# value = my_dict.pop('f')
# print(value)
# print(my_dict)
#
# # 使用 clear 方法
# my_dict.clear()
# print(my_dict)

# my_set = {1, 2, 3, 4}
# print(my_set)  # 输出：{1, 2, 3, 4}
#
# my_list = [1, 2, 2, 3, 4, 4, 5]
# my_set = set(my_list)
# print(my_set)  # 输出：{1, 2, 3, 4, 5}
#
# # 创建一个空集合
# empty_set = set()

# 定义函数
# def compute_stats(numbers):
#     length = len(numbers)
#     total = sum(numbers)
#     average = total / length
#     return length, total, average
#
# # 使用函数
# numbers = [10, 20, 30, 40, 50]
# length, total, average = compute_stats(numbers)
#
# print(f"长度: {length}")
# print(f"总数: {total}")
# print(f"均值: {average}")
# for i in range(5):
#     print(i)
# print(f"最后一次迭代中，i = {i}")

# sum_n = lambda x, y: x + y
#
# print(sum_n(1, 2))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(list(filter(lambda x: x % 2 == 1, a)))

