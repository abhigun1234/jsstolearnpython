# def hello(name):
#     name='abhishek'
#     print('hello',name)
#
# name='raj'
# hello(name)
# print(name)

# str='abhishek'
# str[0]=12


# pass by value or pass by ref
# def modify(name):
#     name='ravi';
#     print(name,id(name))
#
# name='abhishek'
# modify(name)
# print(name, id(name))

def modify(myList):
    myList.append('abhishek')
    print(myList,id(myList))


myList=['ravi']
modify(myList)
print(myList, id(myList))

# def printinfo( name, age ):
#    "This prints a passed info into this function"
#    print( "Name: ", name)
#    print ("Age ", age)
#    return;
#
# # # Now you can call printinfo function
# printinfo( 50, 'abhishek' )# keword argument




def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# # Now you can call printinfo function
printinfo( age=5, name="miki" )
# printinfo( name="raj" )
 //*args
# Function definition is here
def printinfo( *vartuple ):
   "This prints a variable passed arguments"
   print( "Output is: ",vartuple)
   # print( arg1)
   # for var in vartuple:
   #    print( var)
   return;
printinfo( 'abhi' )
printinfo( 'ravi','rt' )
printinfo( 'a','c','b')