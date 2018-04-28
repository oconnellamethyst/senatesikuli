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

# Main Program

starid = input("Please enter your StarID:")
staridpass = input("Please enter your StarID Password:", hidden = True)
firstname = input("Please enter your first name:")
lastname = input("Please enter your first name:")

wait("34outlook.PNG")
click("34outlook.PNG")
wait("36welcometooutlook.PNG")
type(Key.ENTER)
type(Key.ENTER)
wait("37name.PNG")
type("37name.PNG", firstname + " " + lastname)
type(Key.TAB)
type(concatenate(firstname,lastname),"@saintpaul.edu")
type(Key.TAB)
type(staridpass)
type(Key.TAB)
type(staridpass)
type(Key.ENTER)

wait("5security.PNG")
type(starid + "@minnstate.edu")
type(Key.TAB)
type(staridpass)
click("8remembermycredentials.PNG")
type(Key.ENTER)

wait("5security.PNG")
click("15securitypromptmorechoices.PNG")
wait("16useadifferentaccount.PNG")
click("16useadifferentaccount.PNG")

wait("19usernamefield.PNG")
type("19usernamefield.PNG", starid)
type(Key.TAB)
type(staridpass)
click("8remembermycredentials.PNG")
type(Key.ENTER)


wait("12sucessfulconfiguration.PNG")
click("13finishbutton.PNG")


    