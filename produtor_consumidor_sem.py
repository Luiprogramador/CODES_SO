import threading
import time

saldo = 0
mutex = threading.Semaphore(1)

def deposita(valor):
    global saldo , mutex
    mutex.acquire()
    saldo_local = saldo
    time.sleep(5)
    saldo_local += valor
    saldo = saldo_local
    mutex.release()
    print(f"Saldo atual: {saldo}")

def saca(valor):
    global saldo, mutex
    mutex.acquire()
    saldo_local = saldo
    saldo_local -= valor
    saldo = saldo_local
    mutex.release()
    print(f"Saldo atual: {saldo}")


if __name__ == '__main__':
    print(f"Saldo inicial: {saldo}")
    threading.Thread(target=deposita, args=(1000,)).start()
    threading.Thread(target=deposita, args=(1000,)).start()
    threading.Thread(target=deposita, args=(1000,)).start()
    threading.Thread(target=deposita, args=(1000,)).start()

    s1 = threading.Thread(target=saca, args=(500,))

    s2 = threading.Thread(target=saca, args=(500,))
    s1.start()
    s2.start()
    s1.join()
    s2.join()
    time.sleep(10)
    print(f"Saldo final: {saldo}")
