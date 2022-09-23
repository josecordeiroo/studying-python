import re #RegEx

texto="quando surge o alviverde imponente no gramado em que a luta o aguarda"

res=re.findall("a", texto) #esse retorna todos os encontrados

print(f"Letra encontrada {len(res)} vezes.")

res=re.search("letra", texto) #esse somente indica se encontrou ou nao