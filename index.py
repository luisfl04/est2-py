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





































































































