#Escreva um programa em Python que solicita ao usuário 
#para digitar seu nome, o valor do seu salário mensal e 
#o valor do bônus que recebeu. 
#O programa deve, então, imprimir uma mensagem saudando o 
#usuário pelo nome e informando o valor do salário 
#em comparação com o bônus recebido.#

nome = input("Digite seu nome: ")
valor_salario = int(input("Digite o seu salario: "))
bonus_porcentagem = 1.5

valor_final = 1000 + (valor_salario * bonus_porcentagem)
print(valor_final)



