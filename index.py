import string

# function "Palindrom"

def palindromo(palavra):

    excluindo_pontos = set(string.punctuation) #excluindo pontos da palavra
    frase = " ".join(i for i in palavra if i not in excluindo_pontos) # formando a palavra a partir do método join() sem os pontos.
    frase = frase.replace(" ", "").lower()  # removendo os espaços vazios e trnsformando as letras em minúsculas

    if palavra == palavra[::-1]:
        return "this sentence " + frase + " its palindrom!"
    else:
        return "This sentence " + frase + " it`s not palindron!"

def main():

    frase = (input("Type the phrase: "))
    print(palindromo(frase))

if __name__ == "__main__":
    main()


# DATA STRUCTURES: 

# lista:
teams_never_down = ["flamengo", "Santos", "São paulo"]
# Acessado elementos:
teams_never_down[0]
# adicionado elementos:
teams_never_down.insert(1, "barcelona") # bracelona no indice 1
# adc elemento no fim da lista:
teams_never_down.append("Real madrid")
#removendo elemento:
teams_never_down.remove("barcelona", "Real madrid")
# ordenando uma lista por ordem alfabética:
teams_never_down.sort()
# imprimindo os elementos da lista como uma string:
teams_strings = ",".join(teams_never_down)
# criando uma lista com listas:
list_of_names = [["luis,", "oliveira"], ["pedro", "Joao"]]
list_of_names[1][0] # buscando por Pedro na lista
#convertendo listas em tuplas:
tuple(teams_never_down)

# tupla

#somando duas tuplas:
a = (1,2)
b = a + (3,4,5)
# multiplicando tuplas:
a * 2 # (1,2,1,2)
# index na tupla
b.index(2)
# adc valores a elem de tuplas:
(a,b,d) = (2,4,6.7)
# convertendo uma tupla em uma lista:
list(b)
# adicionado indentidades a elementos em uma tupla:
me = ("luis", "felipe", 19)
fristhname, secondname, age = me

# conjuntos:

ex = {1,2,1,1,4,5,5,4,2} # Não irá amazenar elementos repetidos.
# Usando for com conjuntos:
conj = {i for i in range(0,10)} # nesse caso se não fosse um conjunto o "for" iria iterar infinitamente.
# adc elem ao conjunto:
conj.add(11)
# transfromando uma lista em um conjunto:
lista = [1,2,6,4,1,1,3,2]
lista_conj = set(lista)

# Dicionário:

dic = {"a": 10, "b": 2, "c": 12}
# acessando valores:
dic["b"] # 2
# atualizando (adicionando) o valor de uma chave:
dic["b"] = 11
# iniciando um dicionário vazio e adicionado valores a ele:
dictwo = {}
dictwo["name"] = "luisin"
dictwo["number"] = 86995254202
dictwo["instagram"] = "@luisfl04_"
dictwo[(1,33,22,44,"heloo")]
# Buscando todas as chaves em um dicionário:
dictwo.keys()
# Buscando todos os valores
dictwo.values()
# retornado as chaves e os elementos como pares:
dictwo.items()

# ORIENTAÇÃO A OBJETOS:

# definindo uma classe:
class LibraryBook:

    pass
# Adicionado uma instância a classe:
mybook = LibraryBook    
# Criando uma class com o metodo "__init__" e passando valores usando a instância:
class Books(object):

    def __init__(self, autor, titulo, ano):
        self.autor = autor
        self.titulo = titulo
        self.ano_lanc = ano

stevejobs = Books
stevejobs.autor = "Water Isaacson"
stevejobs.titulo = " Steve Jobs por Water Isaacson"
stevejobs.ano_lanc  = 2012
# passando todas os dados para "__init__" por parâmetro:
stevejobs = Books("Water Isaacson", "Steve Jobs por Water Isaacson", 2012)
# adiconado métodos para a classe:
class Books(object):

    def __init__(self, autor, titulo, ano):
        self.autor = autor
        self.titulo = titulo
        self.ano_lanc = ano
    
    # Método que retorna as infos como string:
    def title_and_autor(self):
        return "{} {}: {}" .format(self.autor[1], self.autor[0], self.titulo)
    # método que retorna todas as infos do livro:
    def __str__(self):
        return "{} {} ({}): {}" .format(self.autor[1], self.autor[0], self.titulo, self.ano_lanc)
    
