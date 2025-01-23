# Python中有三种数字类型:
# int, float, complex

# 整数类型
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

# 浮点
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# 复数
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# 类型转换
x1 = 1    # int
y1 = 2.8  # float
z1 = 1j   # complex

# int to float
a = float(x1)
# float to int
b = int(y1)
# int to complex
c = complex(x1)
print(a,b,c)
print(type(a),type(b),type(c))
#注意: 您不能将复数转换为其他数字类型。转为complex后无法转为其他数字类型

# 随机数
# Python有一个内置模块random来制作随机数
import random
print(random.randrange(1,10))


