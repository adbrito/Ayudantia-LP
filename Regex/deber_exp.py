import re
lista = [
    '24@espol.edu.ec',
    '23443jj@espol.edu.ec',
    '23adbrito@fiec.espol.edu.ec',
    '@espol.edu.ec',
    '23adbrito@fiec..espol.edu.ec',
    'a@edu.ec',
    'adbrito19@espol.edu.ec.',
    'adbrito@espol.edu.ec.'
    'user1@espol.edu.ec',
    'adbrito@espol.edu.ec@espol.edu.ec',
    'ADBRITO@espol.edu.ec',
    'Adbrito@espol.edu.ec@edu.ec',
    'amazon@fiec.edu.ec',
    'adbrito@espol.edu.ec',
    'adbrito@espol..edu.ec',
    'adbrito@@espol.edu.ec',
    'abdi._2@espol.edu.ec',
    'correo.1@fiec.espol.edu.ec',
    'mi_correo@dw.fadcom.espol.edu.ec',
    'adbrito19@espol.edu.ec'
]
for i in lista:
    stock = re.fullmatch(r'^[a-z]+[\w]+\.?-?[\w]+?@([a-z]+\.)*(espol.edu.ec)$', i)
    print("Cadena {} -> {}".format(i, stock))
print("***********************************************************************************************")
lista = [
    '<img src="meme.png">',
    '<img src="w3schools.jpg" alt="informacion" width="104" height="142">',
    '<img width="30" height="50" src="w3schools.jpeg">',
    '<img src="w3schools.jpeg" alt="imagen">',
    '<img src="w3schools.jpeg">',
    '<img src="w3schools.jpg">',
    '<img alt="imagen">',
    '<img width="30">'
]
for i in lista:
    stock = re.fullmatch(
        r'^<img((\s([\w]+="[\w]+")?)*?|\s)(src="[\w]+(\.png|\.jpg|\.jpeg)")?(((\s[\w]+="[\w]+"))*?>|>)$', i)
    print("Cadena {} -> {}".format(i, stock))
print("***********************************************************************************************")

lista = [
    'variable',
    '$variable',
    '@variable',
    '@@variable',
    '@@var2_',
    '@var',
    '@vidas',
    '@@v',
    'suma',
    '@@@variable2',
    '@$val',
    'var@'
]
for i in lista:
    stock = re.fullmatch(r'^(@{1,2}|\$)?[\w]+$', i)
    print("Cadena {} -> {}".format(i, stock))
print("***********************************************************************************************")

lista = [
    'hola',
    'abc',
    '123',
    'prueba',
    '2021hola',
    '2021hola2021',
    'hola20212021',
    'abcdefghijklmn',
    '202120212021',
    'qwert45rt565ee',
    '0991279378',
    'ola20210203',
    'Hi39iu87yyt5'
    'listo12320212',
    'AB1994brito'
]

for i in lista:
    stock = re.fullmatch(
        r'^((?!.*hola|.*abc|.*prueba|.*123)[a-z\dA-Z]){10,}$', i)
    print("Cadena {} -> {}".format(i, stock))
print("***********************************************************************************************")
