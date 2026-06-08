# Vamos usar uma variável chamada nome para
# guardar o nome do cliente. Utilizaremos também
# o comando input(in -> dentro | put -> por em algum lugar)
nome = input("Digite o seu nome: ")
print("Olá, Sr(a)."+nome)
print(f"Olá, Sr(a). {nome}")
# O oprador + foi utilizado para
# contatenar(juntar) o texto entre aspas("")
# com a variável nome
print("Olá. Sr(a)."+nome+". Seja bem vindo")
# Abaixo, usamos o comando print com a letra
# f(foramt) para inserir uma variável no meio
# de uma string. A variável foi inserida com chaves({})
# esta técnica é chamada de interpolação
print(f"Olá Sr(a). {nome}. Seja bem vindo")