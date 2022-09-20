#Server.py
import Pyro4
import random
import datetime
import math
import timeit

#Importação para detecção do IP
import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

now = datetime.datetime.now()
print('[SERVER]Data: '+now.strftime('%d-%m-%y')+' Hora: '+now.strftime('%H:%M:%S'))
@Pyro4.expose
class Server(object):
    def get_usid(self, nome):
        return "[SERVER]Hello, {0}.\n" \
            "Your Current User Session is {1}:".format(nome, random.randint(0, 1000))

    def adicao(self, numero_1, numero_2):
        inicio = timeit.default_timer()
        resultado = numero_1 + numero_2
        fim = timeit.default_timer()
        print('[SERVER]:Requisição de adição feita por %s, duração: %fs' % (ip_address, fim - inicio))
        return "[SERVER]:{0} + {1} = {2}".format(numero_1, numero_2, resultado)

    def subtracao(self, numero_1, numero_2):
        inicio = timeit.default_timer()
        resultado = numero_1 - numero_2
        fim = timeit.default_timer()
        print('[SERVER]:Requisição de subtração feita por %s, duração: %fs' % (ip_address, fim - inicio))
        return "[SERVER]:{0} - {1} = {2}".format(numero_1, numero_2, resultado)

    def multiplicacao(self, numero_1, numero_2):
        inicio = timeit.default_timer()
        resultado = numero_1 * numero_2
        fim = timeit.default_timer()
        print('[SERVER]:Requisição de multiplicação feita por %s, duração: %fs' % (ip_address, fim - inicio))
        return "[SERVER]:{0} * {1} = {2}".format(numero_1, numero_2, resultado)

    def divisao(self, numero_1, numero_2):
        inicio = timeit.default_timer()
        resultado = numero_1 / numero_2
        fim = timeit.default_timer()
        print('[SERVER]:Requisição de divisão feita por %s, duração: %fs' % (ip_address, fim - inicio))
        return "[SERVER]:{0} / {1} = {2}".format(numero_1, numero_2, resultado)

    def raiz_quadrada(self, numero_1, numero_2):
        inicio = timeit.default_timer()
        resultado1 = math.sqrt(numero_1)
        resultado2 = math.sqrt(numero_2)
        fim = timeit.default_timer()
        print('[SERVER]:Requisição de raiz quadrada feita por %s, duração: %fs' % (ip_address, fim - inicio))
        return "[SERVER]:Raiz de {0}:{1} Raiz de {2}:{3}".format(numero_1, resultado1, numero_2, resultado2)


daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
url = daemon.register(Server)
#Registro do Servidor, deve ter o mesmo nome declarado no client para funcionar
ns.register("RMI.calculadora", url)
print("[SERVER]:O servidor está ligado, pode iniciar o seus Clients")
daemon.requestLoop()

