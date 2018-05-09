def addsenateinbox():
    '''
    Program to add the senate shared inbox
    '''
    wait("34outlook.PNG")
    click("34outlook.PNG")
    wait("23file-1.PNG")
    click("23file.PNG")
    wait("24accountsettings.PNG")
    click("24accountsettings.PNG")
    wait("25accountsettings.PNG")
    click("25accountsettings.PNG")
    wait("26sendfromthisaccount.PNG")
    doubleClick("26sendfromthisaccount.PNG")
    wait("28moresettings.PNG")
    click("28moresettings.PNG")
    wait("29advanced.PNG")
    click("29advanced.PNG")
    wait("30add.PNG")
    click("30add.PNG")
    wait("32lilbluebox.PNG")
    type("32lilbluebox.PNG", "SPC-Student Senate")
    wait("31okay.PNG")
    click("31okay.PNG")
    wait("33apply.PNG")
    click("33apply.PNG")

#Main
addsenateinbox()


