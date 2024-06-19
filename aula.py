#Algoritimo > sequencia de passos para executar uma tarefa!

#3 estrutura possiveis no algoritmo

#1 > condicional(decisao - vou executar um script se acontecer X e outro se Y)
#2 > estrutural(sequencia de passos continuos)
#3 > repetição(permite exxcutar varias vezes o mesmo codigo)

#Variaveis
#1 espaços no armazenamento que pode armazenar dados para a execução de um processo!

#Int, float, string e boolean
#Int(5) : armazena valores inteiros(10,14,99)
#Float(1.66) : armazena numeros decimais(1,2 1,7 3,6)
#String: armazena cadeia de caracteres(nome de uma rua, nome completo, sao valores literais, sem calculos)
#Regras > para ser caracterizados como string deve estar entre "", '', "casa kel"
#Boolean(true or false): é o poligrafo, ele aceita dois valores(true e false)

#o pyton tem a tipagem dinamica, ou seja, ele entende a partir do valor do tipo da variavel!


#VARIAVEIS
#curso = "Manufatura Dgitial"
#a variavel "curso" recebe o valor "Manufatura Digital"

#print(type(curso))

#exibir > comando print
# print("Olá eu sou um print, estou executando seu .py")

#para cinversas com o usuario eu uso o input
# altura = float(input("Digite a sua altura"))
#a variavel altura recebe um valor quebrado de altura
# print(f"sua altura é {altura}")
#exibe para mim a "FORMATAÇÃO" do texto com o valor de uma variavel :)

# print("Cadastro de pessoa")
# nome = input("digite seu nome")
# # idade = input("digite sua idade")
# endereco = input("digite um endereco")
# cpf = input("digite seu cpf")
# distancia = input("digite a distancia percorrida no dia")
# anoDenascimento = int(input("digite o ano do seu nascimento"))
# idade = 2024 - anoDenascimento
# print((nome, idade, endereco, cpf, distancia, anoDenascimento))

#estrutuda de algoritmo CONDICIONAL
#EXECUTO alguma intrução de acordo com os dados que tenho. Por exemplo, so posso me alistar no exercito se for maior de idade
#se for maior de iidade
#Para usar o IF  e Else, eu tenho que saber quais opções eu tenho!

# if(idade >= 18):
    #se a idade for maior ou igual a 18 ENTAO(:) exiba a mensagem
#     print("você ja pode se alistar!")
# else:
#se a idade nao for maior ou igual a 18 ENTÃO(:) exiba a mensagem
    # print("você é menor de idade")

# nota = float(input("digite uma nota"))
#
# if(nota > 5):
#     print("você esta aprovado")
#
# elif(nota == 5):
#     print("Você passara no conselho")
#
# else:
#     print("você esta reprovado")

salario = float(input("Digite seu salario"))

if(salario <= 1500):
    print(f"seu salario é {salario + 500}")

elif(salario <= 2000):
    print(f"seu salario é {salario + 400}")

elif(salario <= 3000):
    print(f"seu salario é {salario + 300}")

else:
    print("você é pobre :(")