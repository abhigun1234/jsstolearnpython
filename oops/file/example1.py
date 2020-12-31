
try:
    f = open("demofile.txt", "r")
except Exception as e: print("error1222",e)

print(f.read())


