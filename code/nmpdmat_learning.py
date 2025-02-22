import numpy as np
import pandas as pd

# np_array=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# print(np_array)
# print(np_array.shape)
#
#
# zeros_array=np.zeros((2,3))# 创建一个 2x3 的零矩阵
# ones_array=np.ones((3,4)) # 创建一个 3x4 的单位矩阵
# range_array=np.arange(10)# 创建一个元素值从 0 到 9 的数组
# random_array=np.random.randint(0,4,(3,4))# 创建一个 3x4 的矩阵，元素都是 0 到 4 的随机整数
# print(zeros_array)
# print(ones_array)
# print(range_array)
# print(random_array)
# element = np_array[0]  # 获取第一个元素
# print(element)
# # 创建一个 3x3 的二维数组
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
# # 访问第二行第三列的元素
# print(arr[1, 2])
# # 访问第二行
# print(arr[1, :])
# # 访问第三列
# print(arr[:, 2])
#
# # 访问子矩阵（前两行，前两列）
# print(arr[:2, :2])

# 创建两个矩阵
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])
#
# # 矩阵加法
# addition = A + B
# print("矩阵加法 A + B:\n", addition)
#
# # 矩阵减法
# subtraction = A - B
# print("\n矩阵减法 A - B:\n", subtraction)
#
# # 矩阵乘法（叉乘）
# elementwise_multiplication = A * B
# print("\n矩阵叉乘 A * B:\n", elementwise_multiplication)
#
# # 矩阵乘法（点乘）
# dot_product = np.dot(A, B)
# print("\n矩阵点乘 A dot B:\n", dot_product)
#
# # 矩阵除法（元素对元素）
# elementwise_division = A / B
# print("\n矩阵元素对元素除法 A / B:\n", elementwise_division)
# c=np.array([[1,2],[3,7],[8,9]])
# print(c)

# A=np.array([[1,0,0],[0,2,0],[0,0,3]])
# B=np.array([[9,8,7],[6,5,4],[3,2,1]])
# print("矩阵A",A)
# print("矩阵B",B)
# #矩阵转置
# A_T=A.T
# B_T=B.T
# print(A_T)
# print(B_T)
#
# #尝试求矩阵的逆
# try:
#     inverse_A=np.linalg.inv(A)
# except np.linalg.linalg.LinAlgError:
#     inverse_A="A不可逆"
#
# try:
#     inverse_B=np.linalg.inv(B)
# except np.linalg.linalg.LinAlgError:
#     inverse_B="B不可逆"
#
# print("A的逆矩阵",inverse_A)
# print("B的逆矩阵",inverse_B)
# A=np.array([[1,2,3],[4,5,6],[7,8,9]])
# B=np.array([2])
# print(A*B)


# data={'name':['qhh','zmy','czm','kyt'],#看作两个键，每个键各三个值，也可以看作两列三行
#       'age':['19','20','21','22']}
#
# df=pd.DataFrame(data)
# print(df)


data = {'Name': ['刘备', '关羽', '张飞'],
        'Age': [40, 35, 30],
        'City': ['涿郡', '解县', '涿郡']}
df = pd.DataFrame(data)

df.set_index('City',inplace=True)
print(df.iloc[0])
print(df.iloc[0,1])
