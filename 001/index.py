name = "José"
print(type(name))
age = 90

# todos recebem o mesmo resultado "0"
a = b = c = 0  

#boolean
testBoolean = True  # primeira letra maiuscula

# if else
if name == "Diego":
    print("1")
else:
    print("2")

# function
def testFunction(name):
    global secondName  # variavel global primeiro declara, na outra linha atribui
    secondName = name


testFunction("Cordeiro")
print(f'Meu nome é {name} {secondName} e eu tenho {age} anos')


# transformando números
floatNumber = 22.34354544
intNumber = int(floatNumber)
print(intNumber)
floatNumber = float(intNumber)
print(floatNumber)

#lenght
print(len(name))

#split separada cada palavra e coloca em um array
title="curso de python no youtube totalmente grátis"
newTitle= title.split(" ")
print(newTitle)

#in achei util pra fazer pesquisa
if ("Python".upper() in title.upper()): #usando o upper para deixar todo mundo maiusculo e permitir a busca independente de como foi escrito
    print(title)

if ("javascript" not in title):
    print("Este curso não é de javascript")