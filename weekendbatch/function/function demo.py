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
student_list=[]
studetData={}

def addStudenData(name,address,phone_no):
    student_list.append(name)
    return student_list

name=input('enter student name')
address=input('enter address')
phone_no=input('enter phone no')
student_list=addStudenData(name,address,phone_no)
studentData={"studentsta":student_list}
print('studentData',studentData)


