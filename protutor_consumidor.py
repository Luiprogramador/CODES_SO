# Guilherme Santigo Gomes 22407909
# Cleudes Içami Kumeda Chirico 22401205
# Lui Mendes Jaime 22400660

import time
import random
import threading

N = 10
buffer = [None] * 10
count = 0

def produtor():
    global count, buffer
    while True:
        print(buffer)
        if count < N:
            iten = random.randint(0, 100)
            print(f"Produtor produziu item {iten}...")
            buffer[count] = iten
            count+=1
        time.sleep(0.5)
        

def consumidor():
    global count, buffer
    while True:
        if count > 0:
            iten_in_pos = buffer[count-1]
            buffer[count-1] = None
            count -= 1
            print(f"Consumidor consumiu item {iten_in_pos}...")
        time.sleep(1)


if __name__ == '__main__':
    produtor1 = threading.Thread(target=produtor)
    consumidor1 = threading.Thread(target=consumidor)

    produtor1.start()
    consumidor1.start()
    
    produtor1.join()
    consumidor1.join()

