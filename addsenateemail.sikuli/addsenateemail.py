def concatenate(first,last):
    firstpart = []
    lastpart = []
    for char in first:
        if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            firstpart.append()
        else:
            pass
        firstpart = []
    for char in last:
        if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            lastpart.append()
        else:
            pass
    return(firstpart + "." + lastpart)

# Main Program

starid = input("Please enter your StarID:")
staridpass = input("Please enter your StarID Password:")
firstname = input("Please enter your first name:")
lastname = input("Please enter your first name:")

wait("34outlook.PNG")
click("34outlook.PNG")
wait("1welcomescreen.PNG")
type(key.ENTER)
wait("2accountsetup.PNG")
type(firstname + " " + lastname)
type(key.TAB)
type(concatenate(firstname,lastname) + "@saintpaul.edu")
type(key.TAB)
type(staridpass)
type(key.TAB)
type(staridpass)
type(key.ENTER)

wait("5security.PNG")
type(starid + "@minnstate.edu")
type(key.TAB)
type(staridpass)
click("8remembermycredentials.PNG")
type(key.ENTER)

wait("5security.PNG")
click("15securitypromptmorechoices.PNG")
wait("16useadifferentaccount.PNG")
click("16useadifferentaccount.PNG")

wait("19usernamefield.PNG")
type("19usernamefield.PNG", starid)
type(key.TAB)
type(staridpass)
click("8remembermycredentials.PNG")
type(key.ENTER)


wait("12sucessfulconfiguration.PNG")
click("13finishbutton.PNG")


    