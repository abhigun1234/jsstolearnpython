# function defination
def hello(year):
    print('argumnt',year)
    print("hello every on welcome to the year ",year)
    if year==2020:
        print('this was a corona year')
    else:
        print('corona is over now enjoy')

# function calling

year=int(input('enter the year'))
hello(year)