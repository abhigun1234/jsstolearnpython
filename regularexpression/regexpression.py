import  re
str='man sun mop run maan maap '
result =re.match(r'm\w\w\w',str)
print(result)