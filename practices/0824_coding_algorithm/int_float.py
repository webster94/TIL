str = '123'
str2 = '12.3'

print(int(str), type(int(str)))


test = '1+2'
print(test)
print(repr(test))
print(eval(repr(test)))
print(eval(eval(repr(test))))
