def Temp_C(value):
	PrintT =[]
	# C to F
	PrintT.append("Fahrenheit: "+ (str((float(value) * float("1.8"))+float("32"))))
	# C to K
	PrintT.append("\nKelvin: "+ (str(float(value)+ float("273.15"))))
	# C to C
	PrintT.append("\nCelsius: "+ (str(float(value))))
	return PrintT

def Temp_F(value):
	PrintT =[]
	# F to F
	PrintT.append("Fahrenheit: "+ (str(float(value))))
	# F to K
	PrintT.append("\nKelvin: "+ (str((float(value)- float("32"))* float(".555") + float("273.15"))))
	# F to C
	PrintT.append("\nCelsius: "+ (str((float(value)- float("32"))* float(".555"))))
	return PrintT

def Temp_K(value):
	PrintT =[]
	# K to F
	PrintT.append("Fahrenheit: "+ (str((float(value) - float("273.15"))* float("1.8") + float("32"))))
	# K to K
	PrintT.append("\nKelvin: "+ (str(float(value))))
	# K to C
	PrintT.append("\nCelsius: "+ (str(float(value)- float("273.15"))))
	return PrintT
def Wind_F(Temp, Wind):
	PrintM =[]
	Temp = float(Temp)
	Wind = float(Wind)
	C = (str(float(35.74 + (0.6215 * Temp) - (35.75 * Wind ** .16) + (.4275 * Temp * Wind ** .16))))
	#PrintM.append("Wind Chill(Fahrenheit)"+ (str(float("35.74")+ (float(".6215")* float(Temp))- (float("35.75")* ))))
	PrintM.append("Wind Chill (Fahrenheit)"+ C)
	return PrintM
def Wind_F_NP(Temp, Wind):
	#PrintM =[]
	Temp = float(Temp)
	Wind = float(Wind)
	C = (float(35.74 + (0.6215 * Temp) - (35.75 * Wind ** .16) + (.4275 * Temp * Wind ** .16)))
	#PrintM.append("Wind Chill(Fahrenheit)"+ (str(float("35.74")+ (float(".6215")* float(Temp))- (float("35.75")* ))))
	#rintM.append("Wind Chill (Fahrenheit)"+ C)
	return C
def Wind_K(value, Wind):
	PrintT =[]
	# K to F
	Temp = ((float(value) - float("273.15"))* float("1.8") + float("32"))
	Wind = float(Wind)
	C = (str(float(35.74 + (0.6215 * Temp) - (35.75 * Wind ** .16) + (.4275 * Temp * Wind ** .16))))
	#PrintM.append("Wind Chill(Fahrenheit)"+ (str(float("35.74")+ (float(".6215")* float(Temp))- (float("35.75")* ))))
	PrintT.append("Wind Chill (Fahrenheit)"+ C)
	return PrintT
def Wind_C(value, Wind):
	PrintT =[]
	# C to F
	Temp = ((float(value) * float("1.8"))+float("32"))
	Wind = float(Wind)
	C = (str(float(35.74 + (0.6215 * Temp) - (35.75 * Wind ** .16) + (.4275 * Temp * Wind ** .16))))
	#PrintM.append("Wind Chill(Fahrenheit)"+ (str(float("35.74")+ (float(".6215")* float(Temp))- (float("35.75")* ))))
	PrintT.append("Wind Chill (Fahrenheit)"+ C)
	return PrintT
