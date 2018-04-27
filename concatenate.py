def concatenate(first,last):
    firstpart = []
    lastpart = []
    for char in first:
        if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            firstpart.append(char)
        else:
            pass
    for char in last:
        if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            lastpart.append(char)
        else:
            pass    
    firstpart = ''.join(firstpart)
    lastpart = ''.join(lastpart)
    concatenation = firstpart + "." + lastpart
    return(concatenation)

print(concatenate("Amethyst","O'Connell"))
