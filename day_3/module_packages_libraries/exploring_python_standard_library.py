import builtins

for name in dir(builtins):
    if name[0].islower():
        print(name)