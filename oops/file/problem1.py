f=open('myfile.txt','w')
print('Enter  text(@ at end)):')
while str !='@':
    str=input()
    f.write(str+"\n")
    if(str!='@'):
        f.write(str+"\n")
f.close()
