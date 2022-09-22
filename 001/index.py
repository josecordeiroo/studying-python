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

