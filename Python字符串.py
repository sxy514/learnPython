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


# Python 字符串切片
# 你可以使用切片语法返回需要的字符
# 指定开始索引和结束索引, 用冒号分隔
b = "Hello,World"
print(b[2:5])
# 那么通过省略开始索引就可以从头开始切片字符
print(b[:5])
# 同样的, 省略了结束索引则切片到最后
print(b[2:])
# 若索引为负, 则会从字符串末尾开始切片
print(b[-5:-2])


# Python 修改字符串
# 内置的函数 upper() 将返回大写的字符串
au = "Hello world  "
print(au.upper())
# lower() 函数将返回小写的字符串
print(au.lower())
# 使用函数 strip() 该方法删除开头或结尾的任何空格
print(au.strip())

# 替换字符串, 使用replace()函数可以将一个字符串替换为另一个
print(au.replace("H","j"))

# 拆分字符串使用 split() 函数, 这个方法将返回一个列表,其中指定分隔符
ac = "Hello, World!"
print(ac.split(","))


# 字符串连接,使用 + 号
aconn = "Hello"
bconn = "World"
print(aconn+" "+bconn)


# 字符串格式
"""
    正如在变量章节里学到的, 我们不能像下面这样组合字符串
    a = 20
    b = "I am" + a
    这样会报错, 字符串无法直接和其他类型相加来连接
"""
# 但是我们可以用f-string或者format()函数来实现
# 要将字符串指定为f-string,只需要在字符串签名加上f, 并在变量内添加占位符号{},如下
age = 23
txt = f"my name is john, I'm {age}"
print(txt)
# 占位符可以包含变量,操作,函数和修饰符来格式化值
# 占位符内可以包含用于设置值格式的修饰符
# 通过添加冒号后跟合法格式类型来包含修饰符, 例如表示两位小数的固定浮点数
price = 89
txt = f"The price is {price:.2f} dollars"
print(txt)
# 占位符可以包含python代码, 比如数学运算
txt = f"the price is {20*25} dollars"
print(txt)


# Python 转义字符
# 要在字符串中插入非法字符, 需要使用转义字符, 转义字符是一个反斜杠
# txt = "We are the so-called "Vikings" from the north." 这里的双引号使用错误,导致报错
# 要解决这个问题, 就在非法符号前加上转义符号 \
txt = "We are the so-called \"Vikings\" from the north."
# 转义符有许多:
# \' 单引号
# \\ 反斜杠
# \n 换行
# \r 回车键
# \t 制表符
# \b 退格键
# \f 换页
# \ooo 八进制值
# \xhh 十六进制值


# 字符串相关的方法, 内容过多不赘述
# https://www.w3schools.com/python/python_strings_methods.asp
