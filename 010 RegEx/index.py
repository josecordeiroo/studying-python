import re #RegEx

texto="quando surge o alviverde imponente no gramado em que a luta o aguarda"

res=re.findall("a", texto)

print(f"Letra encontrada {len(res)} vezes.")