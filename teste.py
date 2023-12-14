from threading import Thread, Lock
import time 
import random


armazem = []
trava = Lock()

class ProdutorThread(Thread):
    def run(self):
        global armazem
        while True:
            trava.acquire()
            armazem.append(random.randrange(0, 9))
            print(f" Produção: {armazem[-1]}")
            print(f"Estoque: {armazem}")
            trava.release()
            time.sleep(random.random())

class ConsumidorThread(Thread):
    def run(self):
        global armazem
        while True:
            trava.acquire()
            if not armazem:
                print("Estoque vazio.")
            numero_de_consumo = armazem.pop(0)
            print(f" Consumo: {numero_de_consumo}")
            print(f" Estoque: {armazem}")
            trava.release()
            time.sleep(random.random())

if __name__ == "__main__":
    ProdutorThread.start()
    ConsumidorThread.start()
