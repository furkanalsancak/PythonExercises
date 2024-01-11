'''
LEGB
Local, Enclosing, Global, Built-in
'''

# import builtins

# # print(dir(builtins))

# def my_min():
#     pass

# m = min([5,1,4,3])
# print(m)

#x = 'global x' #global variable

def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)
    
    inner()
    print(x)

# def test(z):
#     #global x
#     x = 'local x' #local variable
#     #print(y)
#     print(z)

# test('local z')
# print(y) #cannot access because local
#print(x)

outer()
