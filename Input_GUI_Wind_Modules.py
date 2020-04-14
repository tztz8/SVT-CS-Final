import easygui
def Input_Wind():
    #RAMI = True
    #while RAMI:
    try:
        value = float(easygui.enterbox(msg='Enter Wind', title='Wind', default='', strip=True))
            #print (value)
            #RANI = False
    except:
        easygui.msgbox('This is not a number', ok_button="OK",)
        value = None
            #RANI = True
    return value
#Value = Input_Temp()
#print(Value)
