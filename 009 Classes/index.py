soma= lambda n1, n2: n1 + n2
print(soma(20, 30))


ratata=lambda x, func: x + func(x) # A lambda sempre retorna o resultado

def soma(number):
    return number + 10

print(ratata(10, soma))