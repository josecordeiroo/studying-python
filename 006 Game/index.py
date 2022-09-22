import random

n = int(random.randint(0, 100))

print(n)
print("Início do programa.")

r = int(input("Chute um número de 0 a 100: "))

c = 1

while r != n:
    if n < r:
        r = int(input("Errou. O número é menor. Tente novamente: "))
    else:
        r = int(input("Errou. O número é maior. Tente novamente: "))
    c += 1

if (c == 1):
    print("Parabéns, você acertou de primeira!")
else:
    print(f"Parabéns, você acertou em {c} tentativas!")


print("Fim do programa.")
