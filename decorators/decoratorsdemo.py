# def  hello(name="abhi"):
#     return "hello"+name
#
#
# # print(hello())
# greetMe=hello
# print(greetMe())
#returnin function
# def hello(name="abhi"):
#     print('hello abhi')
#     def greet():
#         return 'this string inside greet'
#     def welcome():
#         return "this string inside welcome"
#     print(greet())
#     print(welcome())
#     if name=='abhi':
#         return greet
#     else:
#         return welcome
#
#
# myfunc=hello()
# print(myfunc())
# welcome()

#function as a argument
# def hello():
#     return 'hi abhi'
# def other(func):
#     print("hello")
#     print(func())
#
# other(hello)
# hello(10)
# def  new_decorator(func):
#     def wrap_func():
#         print("before executing a function")
#         func()
#         print("func called ")
#     return wrap_func
# @new_decorator
# def func_needs_decorator():
#     print("func need decorator")
# # func_needs_decorator=new_decorator(func_needs_decorator)
# func_needs_decorator()

#decorator