stevejobs = Books(("Water Isaacson", "Appla computers", 2010))
# declarando classes pai e filho com herança:
class Avo(object): # Classe pai
    pass
class Pai():
    pass
class Filho():
    pass
# chamando um método por herança:
class carros(object):
    def Minhasmotos(self):
        return "Fan 2011"
class carros2(carros):
    pass
class carros3(carros):
    pass
# chamando a função "MinhasMotos" da classe pai:
teste = carros3()
teste.Minhasmotos()
# Substituindo o valor do método da classe pai
class carros3(carros):
    def Minhasmotos(self):
        return"Crosser 2016"
# Acessando o método de construtor tanto na classe pai como na classe filha:
class Father(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is {}".format(self.name)
    
class Son(Father):
    
    def __init__(self, name):
        self.name = name
# Buscando o __init__ da classe filha:
name = Son("Reed")
# Buscando o a classe pai:
nametwo = Father("Steve")
print(name)
print(nametwo)


# BIBLIOTECAS:

# Usando a biblioteca Math:
import math
# Usando método de calcular potência:
print("2 ^ 3 = ",math.pow(2,3))
# Método teto:
print(math.ceil(3.57)) # = 4
# método piso:
print(math.floor(4.87)) # = 4
# método de valor absoluto:
print(math.fabs(-934.66)) # = 934.66
# Método de logaritimo com base "e" e especificando a base:
print(math.log(1000))
print(math.log(100,10)) # Log de 100 na base 10.

# Operações com vetores:

# Multiplicando elem de uma lista:
[1,2,3] * 3 # res = [1,2,3,1,2,3,1,2,3]
# Para multiplicar a lista como um vetor se faz isso:
[i * 3 for i in[1,2,3]] # res = [3,6,9]
# somando dois vetores:
[1,2,3] + [4,5,6]
# Somando o VALOR de dois vetores:
a = [1,2,3]
b = [4,5,6]
[a[i] + b[i] for i in range(len(a))]
# multiplicando valores de dois vetores:
x = [1,2,3]
y = [4,5,6]
total = 0
for i in range(len(a)):
    total = total + x[i] * y[i]

# NUMPY:

# Calculando produto escalar com numpy:

import numpy as np

x = np.array([1,2,3])
y =  np.array([4,5,6])
# Usando método dot() para calcular:
np.dot(x,y)
# método sum() para multiplicar os vetores:
np.sum(x * y)
# criando matrizes multidimensionais com o método ones():
np.ones((3,3,3)) # 3 matrizes de 3 linhas e 3 colunas, respectivamente.

# Usando numpy, scipy e matplotlib para analisar dados:

import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# Dados que o usuário inseriu:
A = [4.0, 3.5, 3.0, 2.5, 2.0]
B = [1.31, 1.14, 0.97, 0.81, 0.76]
AError = [0.2, 0.2, 0.2, 0.2, 0.2]
BError = [0.03, 0.02, 0.04, 0.02, 0.05]

print("Exsstimated B for each error:\n")

for i in range(5):
    print(str(A[i]) + "+-" + str(AError[i]) + ": " + str(B[i]) + "+-" + str(BError[i]))
# aplicando a biblioteca numpy para fazer dos dados brutos uma matriz multidimensional:
x = np.array(A)
y = np.array(B)
xError = np.array(AError)
yError = np.array(BError)

# defifinindo uma função linear para ajuste do gráfico:
def func(d,e,f):
    return d * e + f
# Criando um matriz com infos de variância e covariância de inclinação:
w, u = opt.curve_fit(func, x, y)
# aplicando cordenadas x e o resultado otimizado sobre o ajuste da curva(opt.curve_fit) para encontrar a linha de melhor ajuste:
yflit = func(x, *w)

# Usando matplotlib para criar gráfico:
# Personalizando gráfico:
plt.errorbar(A,B, xerr= AError, yerr= BError, fmt= "o" , ms = 3)
plt.plot(x, yflit, label = "flit", linewidth = 1.5, linestyle = "dashed")
# Adicionado titulos e etiquetas ao gráfico:
plt.title(" A vs B Custo benefício")
plt.xlabel(" Custo padrão esperado A (X)")
plt.ylabel("Benefícios de acordo com informações adicionadas B (Y)")
#Printando:
print("Parâmetros esperados entre A e B: ", w)
print("Variância esperada entre os meses: ", np.sqrt(np.diag(u)))
# salvando o gráfico:
plt.savefig("Teste.jpg")
plt.show()

# Embaralhando e sorteando elementos usando a biblioteca random:

import random

times = ["flamengo", "corinthians", "Vitoria", "Real Madrid" , "Manchester United"]
# Embaralhando lista:
random.shuffle(times)
# Sorteando um elemento da lista:
sorteio = random.choice(times)
# ordenando elementos de uma lista:
times.sort(reverse= True) # Ordem decrescente
times.sort(reverse= False) # Ordem crescente
# copiando elementos de uma lista:
times2 = list(times)
# fazendo backup de uma lista:
cursos_ti = ["s.i", "ads", "ciência da computação"]
lista_de_backup = ["s.i", "ads","ciência da computação"]

backup = list(lista_de_backup)

if backup == cursos_ti:
    cursos_ti.clear()
    print("Backup feito! A lista original foi excluida.")
else:
    print("Erro! as listas não são iguais.")

# contando quantas vezes um elem se repete em uma lista:
numeros = [1,1,12]
contagem = numeros.count(1)
# retorndo o elemento e o índice de uma lista com o método enumerate():

nomes = ["amelio", "Lassester", "michel scott"]

for indice, elementos in enumerate(nomes):
    print(f"{elementos} está contido no índice {indice}")

# criando uma lista aninhada:
matriz = [[1,2,3], [4,5,6], [7,8,9]]
# Somando elementos das listas aninhadas:
soma_matriz = matriz[0][1] + matriz[1][1] + matriz[2][1] # nesse exemplo foi somado todos os segundos elementos das listas, ultilizando os índices externos e internos.
# somando elementos de uma matriz:

lista = [[3,7,1], [6,9,0], [13,5,2]]

tr_A = 0 # Soma de elementos iguais da matriz
soma_a = 0 # Soma de todos os elem da matriz

lin = len(lista) # quantidade de elementos da lista
col = len(lista[0]) # Quantidades de elementos no primeiro indice da lista

for i in range(lin):
    for j in range(col):
        if i == j:
            # elementos iguais na diagonal da matriz:
            tr_A = tr_A + lista[i] [j]

        # Somando todos os elem:
        soma_a = soma_a + lista[i] [j]

print(f"Elementos iguais na diagonal da matriz: {tr_A}")
print(f"Soma de todos os elem: {soma_a}")
# Criando uma lista com o método "comprehensions":
# exemplos:
minha_lista = [x + 1 for x in range(10)]
minha_lista = [x for x in range(10) if x % 2 == 0] # retorna osvalores pares de 0 a 10.
minha_lista = [x for x in "HACKETON"]


# Aplicações Thread:

import threading

def trabalhador(num):

    while True:
        ativas = threading.active_count() -1
        print(f"Trabalhador {num} de {ativas} threads ativas.")
        # return

for i in range(5):
    t = threading.Thread( target = trabalhador, args = (i,))
    t.start()

# Programa que calcula uma função separadamente e compaçadamente usando threads e timesleep:

from math import sin
import time

def expoente(x):
    global resposta_expoente
    time.sleep(5)
    resposta_expoente = x ** 2

def multiplicacao(x):
    global resposta_multiplicacao
    time.sleep(10)
    resposta_multiplicacao = 5 * x

def seno(x):
    global resposta_seno
    time.sleep(15)
    resposta_seno = sin(x)

if __name__ == "__main__":
    x = 2

    thread_um = threading.Thread( target = expoente, args = (x,))
    thread_dois = threading.Thread( target = multiplicacao, args = (x,))
    thread_tres = threading.Thread(target = seno, args = (x,))
    thread_um.start()
    thread_um.join()
    thread_dois.start()
    thread_dois.join()
    thread_tres.start()
    thread_tres.join()

    soma_final = resposta_expoente + resposta_multiplicacao + resposta_seno
    print("Dada a função f(x) = x^2 + 5*x + sen(x)")
    print(f"Para x = {x}, temos como produto: {soma_final:.2f}")

# Programa que ilustra o consumidor e produtor no acesso de um "armazém":




















































































































