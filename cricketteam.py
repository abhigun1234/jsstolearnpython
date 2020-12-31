cricketTeam={}
myTeam=[]
for i in range(3):
    name=input("enter cricketer name")
    age=input("enter cricketer age ")
    score=input("enter score")
    print(name)
    print(age)
    print(score)
    cricketTeam.update({'name':name,'age':age,'score':score})
    myTeam.append(cricketTeam)
    print(cricketTeam)
    print(myTeam)