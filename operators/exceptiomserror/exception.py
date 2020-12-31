# i=0
# b=2
# c=b/i
# print(c)
#

# mylist=[1,2,3]
# print(mylist1)
# try:
#   f=open('simple1.txt','w')
#   f.write('test write to simple text')
# except  IOError:
#     print("Error:")
# finally:
#     print('it will exicute every time')
# else:
#     print("sucsess")
#     f.close()
try:
    f = open('simple1.txt', 'r')
    f.write('test write to simple text')
except IOError:
     print("there is in readin the file ")
finally:
    print("its execute every time")
print("hello ")
a=0
print("a",a)