import os
import time
import multiprocessing

primos = [
    400000000000063,
    400000000000129,
    400000000000147,
    400000000000187,
    400000000000201,
    400000000000231,
    400000000000241,
    400000000000247,
    400000000000253,
    400000000000261,
    400000000000339,
    400000000000357,
    400000000000361,
    400000000000399,
    400000000000507,
    900000060000001,
    900001380000529,
    900002220001369,
    900002460001681,
    900002940002401,
]

def eh_primo_sequencial(n):
    if n <= 1:
        return False
    for primo in range(2, int(n**0.5) + 1):
        if n % primo == 0:
            return False
    return True

def eh_primo_paralelo(numeros):
    current_pid = os.getpid()  # Obtém o ID do processo atual
    for numero in numeros:
        if eh_primo_sequencial(numero):
            print(f"Processo {current_pid} - {numero} é primo")
        else:
            print(f"Processo {current_pid} - {numero} não é primo")

if __name__ == "__main__":
    start_time = time.perf_counter()

    # Número de processos a serem criados
    num_processos = multiprocessing.cpu_count()  # Usa o número de CPUs disponíveis
    pool = multiprocessing.Pool(processes=num_processos)

    # Divide a lista de números em partes iguais para cada processo
    chunk_size = len(primos) // num_processos
    chunks = [primos[i:i + chunk_size] for i in range(0, len(primos), chunk_size)]

    # Executa a função em paralelo
    pool.map(eh_primo_paralelo, chunks)

    pool.close()
    pool.join()

    end_time = time.perf_counter()
    print(f"Tempo total: {end_time - start_time:.2f} segundos")
