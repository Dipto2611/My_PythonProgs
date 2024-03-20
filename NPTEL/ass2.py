def remdup(l):
  L=[]
  for ips in l:
    if ips not in L:
      L.append(ips)
  return(L)

def sumsquare(l):
  odd_sum=0
  even_sum=0
  for ats in l:
    if ats%2!=0:
      odd_sum+=ats*ats
    else:
      even_sum+=ats*ats
  return([odd_sum,even_sum])

def transpose(m):
  ans=list()
  for ind in range(len(m[0])):
    a=[]
    for j in range(len(m)):
      a.append(m[j][ind])
    ans.append(a)
  return(ans)


# print (remdup([3,1,3,5]))
# print (remdup([7,3,-1,-5]))
# print (remdup([3,5,7,5,3,7,10]))
# print (sumsquare([1,3,5]))
# print (sumsquare([2,4,6]))
# print (sumsquare([-1,-2,3,7]))
# print (transpose([[1,2,3],[4,5,6]]))
# print (transpose ([[1],[2],[3]]))
# print (transpose([[3]]))




