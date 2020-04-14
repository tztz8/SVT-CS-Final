from Temp_Converter_Module import *
def Wind_Table():
	PrintT = []
	#PrintT.append("-------------------------------------------------------------------------------")
	PrintT.append("|---------------------------------Temperature---------------------------------------------|\n")
	PrintT.append("|Wind_-15__-10___-5_____0____5____10___15__20__25___30___35__40|\n")
	PrintT.append("|----+------------------------------------------------------------------------------------|\n")
	for V in range(5,60,5):
		#print(V)
		V2 = (float (V)+ float("5"))
		PrintT.append("%8d|"% V2)
		for T in range(-20,40,5):
			#print(T)
			wc = Wind_F_NP(T,V)
			#print(wc)
			PrintT.append("%-4.2f|"% wc)
		PrintT.append("\n")
		PrintT.append("-  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --\n")
	return PrintT