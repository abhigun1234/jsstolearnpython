f = open("welcome", "a")
f.write("nksbkdbsjkbdjsdj ")
f.close()

#open and read the file after the appending:
f = open("welcome", "r")
print(f.read())

# pip install numpy