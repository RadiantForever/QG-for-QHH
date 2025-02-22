# python基础知识

![6e8e96b795b890d1c73d884d2270a6a](https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250202174835229.png)

相比C语言，python的分块采用为缩进划分

print后面不用加;

一个tab自动缩进四个空格

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250202175427001.png" alt="image-20250202175426956" style="zoom:50%;" />

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250202175827784.png" alt="image-20250202175827709" style="zoom: 33%;" />

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250202175929823.png" alt="image-20250202175929744" style="zoom:33%;" />

ctrl加上/   单行被注释，再按取消注释

移动鼠标选中多行，c加/注释多行<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250202181031873.png" alt="image-20250202181031818" style="zoom: 50%;" />

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250203105238937.png" alt="image-20250203105238797" style="zoom: 25%;" />

\为行连接符

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250216113402481.png" alt="image-20250216113402303" style="zoom: 50%;" />

py中的整数无限大，不用考虑整数溢出

a=7//2    取整数的÷号，结果是3

314E-2   就是3.14 意思是314乘以10的-2次方

divmod(13,3)     get (4,1)   同时得到商和余数

![ca3e8d8b60a7b48af1e8fb59efb163f](https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250216114833910.jpg)

相当于c里的强制转换

round（value）可以返回四舍五入的值，但不会改变原有值，而是产生新的值



# 字符串

len(xxx)计算字符串

- str.upper(): 将所有字符转换为大写。
- str.lower(): 将所有字符转换为小写。
- str.startswith(prefix): 检查字符串是否以特定前缀开始。
- str.endswith(suffix): 检查字符串是否以特定后缀结束。
- str.find(sub): 返回子字符串首次出现的索引，如果未找到则返回-1。
- str.replace(old, new): 将所有出现的旧子字符串替换为新子字符串。
- str.split(delimiter): 根据指定的分隔符分割字符串。
- str.join(iterable): 使用字符串作为分隔符连接可迭代对象中的字符串。

对象的方法，在使用上，与操作数据的函数的主要区别在于，函数操作一个数据的时候，是把数据作为参数，放在函数名后面的括号中使用，比如 `len(greeting)`；数据对象的方法也是个函数，但是在调用它的时候，先要把表示数据对象的变量写在前面，然后加一个点，在把方法函数写在点后面，比如 `greeting.upper()`。

![image-20250216193904288](https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250216193904346.png)

