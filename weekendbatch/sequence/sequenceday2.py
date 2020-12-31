myTuple=(1,'abhishek')
myList=[1]
# myTuple[0]='ravi'
myList[0]=3
# mutable vs imutable
# list   tuple
# byte  bytearray
# str='abhishek'
# str[0]='ll'

#range(0,10,1)
# myStudent=['shrni','shani']
# for student in myStudent:
#     print(student)
# studentList=[]
# studentList.append()
# studenDetails={"stDetails":studentList}
# for  i in range(1,11,1):
#     print("i===",i)
# studenDetails={"stDetails":studentList}
phyMarks=[12,13,14]
data=min(phyMarks)
print(data)
studentList=[]
studentDetails={}
for i in range (0,2):
    name = input('enter your name')
    email = input('enter student email')
    studentList.append(name)
    studentList.append(email)
studentDetails={"student":studentList}
print("studentDetails",studentDetails)
