import re
print("Las soluciones propuestas pueden ser optimizadas, considere que existen muchas formas de validar una expresión regular")
print("***********************************************************************************************")
print("Palabras que empiecen con abc")
lista1 =['abc','abcd','abcdef','sde']
for i in lista1:
    stock = re.fullmatch(r'^abc[a-z]*$', i)
    print("Cadena {} -> {}".format(i,stock))
print("***********************************************************************************************")
print("Hashtag en donde se mencione a la universidad")
lista1 =['#ESPOL',"gola",'#Espol','#espol64','#BienvnidoESPOL', '#PREEspol','#ADNESPOL','#AdnEspol','#ESPOL_ADN','#espol','#ActitudESPOL','#Regreso_A_Clases_ESPOL', '#ESP']
for i in lista1:
    stock = re.fullmatch(r'^#\w*(espol|ESPOL|Espol)\w*$',i)
    print("Cadena {} -> {}".format(i,stock))
print("***********************************************************************************************")
lista1=['BarcelonaCampeon','ab','#QuieroTenerMiAP','1800Ecuador','aaabbcc','^hoy es un buen día$','aaabbccdd','123','Aiiiiuuuda','Adelante','Esto es LP','09989uhA']
for i in lista1:
    stock = re.fullmatch(r'^([a-zA-Z0-9]{8,10})$',i)
    print("Cadena {} -> {}".format(i,stock))
print("***********************************************************************************************")
print("Validar que las dos primeras letras sean mayuscula")
lista1 =['ABrito', 'CVanegas','TSamaniego','MAngulo','abrito','Abrito']
for i in lista1:
    stock = re.fullmatch(r'^[A-Z]{2}[a-z]+$',i)
    print("Cadena {} -> {}".format(i,stock))
print("***********************************************************************************************")
print("Validar que el número binario sea par o 0")
lista1=['010','10','110','111','0','1']
for i in lista1:
    stock= re.fullmatch(r'^(0|1)*0$',i)
    print("Cadena {} -> {}".format(i,stock))
print("***********************************************************************************************")
print("Formato de horas en hh:mm:ss, 24 horas")
lista1 = ['01:20:34','19:20:23','25:00:00','23:59:59','00:00:00','23:60:60','26:00:00']
for i in lista1:
    stock = re.fullmatch(r'^([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$',i)
    print("Cadena {} -> {}".format(i,stock))
print("***********************************************************************************************")
print("Validar que la fecha ingresada del mes de agosto del 2021 no sea el feriado del 10/agosto, formato de fecha dd-mm-aa y dd/mm/aa")
lista1 = ['01/08/21','01-08-21','19/08/21','10-08-21','10/08/21']
for i in lista1:
    stock = re.fullmatch(r'^(([01][1-9]|2[0-9]|3[0-1])\/08\/21)|(([01][1-9]|2[0-9]|3[0-1])-08-21)$',i)
    print("Cadena {} -> {}".format(i,stock))
print("***********************************************************************************************")
lista1=['rgb(255,255,255)','RGB(120,0,0)','rgb(256,256,256)','rgb(200,256,245)','RGB(239,000,000)']
print("Formato de colores en rgb suponiendo que el ingreso de los colores sean de 3 digitos. Ej.: Válido RGB(000,000,000), NO Válido RGB(0,0,0)")
for i in lista1:
    stock = re.fullmatch(r'^(rgb|RGB)\(([0-1][0-9]{2}|2[0-4][0-9]|25[0-5]),([0-1][0-9]{2}|2[0-4][0-9]|25[0-5]),([0-1][0-9]{2}|2[0-4][0-9]|25[0-5])\)$',i)
    print("Cadena {} -> {}".format(i,stock))
print("***********************************************************************************************")
lista1=['#FFF234','#233fff','#wwwww2']
print("Formato de colores en hexadecimal")
for i in lista1:
    stock = re.fullmatch(r'^#(([0-9a-fA-F]{2}){3}|([0-9a-fA-F]){3})$',i)
    print("Cadena {} -> {}".format(i,stock))