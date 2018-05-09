try:
    starid = input("Please enter your StarID:")
    staridpass = input("Please enter your StarID Password:", hidden = True)

    wait("5security.PNG",900)
    click("15securitypromptmorechoices.PNG")
    wait("39differentacc.PNG")
    click("39differentacc.PNG")

    wait("19usernamefield.PNG")
    type("19usernamefield.PNG", starid)
    type(Key.TAB)
    type(staridpass)
    click("8remembermycredentials.PNG")
    type(Key.ENTER)

    wait("5security-2.PNG",900)
    click("20passwordfield.PNG")
    type(staridpass)
    click("8remembermycredentials-1.PNG")
    type(Key.ENTER)
    
    # Clears out user data
    starid = ":ashd;gahhjgaJHFDHl"
    staridpass = ":ashd;gahhjgaJHFDHl"
    del starid
    del staridpass
except:
    # Clears out user data even if the program fails
    starid = ":ashd;gahhjgaJHFDHl"
    staridpass = ":ashd;gahhjgaJHFDHl"
    del starid
    del staridpass