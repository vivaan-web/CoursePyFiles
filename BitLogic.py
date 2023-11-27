def andFunc(op1, op2):
    return op1 and op2

def notFunc(op1):
    return not op1

def orFunc(op1, op2):
    return not (andFunc(not op1,not op2))

print(orFunc(1,1))
print(orFunc(0,1))
print(orFunc(1,0))
print(orFunc(0,0))

