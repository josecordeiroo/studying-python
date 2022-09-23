import re #RegEx

texto="quando surge, o alviverde imponente no gramado, em que a luta o aguarda"

res=re.findall("a", texto) #esse retorna todos os encontrados

res=re.search("letra", texto) #esse somente indica se encontrou ou nao

res=re.split("\s", texto) # cria um array com cada palavra entre os espaços

res=re.sub("a","b", texto) # percorre toda a string trocando A por B

