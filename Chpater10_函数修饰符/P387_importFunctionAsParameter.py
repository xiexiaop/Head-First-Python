# def apply(func: object, value: object) -> object:
#     return func(value)

# # print是一个函数
# apply(print, 42)


# # ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
# # 接受一个参数列表
# def myfunc(*args):
#     for a in args:
#         print(a, end=' ')
#     if args:
#         print(args)

# myfunc(1)
# myfunc(10,20,30,40)
# values=[1,2,3]
# myfunc(values)
# myfunc(*values)

# # ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
# # 接受一个字典参数
# def myfunc2(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v, sep='->', end=' ')


# myfunc2(a=10, b=20)
# dictValue = {'key': 10, 'value': 20}
# myfunc2(**dictValue)

# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
# 创建一个函数可以接受任意多的参数
def myfunc3(*args,**kwargs):
    if args:
        for a in args:
            print(a,end=' ')
    if kwargs:
        for k,v in kwargs.items():
            print(k, v, sep='->', end=' ')
    print()

myfunc3(1,2,3,a=10,b=10,c=30)
myfunc3(1,2,3)
myfunc3(a=10,b=10,c=30)