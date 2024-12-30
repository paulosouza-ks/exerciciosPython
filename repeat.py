# Receber uma string e um número do usuário, depois repetir a string de acordo com o número informado.

txt = input("Informe um texto: ")
qtd = int(input("Quantas vezes quer repeti-lo? "))

print("Texto repetido: ", ((txt + " ") * qtd))
