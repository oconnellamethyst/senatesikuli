starid = input("Please enter your StarID:")
staridpass = input("Please enter your StarID Password:")
firstname = input("Please enter your first name:")
lastname = input("Please enter your first name:")
def concatenate(firstname,lastname):
    firstpart = []
    lastpart = []
    for char in firstname:
        if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            firstpart.append()
        else:
            pass
        firstpart = []
    for char in lastname:
        if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            lastpart.append()
        else:
            pass
    return(firstpart + "." + lastpart)
    