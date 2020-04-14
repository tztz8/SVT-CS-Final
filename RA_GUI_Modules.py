import easygui
def RAM(RA):
    if ynbox(msg='Shall We Run Agen?', title=' ', choices=('Yes', 'No'), image=None):
        RA = True
    else:
        RA = False
    return RA
