# myAddress={'name':'abhishek'}
# value=myAddress['name']
# print(value)
# myAddess={'name':'abhishek','address':['address1']}
# my_dict={"key1":"value"}
# print(my_dict['key1'])
# mydict1={"key1":1234,"key2":"value2",'key3':{'123':[1,2,'abhishek']}};
# mydict1={"key1":1234,"key2":"value2",'key3':{'123':[1,2,'abhishek'],'mykey':[1,2,3,4,['abhi','shrinivas']]}};
# print(mydict1['key3']['mykey'][2])
#
# # myList=[1,2,3,4,5,6,7,['a','b','c']]
# # print(myList[7][1])
# #
# # # print( mydict1['key3']['123'][2]
# #
# #
# # mydict1={"key1":'val1'}
# # print(mydict1['key1']);



mydict1={"key1":'val1',"key2":'val2'}
print(mydict1.keys())
for k1 in mydict1.keys():
    print("key",k1)
    print('val',mydict1[k1])
