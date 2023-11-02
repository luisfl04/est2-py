import string

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


