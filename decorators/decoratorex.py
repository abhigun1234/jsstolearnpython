def decor(fun):
    def inner():
        value=fun()
        return  value +2
    return  inner
@decor
def num():
    return 10
# what is decoraror how to write decorator
# def getName():
#     return 'akash'
print(num())

# result_func=decor(num)
# print(result_func())

# def greet(fun):
#     def inner():
#         value=fun()
#         return "welcom " +value
#     return  inner
#
# def hello():
#     return "abhishek"
#
# result=greet(hello)
# print(result())
#

# def greet(fun):
#     def inner():
#         value=fun()
#         return "welcom " +value
#     return  inner
# @greet
# def hello():
#     return "abhishek"

# result=greet(hello)
# print(result())
# print(hello())
#
