
def add(a,b):
    len1 = len(a)
    len2 = len(b)
    if len1 > len2:
        b = '0'*(len1 - len2) + b
    elif len2 > len1:
        a = '0'*(len2 - len1) + a
    op1 = [int(x) for x in a[::-1]]
    op2 = [int(x) for x in b[::-1]]
    c = 0
    result = ''
    for x, y in zip(op1, op2):
        s = (x+y+c)%10
        c = (x+y+c)/10
        result += str(s)
    if c:
        result += str(c)

    return result[::-1]


def prod(a,b):
    operand = [int(x) for x in a[::-1]]
    multiplier = [int(x) for x in b[::-1]]

    print operand, multiplier
    output = []
    tens = 0
    for y in multiplier:
        result = ''
        c = 0
        for x in operand:
            p = ((x*y)+c)%10
            c = ((x*y)+c)//10
            result += str(p) 
        if c: 
            result += str(c)
        result = result[::-1] + '0'*tens
        tens += 1
        output.append(result)
    
    a = ''
    for b in output:
        a = add(a,b)
    
    return a

print prod('235','324')



        


        
