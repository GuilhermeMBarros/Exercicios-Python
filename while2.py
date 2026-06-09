palavra = "Tempo"
# O comando len(length = Comprimento), ou seja,
# conta a quantidade de caracteres de uma coleção
qtd_palavra = len(palavra)
print(qtd_palavra)
cont = 0   # cont é igual a 0
while cont <= qtd_palavra:
        # enquanto cont(0) for menor (<) que qtd_palavra,
        # o comando executa
        print(f"A {cont+1}ª letra é {palavra[cont]}")
        # Faz o cont sair de 0, porque ele executou uma vez.
        # Agora cont vale 1, e assim por diante para mostrar as seguintes letras da palavra
        cont+=1 