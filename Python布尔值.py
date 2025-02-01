# 布尔类型值有两个, True和False
# 当你比较两个值时,将计算表达式并返回布尔值
print(10>6)

# 当你在if语句中运行条件时, 会返回bool值
if 5 > 2:
    print("true")
else:
    print("false")

# 评估值和变量
# bool() 方法运行你评估任何值
print(bool("Hello"))
print(bool(15))

# 大多数值结果都为True
# 除空字符串外,任何字符都是True
# 除了0 ,任何数字都是true
# 任何列表、元组、集合和字典都是true，除了空的
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


# 某些值的结果为False
# 值为0或者空的就是false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# 还有一个值，或者这个例子中的对象，返回值为0，如果你有一个对象是由一个函数返回或的类组成的
class myclass():
    def __len__(self):
        return 0

myobj =  myclass()
print(bool(myobj))


# 函数可以返回布尔值, 你可以创建返回bool值的函数
def myfunc():
    return True

print(myfunc())
# 然后根据函数的结果来执行代码
if myfunc():
    print("yes")
else:
    print("no")


# Python还具有许多返回布尔值的内置函数, 比如 siintstance(), 可以用来确定对象是否属于特定数据类型:
x = 200
print(isinstance(x))

