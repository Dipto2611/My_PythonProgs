l=[22,14,19,65,82,55]
v=1
def mystery(l,v):
  
  if len(l) == 0:
    return (v)
  else:
    return (mystery(l[:-1],l[-1]+v))

x=mystery(l,v)
print(x)
