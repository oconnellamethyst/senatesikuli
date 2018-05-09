def TermSelect():
    wait(Pattern("2terms.png").targetOffset(0,32),200)
    click(Pattern("2terms.png").targetOffset(0,32))

def DepartmentSelect():
    wait(Pattern("3departments.png").targetOffset(0,32),200)
    click(Pattern("3departments.png").targetOffset(0,32))

def CourseSelect():
    wait(Pattern("4courseandselection.png").targetOffset(0,32),200)
    click(Pattern("4courseandselection.png").targetOffset(0,32))

def FindCount():
    #FIND FASTER WAY OMG SO SLOWWW
    for time in range(0, 4):
        type(Key.DOWN)
    counter = 4
    while exists("1getcoursematerials-1.png") == None:
        type(Key.DOWN)
        counter += 1
    for number in range(0, counter):
        type(Key.UP)
    count = counter - 2
    return count

def Navigator(WebAddress):
    """Stick in the WebAddress, will navigate to a new page"""
    type('n', KeyModifier.CTRL + KeyModifier.SHIFT)
    wait("19brobar.png")
    type(WebAddress + Key.ENTER)
    sleep(1)

def Selector(int):
    """Stick in the number of terms down the list that the program should navigate to"""
    for number in range(0, int - 1):
        type(Key.DOWN)

def AddSelect():
    wait("6selectyourcourses.png")
    click("6selectyourcourses.png")
    while exists("7addselection.png") == None:
        type(Key.RIGHT)
    click("7addselection.png")

def Highlighter(count, Counter, calibrate):
    """Stick in the count of the number of items in a list and the number of items left in a counter of 25, and an offset of the stopping point (add one for select!)"""
    adjustment = 0
    if (count <= Counter and calibrate == 0):
        type('a', KeyModifier.CTRL)
        AddSelect()
        remainder = Counter - count
    elif (count - calibrate <= Counter):
        Selector(calibrate + 1)
        keyDown(Key.SHIFT)
        Selector(count - calibrate)
        keyUp(Key.SHIFT)
        AddSelect()
        remainder = Counter - (count - calibrate)
    else:
        Selector(calibrate + 1)
        keyDown(Key.SHIFT)
        Selector(Counter)
        keyUp(Key.SHIFT)
        AddSelect()
        remainder = 0
        #this becomes the new calibration
        adjustment = calibrate + Counter
    return(remainder,adjustment)

def Saver(number,PDF):
    while exists("1getcoursematerials-1.png") == None:
        type(Key.DOWN)
    click("1getcoursematerials-1.png")
    for number in range(1,10):
        type(Key.LEFT)
        type(Key.UP)
    wait("7capcha.png")
    click("7capcha.png")
    wait("11gradient.png",900)
    while exists("17bookist-1.png") == None:
        type(Key.RIGHT)
    click("17bookist-1.png")
    wait("14printcoursematerialslist.png")
    click("14printcoursematerialslist.png")
    wait("15saveaspdf.png")
    click("16save.png")
    type(Key.LEFT)
    for keypress in range (1,17):
        type(Key.RIGHT)
    type("-" + number + "-" + PDF)
    type(Key.ENTER)
    type('W', KeyModifier.CTRL)

# Main
Limit = (20,)
DepartSel = 1
Counter = Limit[0]
calibrate = 0
PDF = 1

WebAddress = input("Please paste in the Bookstore's Website and make sure your Chrome browser window is small so that the bottom of the tables have only a few pixels between the scroll bar")
Navigator(WebAddress)
TermSelect()
Terms = FindCount()
for number in range(1,Terms):
    TermSelect()
    Selector(number)
    DepartmentSelect()
    Departments = FindCount()
    CourseSelect()
    Courses = FindCount()
    
    while DepartSel != Departments:
        CourseSelect()
        values = Highlighter(Courses, Counter, calibrate)
        Counter = values[0]
        calibrate = values[1]

        if(Counter == 0):
            Saver(number,PDF)
            PDF += 1
            Counter = Limit[0]
            Navigator(WebAddress)
            TermSelect()
            Selector(number)
            DepartmentSelect()
            Selector(DepartSel)
            CourseSelect()
        else:
            pass
        
        if calibrate == 0:
            DepartmentSelect()
            DepartSel += 1
            Selector(DepartSel)
            CourseSelect()
        else:
            pass
    type('a', KeyModifier.CTRL)
    AddSelect()

    Saver(number,PDF)
    PDF = 1
    Counter = Limit[0]
    Navigator(WebAddress)
    
     