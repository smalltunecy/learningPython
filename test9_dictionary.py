name = {'一点水':123231,'两点水':313131}

print(name['一点水'])

name['cy'] = 131313
print(name)

name['一点水']= 0
print(name)
del name['两点水']
print(name)
name.clear()
print(name)