如果不想让反斜杠起到转义作用，可以使用原始字符串。在字符串前加上 r 或 R，使其成为原始字符串，这样就不会对字符串中所有的 `\` 进行转义。比如设置读取文档路径时使用

### 字符串格式化是将特定的值插入到字符串的某些位置的过程。

![image-20250216195658855](https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250216195658891.png)

# 列表(相当于C语言中的可变数组)，元组（const修饰的不可更改数组）

创建列表的方法是，使用方括号 `[ ]`，在方括号内放置列表的元素，元素之间用逗号分隔，也可以使用 list() 函数创建列表

![image-20250216200423463](https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250216200423498.png)

##### 反向切片

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250216200600873.png" alt="image-20250216200600839" style="zoom:50%;" />

解包，把列表中的元素“解包”（即分解）到变量中的方法。<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250216200847390.png" alt="image-20250216200847355" style="zoom:33%;" />



部分解包：使用一元 '*'运算符来表示“剩余的所有元素

a,b,*rest=number

- append() - 向列表末尾添加一个元素。
- extend() - 将另一个列表（或任何可迭代对象）的元素添加到当前列表的末尾。
- insert() - 在指定索引处插入一个元素。
- remove() - 删除指定的元素。
- pop() - 删除指定索引处的元素并返回它，如果不指定索引，就删除数组的最后一个元素。这个方法与 remove() 的区别在于，remove() 的输入是一个元素的值，pop() 的输入是一个元素的索引。

# IF

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250216204118900.png" alt="image-20250216204118852" style="zoom:50%;" />

**<u>调试</u>**代码时，如果什么都不需要执行，不要注释掉if，这样会报错，可以使用 `pass` 关键字，它是一个占位语句，实际上什么都不做

使用 `elif` 关键字代替 `else if`

py中的switch case

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250216204805684.png" alt="image-20250216204805636" style="zoom:50%;" />

range(x,y,z),x为开始，y为结束，z为步长，在集合[x,y)中，区间左闭右开。

for 循环可以带一个 else 块，当循环正常完成（没有被 break 语句中断）时执行。

# 字典与集合

字典是一种集合，集合中每个元素是一对“键”和“值”。在表示字典的时候，字典本身是使用大括号包裹，内部的元素使用逗号分隔，每个元素内部的键和值通过冒号   ：  分隔。创建一个字典最简单的方法是使用大括号，包所需键值数据包裹起来。

## 需要注意的是：

- ### 字典的键必须是不可变类型，如整数、浮点数、字符串或元组。列表或其他字典不能作为键使用。这是为了避免键被修改，引起查找字典时出现混乱。

- ### 字典的键是唯一的，如果重复添加相同的键，后一次添加的值会覆盖前一个值。

- ### 字典的值可以是任何类型，包括其他字典或列表。

使用 dict() 函数可以从其他数据结构创建字典。

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250216215205087.png" alt="image-20250216215205042" style="zoom: 67%;" />

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250217193426876.png" alt="image-20250217193426770" style="zoom:50%;" />

setdefault() 方法用于获取某个键对应的值，如果键不存在于字典中，则将键及指定的默认值插入到字典中。如果键已经存在，那么它将返回键对应的值，不会改变字典。



![image-20250217193701456](https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250217193701522.png)

使用 keys()、values()、items() 这三个函数可以分别访问字典的键、值和键值对。这些方法都返回的都是字典视图对象，也就是说它们返回的不是固定数据

- dict.update(another_dict): 将另一个字典的键值对合并到当前字典中。
- dict.pop(key): 删除并返回指定键的值。如果键不存在，则引发KeyError。
- dict.clear(): 清除字典中的所有项。

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250217194617343.png" alt="image-20250217194617278" style="zoom:50%;" />

### 集合可以包含任何类型的对象，如数字、字符、其他集合等，但每个元素在集合中必须是唯一的，集合不允许重复元素。

创建集合

使用花括号，或 set() 构造函数来创建集合

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250217195058238.png" alt="image-20250217195058184" style="zoom:50%;" />

- 添加元素： 使用 add() 方法。

- 删除元素： 使用 remove() 或 discard() 方法。remove() 方法在元素不存在时会引发一个错误，而 discard() 方法则不会。

# 函数

函数的定义以 def 关键字开始。

函数头（即函数定义的第一行）必须以冒号结尾。使用 return 语句，可以从函数返回一个值。如果函数不包含 return 语句，它默认返回 None。

相比于C，命名时前面多个一个固定的def

如果函数有多个返回值，实际上返回的是一个元组，可以在调用函数的时候直接以元组拆包的方式直接得到多个返回数据<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250217195922721.png" alt="image-20250217195922647" style="zoom:50%;" />

函数默认参数在函数定义时计算的，只计算一次，而不是每次调用时都重新计算。





# lambda、map、filter

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250217213610498.png" alt="image-20250217213610443" style="zoom: 50%;" />

![image-20250217213638337](https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250217213638391.png)

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250217213738413.png" alt="image-20250217213738364" style="zoom: 67%;" />

map函数可以根据我们指定的函数功能，将若干序元素依次进行处理，最后返回的也是一个序列集合；当序列元素不对等时，不对等部分就不会进行处理。

filter相当于一个筛子，可以将不符合要求的序列元素过滤掉，然后返回一个新的序列

<img src="https://radiantheart.oss-cn-guangzhou.aliyuncs.com/myimage/20250217214125740.png" alt="image-20250217214125697" style="zoom:67%;" />

# 类与对象

**对象**是属于某个类的一个实体，有时会直接被称为**实例**。**属性**也经常被叫做**数据**或者**变量**，是用来描述对象静态状态的。**方法**也经常被叫做**函数**，用来描述对象的动作。

### 封装（数据抽象）

封装是指，把高度相关的一组数据和方法组织在一起，形成一个相对独立的模块。外部程序只能通过严格定义的接口访问这个模块公开的数据和方法；而对于不需要与外部发生联系的数据和方法，则把它们隐藏和保护起来。这样，就避免了编程过程中，模块常常被滥用，导致难以维护的弊病。

比如，需要设计一个用来模拟几个小动物日常生活的程序。在设计程序时，可以把所有小动物的行为和特性抽象归为一个“动物”类。这个类包括了一些公开的属性，如年龄、产地、名字等等；还可以包含一些公开方法，即动物的行为，比如进食、移动、发声等。这个动物类中还有一些内部的属性和方法，它们只能提供类内部使用，而不能被类之外的其它程序调用。比如，让动物走几步，可以通过调用动物类的移动方法，这个方法在内部其实还调用了类的一个私有属性：“腿的数目”，而这个属性是不能够被类之外的程序直接修改或读取的。

### 继承

继承是指，在一个已有的类的基础上，可以生成定义更加细致的**子类**。子类具有原有的类（称为**父类**）的所有公开出来的属性和方法。除此之外，它还有一些特有的更为具体的属性和方法。这使得我们可以定义相似的类型并对其相似关系建模。

比如程序中涉及到几只小狗和几只小鸡，它们都是动物类的实例。但是，小狗们还有它们共有的一些特点。为了使程序代码更好地被重用，这些共同点也应被抽象出来，形成一个子类，“狗”类。

动物类的所有属性和方法，狗类也都具有。所以在定义狗类的时候，先声明它是动物类的一个子类，这样，狗类就立刻具备了所有动物类公开了的属性和方法。再加上狗的一些特殊属性和方法就可以了，比如狗“看家”，鸡“下蛋”等。

子类常常也被叫做**派生类**；父类也可以被称为**基类**、**超类**。父类、父类的父类或更往上的被统称为**祖先类**；相对应，子类、子类的子类或更往下的被统称为**子孙类**或后代类。

### 多态

多态是指同一个方法，在不同子类中具有不同的表现方式。虽然子类具有很多继承自父类的相同的方法，但它们的实现可以是不同的。在调用这些方法时，可以使用父类的名称来调用它们。这样，程序虽然调用了相同的方法，但是因为它们所属的子类不同，其表现行为也会不同。使用多态，可以让我们在应用程序中，在一定程度上忽略相似模块的区别，而以统一的方式调用它们。

比如，几个子类同样都具有一个继承自父类“动物”的方法“发声”。而不同的子类，狗和鸡的“发声”的实现代码是不相同的：狗汪汪，鸡打鸣。这样，在应用程序中需要让一组动物逐个发声时，可以把所有动物都当作是动物类的一个实例，使用相同的代码调用每个实例对应的动物类的“发声”方法。而程序运行到这里，会自动判断要处理的实例是属于“狗”子类还是属于“鸡”子类，然后分别调用狗或鸡类中“发声”方法，或发出汪汪声，或发出唧唧声。