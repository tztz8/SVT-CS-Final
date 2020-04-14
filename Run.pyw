#imports
from Temp_Converter_Module import *
from Menu_GUI_Modules import *
from Input_GUI_Temp_Modules import *
from Input_GUI_Wind_Modules import *
from Print_GUI_Modules import *
from Wind_Table import *
import easygui
#from RA_GUI_Module import *

items = ["Fahrenheit","Kelvin","Celsius","Wind Temp Table","Wind Chill"]
MES = "Your Tempters"

RA = True
while RA:
	(opten, inn) = menu(items)
	if opten == None:
		RA = False
	elif opten == "Fahrenheit": #Temp converter
		RAM = True
		while RAM:
			FAH=Input_Temp()
			if FAH != None:
				PrintT=Temp_F(FAH)
				Print(PrintT, MES)
				RAM = False
	elif opten == "Kelvin": #Temp converter
		RAM = True
		while RAM:
			Kel=Input_Temp()
			if Kel != None:
				PrintT=Temp_K(Kel) 
				Print(PrintT, MES)
				RAM = False
		#Kel=Input_Temp()
		#PrintT=Temp_K(Kel)
		#Print(PrintT, MES)
	elif opten == "Celsius": #Temp converter
		RAM = True
		while RAM:
			Cel=Input_Temp()
			if Cel != None:
				PrintT=Temp_C(Cel)
				Print(PrintT, MES)
				RAM = False
		#Cel=Input_Temp()
		#PrintT=Temp_C(Cel)
		#Print(PrintT, MES)
	#elif opten == "__________________________":
		#easygui.msgbox('Sorry this is not a opeten', ok_button="OK",)
	elif opten == "Wind Temp Table":
		#easygui.msgbox('Sorry this is not finish thery by be errors', ok_button="OK",)
		PrintT= Wind_Table()
		Print(PrintT, "Wind Table")
	elif opten == "Wind Chill":
		msg = "What temp mesherment?"
		choices = ["Fahrenheit","Kelvin","Celsius"]
		reply2 = buttonbox(msg=msg,title = "Wind Temp Table",choices=choices)
		if reply2 == "Fahrenheit":
			RAM = True
			while RAM:
				WTTT = Input_Temp() #input temp and wind
				WTTW = Input_Wind()
				if WTTT != None:
					if WTTW != None:
						PrintM = Wind_F(WTTT, WTTW)
						Print(PrintM, "Wind Table")
						RAM = False
		elif reply2 == "Kelvin":
			RAM = True
			while RAM:
				WTTT = Input_Temp() #input temp and wind
				WTTW = Input_Wind()
				if WTTT != None:
					if WTTW != None:
						PrintM = Wind_K(WTTT, WTTW)
						Print(PrintM, "Wind Table")
						RAM = False
		elif reply2 == "Celsius":
			RAM = True
			while RAM:
				WTTT = Input_Temp() #input temp and wind
				WTTW = Input_Wind()
				if WTTT != None:
					if WTTW != None:
						PrintM = Wind_C(WTTT, WTTW)
						Print(PrintM, "Wind Table")
						RAM = False
'''
	elif opten == "Wind Temp Table2":
		easygui.msgbox('Sorry this is not finish thery by be errors and this is made wrong', ok_button="OK",)
		image = "windchill2.gif"
		MEJ = "Hire is you'r table\nDo you whant to put in Your oney Temp and Wind Speed?"
		choices = ["Yes","No-Cancel"]
		reply = buttonbox(MEJ,title = "Wind Temp Table",image=image,choices=choices)
		if reply == "Yes":
			image = "windchill2.gif"
			msg = "What temp mesherment?"
			choices = ["Fahrenheit","Kelvin","Celsius"]
			reply2 = buttonbox(msg=msg,title = "Wind Temp Table",image=image,choices=choices)
			if reply2 == "Fahrenheit":
				WTTT = Input_Temp()
				WTTW = Input_Wind()
				PrintM = Wind_F(WTTT, WTTW)
				Print(PrintM, "Wind Table")
'''