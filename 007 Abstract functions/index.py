def cores(*t):
    print(t[0])
    print(t[1])
    print(t[2])


cores("azul", "branco", "vermelho")

# função abstrata, não preciso especificar nada antes, mando do jeito que eu quiser

def cores(*t):

    for i in t:
        print(i)


cores("azul", "branco", "vermelho")
