# A program to demonstrate type casting of fundamental data types.

# float, bool, str, complex data type to int
print('float, bool, str, complex data type to int')
print(int(11.99))
print(int(True))
print(int(False))
# print(int("11.11")) 
print(int("11"))
# print(int('ABC'))
# print(int(12 + 23j))

# int, bool, str, complex data type to float
print('int, bool, str, complex data type to float')
print(float(12))
print(float(True))
print(float(False))
print(float('11.11'))
print(float('12'))
# print(float('ABC'))
# print(float(11 + 12j))

# int, float, str, complex data type to bool
print('int, float, str, complex data type to bool')
print(bool(12))
print(bool(0.001))
print(bool(0))
print(bool(11.11))
print(bool(''))
print(bool('ABC'))
print(bool('False'))
print(bool('0'))
print(bool(11 + 34j))

# int, float, bool, complex data type to str
print('int, float, bool, complex data type to str')
print(str(11))
print(str(11.23))
print(str(False))
print(str(True))
print(str(11 + 34j))
print(str(0xAb + 12.5j))

# int, float, bool, str type to complex
print('int, float, bool, str type to complex')
print(complex(11))
print(complex(12.23))
print(complex(0))
print(complex(True))
print(complex(False))
# print(complex(''))
print(complex('19'))
print(complex('22'))
print(complex(87, 11))
print(complex(65.67, 322))
# print(complex(11, '12'))
# print(complex('12', 11))
print(complex('11'))
print(complex(True, False))

# Output
# float, bool, str, complex data type to int
# 11
# 1
# 0
# 11
# int, bool, str, complex data type to float
# 12.0
# 1.0
# 0.0
# 11.11
# 12.0
# int, float, str, complex data type to bool
# True
# True
# False
# True
# False
# True
# True
# True
# True
# int, float, bool, complex data type to str
# 11
# 11.23
# False
# True
# (11+34j)
# (171+12.5j)
# int, float, bool, str type to complex
# (11+0j)
# (12.23+0j)
# 0j
# (1+0j)
# 0j
# (19+0j)
# (22+0j)
# (87+11j)
# (65.67+322j)
# (11+0j)
# (1+0j)