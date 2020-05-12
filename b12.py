import re
value = []
items=[x for x in input("nhap mat khau:").split('.')]
#############
for p in iteams:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\a",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))
