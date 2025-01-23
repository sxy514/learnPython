# Python变量
# 变量在你首次为其分配值时创建
X = 1
print(X)
# 变量不需要使用任何特定类型声明, 甚至可以在设置后更改其类型
y = 5
y = "更改成了字符串"
print(y)

# 类型转换,如果要指定变量的数据类型, 可以用强制转换来完成
xa = str(3)
xb = int(3)
xc = float(3)
print(xa,xb,xc)

# 获取类型
# 你可以使用该函数获取变量的数据类型: type()
ya = 5
yb = "Hello"
print(type(ya))
print(type(yb))

# 单引号还是双引号?
# 可以使用单引号或双引号来声明字符串变量,效果一样
za = 'hi'
zb = "hi"

# Python变量名称区分大小写
a = 4
A = "Sally"
# A不会覆盖a

# Python 变量名称
"""
    命令规则如下:
        变量名称必须以字符或下划线字符开头
        变量名称不能用数字开头
        变量名称只能包含字母数字和下划线
        变量名区分大小写
        变量名称不能为任何Python关键字
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# 多单词的变量名称可以用以下命名规则:
# 驼峰命名, 除第一个单词外,其他单词首字母大写
myVariableName = "a"
# 帕斯卡命名,每个单词首字母大写
MyVariableName = 1
# 蛇型命名, 每个单词之间用下划线隔开
my_variable_name = 1

# 变量也支持多个赋值,注意确保变量的数量和值的数量匹配, 否则会报错
x1,x2,x3 = 1,2,3
print(x1,x2,x3)
# 也可以将一个值分配给多个变量
y1 = y2 = y3 = "same"
print(y1,y2,y3)

# 打开一个集合
# 如果你在列表\元组等中有一个值集合,Python运行你将值提取到变量中,这被称为解包
fruits = ["apple","orange","banana"]
b1,b2,b3 = fruits
print(b1,b2,b3)

# Python 输出变量
# 通常使用print()函数来输出内容
print(X)
# 在函数中输出多个变量则使用逗号分隔:
print(x1,y2)

# Python 全局变量
# 在函数外部创建的变量被称为全局变量,知识点为变量的作用域
# 全局变量可以被所有人使用, 包括函数和外部
# 在函数外部创建变量,然后在函数内调用它
xquanju = "全局变量"
def myfunc():
    print("调用了xquanju"+ xquanju)

myfunc()
# 如果在函数内创建了和外部同名的变量, 则此变量会为局部的,并且只能在函数内使用,全局变量的值保持不变
xqu2 = "外部全局变量"
def myfunc2():
    xqu2 = "函数内同名变量"
    print("调用了"+ xqu2)

myfunc2()
print("调用了xqu2"+ xqu2)
# 这个例子看到了Python的特点,xqu2并没有被函数内的同名变量影响,保持原值

# global 关键字
# 通常,当你在函数中创建变量时, 该变量为local,并且只能在该函数中使用
# 要在函数内创建全局变量, 可以用关键字 global来创建
def myfunc3():
    global xinfunc
    xinfunc = "函数内的全局变量"

myfunc3()

print("调用xinfunc"+ xinfunc)
# 另外,如果要在函数内更改全局变量的值,也使用global关键字,比如:
xwb = "要被修改的外部全局变量"

def myfunc4():
    global xwb
    xwb = "在函数内被修改"

myfunc4()
print("xwb的值" + xwb)
