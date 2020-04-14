from easygui import*
def menu(item):
    msg ="Chose your tepter"
    title = "Temp Converter"
    opte = choicebox(msg, title, item)
    inn = (len(item)+1)
    return (opte, inn)
