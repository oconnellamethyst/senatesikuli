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
lastname = input("Please enter your last name:")
concate = concatenate(firstname,lastname)

wait("34outlook.PNG")
click("34outlook.PNG")
wait("36welcometooutlook.PNG")
type(Key.ENTER)
type(Key.ENTER)
wait("37name.PNG")
type("37name.PNG", firstname + " " + lastname)
type(Key.TAB)
type(concate + "@saintpaul.edu")
type(Key.TAB)
type(staridpass)
type(Key.TAB)
type(staridpass)
type(Key.ENTER)

wait("5security.PNG",900)
click("5security.PNG")
type("a",KeyModifier.CTRL)
type(starid + "@minnstate.edu")
type(Key.TAB)
type(staridpass)
click("8remembermycredentials.PNG")
type(Key.ENTER)

wait("12sucessfulconfiguration.PNG",900)
click("13finishbutton-1.PNG")

wait("5security-1.PNG",900)
click("15securitypromptmorechoices-1.PNG")
wait("39differentacc.PNG")
click("39differentacc.PNG")

wait("19usernamefield-1.PNG")
type("19usernamefield-1.PNG", starid)
type(Key.TAB)
type(staridpass)
click("8remembermycredentials-1.PNG")
type(Key.ENTER)
wait("5security-2.PNG",900)
click("5security-2.PNG")
type(staridpass)
click("8remembermycredentials-2.PNG")
type(Key.ENTER)


    