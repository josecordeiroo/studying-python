smartphone = {
    "Fabricante": "Samsung",
    "Modelo": "S20 Plus",
    "Ano": "2020",
    "Cor": "Azul",
    "Armazenamento": {
        "ssd": "256gb",
        "memory": "16gb"
    }
}

# usar valor especifico
print(smartphone["Armazenamento"]["memory"])

# adicionar um novo
smartphone["Sistema"] = "Android"

print(smartphone)

# remover uma chave
smartphone.pop("Cor")

print(smartphone)
