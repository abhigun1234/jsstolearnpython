class Person :
    id = 1
    name = ''
    dob = ''
    age = 12
    studentData=[]
    # intilizer and its working like constructor in the languge like c++ java
    def __init__(self,_id,name,dob,age):
        # self.id=12
        # self.name='ravi'
        # self.dob='12-2-2013'
        # self.age=12
        self.studentData.append(name)
        self.id=_id
        print(self.id)
        print('init called')

    '''
    model
   data members of the class  state or attribute
    '''


    '''
    action or behiviour 
    '''

    def setName(self,name):
        print("name",name)

    def getName(self):
        return self.name

#object of the class

##  take input from user
p1=  Person(12,'raj','12-2-1986',12)
p2=  Person(13,'abhi','12-2-1986',12)
print("date of birth is",p1.dob)
print("name of the person is",p1.name)
print("age of the person is",p1.age)
print("studentdata",p1.studentData)

