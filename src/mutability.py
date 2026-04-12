num=[1,'two',3]

# The original list will not be modified
def number():
    a=num+[4]
    return a
def alpha():
    b=num+['four']
    return b

print('numeric function:', number())
print('alpha function:', alpha())

# The origianl list will be modified
def number_append():
    c=num.append(5)
    c=num # the original list is modified 
    return c
def alpha_append():
    d=num.append('five')
    d=num # the original list is modified 
    return d

print('numeric append:', number_append())
print('alpha append:', alpha_append())