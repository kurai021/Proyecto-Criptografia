#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  transposicion.py
#  
#  Copyright 2015 Richard Armuelles <richard@richard-host>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



def main():
	
	texto_llano = raw_input("introduzca un mensaje para cifrar: ")
	
	clave = raw_input("introduzca la clave: ")
	
	texto_cifrado = encriptarMensaje(clave, texto_llano)
	
	print(texto_cifrado)
	
def encriptarMensaje(clave, mensaje):
		
		texto_cifrado = [''] * len(clave)
		
		for col in range(len(clave)):
			pointer = col
			
			while pointer < len(mensaje):
				texto_cifrado[col] += mensaje[pointer]
				
				pointer += len(clave)
				
		return ''.join(texto_cifrado)	

if __name__ == '__main__':
	main()

