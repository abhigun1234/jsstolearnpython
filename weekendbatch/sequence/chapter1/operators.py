#aretemetic operators


# + - / * ** %
# print('enter a no and check the no is even or odd')
# a=int(input('enter a no '))
# reminder=a%2
# print("result",reminder)
# if(reminder==1):
#     print('it is a odd no')
# else :
#     print("it is a even no ")
# result=a+b
# print(result)
# result=a*b
# print(result)

#if

'''
docstring
'''

'''
elif logical operators

'''
name=input('enter user name')
age=int(input('enter user age'))
city=(input('enter your city'))
ticketPrice=2000
discount=0
if age<5:
    discount=ticketPrice*10/100
    if city=='pune':
        print('you are not eligible for the discount')
elif age>5 and age <55:
    discount=ticketPrice*5/100
elif age>70:
    discount=ticketPrice*20/100

print('discount ',discount)









