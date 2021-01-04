# # function defination
# def hello(year):
#     print('argumnt',year)
#     print("hello every on welchonome to the year ",year)
#     if year==2020:
#         print('this was a corona year')
#     else:
#         print('corona is over now enjoy')
#
# # function calling
#
# year=int(input('enter the year'))
# hello(year)
# def offer(season):
#     if season== 'diwali':
#         print("20% Discount")
#     else:
#         print("25% Discount")

# stusent list add data through function
# student_list=[]
# studetData={}
#
# def addStudenData(name,address,phone_no):
#     student_list.append(name)
#     return student_list
#
# name=input('enter student name')
# address=input('enter address')
# phone_no=input('enter phone no')
# student_list=addStudenData(name,address,phone_no)
# studentData={"studentsta":student_list}
# print('studentData',studentData)

# pass by value or pass by ref
# def modify(name):
#     name='ravi';
#     print(name,id(name))
#
# name='abhishek'
# modify(name)
# print(name, id(name))
#
# def modify(myList):
#     myList.append('abhishek')
#     print(myList,id(myList))
# def modify(str):
#     # myList.append('abhishek')
#     # print(myList,id(myList))
#     str='bye'
#     print(id(str))


# myList=['ravi']
# modify(myList)
# print(myList, id(myList))
# str='hello'
# modify(str)
# print(id(str))

# def printinfo( name, age ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age ", age)
#    return;
#
# # # Now you can call printinfo function
# printinfo( age=5, name="miki" )
# # printinfo( name="raj" )

# def hello():
#    return
#
#
# data=hello()
# print(data)

#  #*args
# # Function definition is here
# def printinfo( *vartuple ):
#    "This prints a variable passed arguments"
#    print( "Output is: ",vartuple)
#    # print( arg1)
#    # for var in vartuple:
#    #    print( var)
#    return;
# printinfo( 'abhi' )
# printinfo( 'ravi','rt' )
# printinfo( 'a','c','b')
# #
#[] () {}

def add(*num):
    print("num",num)
    result=0
    for no in num:
        print('no',no)
        result=result+no
    print(result)



add(1,2)
add(1,2,3)
add(1,2,3,4,5)