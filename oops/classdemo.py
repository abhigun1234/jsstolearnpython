class Employees:
    'Common base class for all employees'
    empCount = 0
    empData=[]


    def __init__(self):
        print('init called')


    def displayCount(self):
        print
        ("Total Employee %d" % Employees.empCount)

    def displayEmployee(self):
        print
        ("Name : ", self.name, ", Salary: ", self.salary)
    def addEmp(self,name):
        self.empData.append(name)
    def getEmpData(self):
        return self.empData


emp1 = Employees()
name=input('enter your name')
phone_no=input('enter  phone no')
emp1.addEmp(name)
data=emp1.getEmpData()
print(data)
print(emp1.empCount)

