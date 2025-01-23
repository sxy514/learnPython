# Python 字符串
# 在python中使用单引号或者双引号括起来表示字符串
# 'hi' 和 "hi"相同

# 引号内的引号
# 你可以在字符串中使用引号,只要它们不与字符串周围的引号相同:
print("It's alright")
print("He is called 'john'")
print('He is called "John"')

# 将字符串赋值给变量
a = "hi"
# 将多行字符串赋值给变量, 单引号也可以表示, 输出将按照多行字符的格式来
a1 = """
        Lorem ipsum dolor sit amet,
        consectetur adipiscing elit,
        sed do eiusmod tempor incidid
    """
print(a1)


# 字符串是数组
# 与其他流行的编程语言一样, Python中的字符串是表示unicode字符的字节数组
# 但是python没有字符数据类型, 单个字符知识长度为一的字符串
# 方括号可用于访问字符串中的元素

# 获取位置1的字符
c = "hello,world"
print(c[1])


# 遍历字符串
# 由于字符串是数组, 我们可以通过for循环遍历字符串内的字符
for x in "banana":
    print(x)


# 获取字符串长度
# 使用len()函数返回字符串长度
nstr = "Hello,World"
print(len(nstr))


# 检查字符串
# 检查字符串中是否存在某个短语或字符, 我们可以用关键字 in
txt = "The best things in life are free"
print("free" in txt)   # 返回bool值

# 现在我们修改以下代码, 当存在"free"时输出
if "free" in txt:
    print("Yes, 'free' is present.")
# 那么要检查字符串中是否不存在某个短语或字符, 我们可以使用关键字 not in
print("expensive" not in txt)
# 修改代码, 当 expensive不存在时输出
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")
