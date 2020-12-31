print('write in the file and plese enter stop for exit')

f=open('myfile.txt','w')

while str !='stop':
    str=input()
   # f.write(str+"\n")
    if(str!='stop'):
        f.write(str+"\n")
f.close()
