#  str is set char
# myname="abhishek"
# print(myname[:-4])
# # imutable
# # myname[0]='b'
# elements=[10,20,13,13,35]
# x=bytes(elements)
# print(x[2])
# x[1]=12
# elements=[10,20,13,13,35]
# x=bytearray(elements)
# print(x[2])
# x[2]=45
# print(x[2])
myAddress=['pune','maharashtra']
print(myAddress)
myAddress[0]='mumbai'
print(myAddress)
# append
myAddress.append('mulund')
newAddress=['delhi','karolbag']
print(myAddress)
# myAddress.append(newAddress)
# print(myAddress)
myAddress.extend(newAddress)
print(myAddress)
input('enter your name')
