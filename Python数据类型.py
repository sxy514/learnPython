# Python内置的数据类型
"""
    内置的类型有:
    文本类型: str
    数值类型: int,float, complex
    序列类型: list, tuple, range
    映射类型: dict
    Set类型:  set,frozenset
    布尔类型: bool
    二进制类型: bytes, bytearray, memoryview
    无类型:   NoneType
"""

# 获取数据类型, 可使用type()函数来获取任何对象的数据类型
x = 5
print(type(x))

# 创建各类型的变量
x1 = "hi"           # str
x2 = 20             # int
x3 = 20.5           # float
x4 = 1j             # complex
x5 = ["apple","banana"]  # list
x6 = ("apple","banana")  # tuple 元组
x7 = range(6)       # range
x8 = {"name" : "John", "age" : 36}  # dict 键值分别用冒号隔开表示一对
x9 = {"apple","banana"} # set
x10 = frozenset({"apple","banana"}) # frozenset
x11 = True          # bool
x12 = b"Hello"      # bytes
x13 = bytearray(5)  # bytearray
x14 = memoryview(bytes(5))  # memoryview
x15 = None          # NoneType


