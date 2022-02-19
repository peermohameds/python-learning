def listhelp(inputobject):
    for att in dir(inputobject):
        print(att, getattr(inputobject, att))
