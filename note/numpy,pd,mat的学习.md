shape 属性表示了数组形状，reshape 可以改变数组形状

![image-20250217220731013](https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250217220731073.png)

![image-20250217220758683](https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250217220758747.png)



![image-20250217221027934](https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250217221028027.png)

![image-20250218103627652](https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250218103627774.png)

# 数组广播

 如果两个数组的维度数不同，那么小维度数组的形状将会在前面补 1，直到与大维度数组的维数相同。相加相乘相当于将小维度数组“复制”成多份，直到对齐

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250218105259917.png" alt="image-20250218105259852" style="zoom:50%;" />

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250218105351479.png" alt="image-20250218105351427" style="zoom:50%;" />



# PD



## DataFrame 数据结构

DataFrame 是一个二维的、表格型的数据结构，可以存储不同类型的列，如整数、浮点数、字符串。

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250218111420220.png" alt="image-20250218111420132" style="zoom:50%;" />



### 读写 CSV, TSV 文件

使用 pd.read_csv() 函数

pd.read_csv() 函数的参数包括：

- filepath_or_buffer： 文件的路径或类似文件的对象。
- sep： 字段分隔符，默认为,。
- header： 用作列名的行号，默认为 0 （第一行）。
- index_col： 用作行索引的列编号或列名。
- usecols： 返回的列的子集。
- dtype： 列的数据类型。

## 把表格数据写入文本文件使用 pd.to_csv() 函数。