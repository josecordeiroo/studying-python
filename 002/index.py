names = ["zeca", "Jose", "Joao"]

# qualquer um desses dois metodos copia a lista do mesmo jeito, eu testei
names2 = list(names)
names3 = names

print(names)

names.append("Julio")  # tipo o push

print(names)

print(f'Temos {len(names)} nomes na lista')

names.remove(names[0])
names.remove("Jose")
names.pop  # Remove o ultimo elemento da lista
del names[0]  # remove também
names.clear()  # limpa todos os elementos
names2 = list(names)


def calculadora(n1, n2, operador):
    if (operador == "+"):
        return n1 + n2
    elif (operador == "-"):
        return n1 - n2
    elif (operador == "/"):
        return n1 / n2
    elif(operador == "*"):
        return n1 * n2


print(int(calculadora(77, 30, "/")))
