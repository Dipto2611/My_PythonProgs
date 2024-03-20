def threesquares(n):
    while n > 0 and n % 4 == 0:
        n =n// 4
    return(n % 8 != 7)

def repfree(s):
    return(len(set(s))==len(s))
  
  
def hillvalley(l):
    dect = False
    inc = False
    c = 0
    for i in range(len(l)-1):
        if c > 1:
            return False
        right = l[i+1]
        middle = l[i]
        diff = right - middle
        if diff > 0:
            if dect:
                c += 1
            inc = True
            dect = False
        elif diff < 0:
            if inc:
                c += 1
            dect = True
            inc = False
    if c == 1:
        return True
    return False