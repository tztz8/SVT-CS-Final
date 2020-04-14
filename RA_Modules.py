def RAM(RA):
    QRA = input("Do you want to do it aging? (Y/N)\n")
    QRAUpper = QRA.upper()
    if QRAUpper == "N":
            RA = False
    if QRAUpper == "NO":
            RA = False
    if QRAUpper == "Y":
            RA = True
    if QRAUpper == "YES":
            RA = True
    return RA
