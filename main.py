def main():
	
	from operator import xor
	
	def cambiar_decimal(array):
		for index, item in enumerate(array):
			if (item == "a"):
				array[index] = 1
			elif (item == "b"):
				array[index] = 2
			elif (item == "c"):
				array[index] = 3
			elif (item == "d"):
				array[index] = 4
			elif (item == "e"):
				array[index] = 5
			elif (item == "f"):
				array[index] = 6
			elif (item == "g"):
				array[index] = 7
			elif (item == "h"):
				array[index] = 8
			elif (item == "i"):
				array[index] = 9
			elif (item == "j"):
				array[index] = 10
			elif (item == "k"):
				array[index] = 11
			elif (item == "l"):
				array[index] = 12
			elif (item == "m"):
				array[index] = 13
			elif (item == "n"):
				array[index] = 14
			elif (item == "o"):
				array[index] = 15
			elif (item == "p"):
				array[index] = 16
			elif (item == "q"):
				array[index] = 17
			elif (item == "r"):
				array[index] = 18
			elif (item == "s"):
				array[index] = 19
			elif (item == "t"):
				array[index] = 20
			elif (item == "u"):
				array[index] = 21
			elif (item == "v"):
				array[index] = 22
			elif (item == "w"):
				array[index] = 23
			elif (item == "x"):
				array[index] = 24
			elif (item == "y"):
				array[index] = 25
			elif (item == "z"):
				array[index] = 26
			else:
				array[index] = 27
	
	def cambiar_binario(array):
		for index, item in enumerate(array):
			
			integer = int(item)
			
			binary = bin(integer)[2:].zfill(5)
			array[index] = binary
	
	def llenar_clave(array1, array2):
		for index in array2:
			if(len(array1) != len(array2)):
				array2.append(index)
	
	def xor_operacion(array1, array2):
		
		arrayXOR = []
		i = 0
		i2 = 0
		i3 = 0
		
		while i < len(array1):
			
			array1[i] = int(array1[i])
			
			i += 1
		
		while i2 < len(array2):
			
			array2[i2] = int(array2[i2])
			
			i2 += 1
		
		while i3 < len(array1):
			
			resultado = xor(array1[i3],array2[i3])
			resultado = bin(resultado)[2:].zfill(5)
			arrayXOR.append(resultado)
			
			i3 += 1
				
		print "array XOR resultante: ", arrayXOR
		
		for index, item in enumerate(arrayXOR):
			if (item == "00001"):
				arrayXOR[index] = "a"
			elif (item == "00010"):
				arrayXOR[index] = "b"
			elif (item == "00011"):
				arrayXOR[index] = "c"
			elif (item == "00100"):
				arrayXOR[index] = "d"
			elif (item == "00101"):
				arrayXOR[index] = "e"
			elif (item == "00110"):
				arrayXOR[index] = "f"
			elif (item == "00111"):
				arrayXOR[index] = "g"
			elif (item == "01000"):
				arrayXOR[index] = "h"
			elif (item == "01001"):
				arrayXOR[index] = "i"
			elif (item == "01010"):
				arrayXOR[index] = "j"
			elif (item == "01011"):
				arrayXOR[index] = "k"
			elif (item == "01100"):
				arrayXOR[index] = "l"
			elif (item == "01101"):
				arrayXOR[index] = "m"
			elif (item == "01110"):
				arrayXOR[index] = "n"
			elif (item == "01111"):
				arrayXOR[index] = "o"
			elif (item == "10000"):
				arrayXOR[index] = "p"
			elif (item == "10001"):
				arrayXOR[index] = "q"
			elif (item == "10010"):
				arrayXOR[index] = "r"
			elif (item == "10011"):
				arrayXOR[index] = "s"
			elif (item == "10100"):
				arrayXOR[index] = "t"
			elif (item == "10101"):
				arrayXOR[index] = "u"
			elif (item == "10110"):
				arrayXOR[index] = "v"
			elif (item == "10111"):
				arrayXOR[index] = "w"
			elif (item == "11000"):
				arrayXOR[index] = "x"
			elif (item == "11001"):
				arrayXOR[index] = "y"
			elif (item == "11010"):
				arrayXOR[index] = "z"
			else:
				arrayXOR[index] = "_"
		
		print "Texto cifrado", arrayXOR
				
						
	texto_llano = raw_input("Introduzca el texto llano: ")
	
	array_texto = list(texto_llano)
	
	print "Texto llano: ", array_texto 
	print "\n"
	
	clave = raw_input("Introduzca la clave: ")
	
	array_clave = list(clave)
	
	llenar_clave(array_texto, array_clave)
	
	print "clave: ", array_clave
	print "\n"
	
	cambiar_decimal(array_texto)
	
	cambiar_decimal(array_clave)
	
	print "Texto llano en decimal: ", array_texto 
	print "\n"
	
	print "Clave en decimal: ", array_clave 
	print "\n"
	
	xor_operacion(array_texto, array_clave)
	
	
	return 0

if __name__ == '__main__':
    main()
