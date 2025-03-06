def solution(a, b):
    var1 = str(a) + str(b)
    var2 = 2*int(a)*int(b)
    
    if int(var1) > var2:
        return int(var1)
    
    elif int(var1) == var2:
        return int(var1)
    
    else:
        return var2