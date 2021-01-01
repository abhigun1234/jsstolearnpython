import operators.modules.moduleb as mod


mod.func()
print("__name__",__name__)
if __name__ =='__main__':
    print("modulea running directly")
else :
    print("modulea imported")
