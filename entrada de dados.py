#Exercício para pegar dados do usuário, executar uma ação e imprimir

nome = input("Digite seu nome ")
idade = input ("digite sua idade ")     # A função input sempre retorna uma string
ano_nascimento = 2020 - int(idade)

print(f'{nome} tem {idade} anos \n'
      f'{nome} nasceu em {ano_nascimento}.')
