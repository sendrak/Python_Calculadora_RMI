#Client.py
import Pyro4
import datetime
Client = Pyro4.Proxy("PYRONAME:RMI.calculadora")
now = datetime.datetime.now()
print('Informações da Conexão: \nData: '+now.strftime('%d-%m-%y')+'\nHora: '+now.strftime('%H:%M:%S'))
nome = input("Informe seu nome: ").strip()
print(Client.get_usid(nome))
n = int(input("Quantas operações você quer fazer, {0} ?".format(nome)))
while n > 0:
    n = n-1
    numero_1 = int(input("\nInforme o primeiro número: "))
    numero_2 = int(input("Informe o segundo número: "))
    print("Escolha a operação desejada: \n" + "1.Adição \n" + "2.Subtração \n" + "3.Multiplicação \n" + "4.Divisão\n" + "5.Raiz Quadrada\n")
    operacao = int(input("Qual a sua escolha: "))
    if operacao == 1:
        print(Client.adicao(numero_1, numero_2))
    elif operacao == 2:
        print(Client.subtracao(numero_1, numero_2))
    elif operacao == 3:
        print(Client.multiplicacao(numero_1, numero_2))
    elif operacao == 4:
        print(Client.divisao(numero_1, numero_2))
    elif operacao == 5:
        print(Client.raiz_quadrada(numero_1, numero_2))
    else:
        print("Opção inválida")

    if n <= 0:
        print("\n*----------------------------------------*")
        print("Número de requisições solicitadas encerrada.")
        print("Conexão finalizada.")
