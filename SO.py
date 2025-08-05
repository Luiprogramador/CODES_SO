import os
from time import sleep
import multiprocessing

# Função para imprimir 1000 iterações
def imprime_1000():
    current_pid = os.getpid()  # Obtém o ID do processo atual
    for i in range(1000):
        print(f"Processo {current_pid} executando iteração {i}")

# Função para imprimir 2000 iterações
def imprime_2000():
    current_pid = os.getpid()  # Obtém o ID do processo atual
    for i in range(2000):
        print(f"Processo {current_pid} executando iteração {i}")

# Função para executar os processos em paralelo
def run_processes():
    print("Iniciando processos em paralelo...")
    process1 = multiprocessing.Process(target=imprime_1000)
    process2 = multiprocessing.Process(target=imprime_2000)

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    print("Todos os processos foram concluídos.")

# Função principal
def main():
    # Exibe informações sobre o processo atual e o processo pai
    current_pid = os.getpid()
    parent_pid = os.getppid()
    print(f"O ID do processo pai é: {parent_pid}")
    print(f"O ID do processo atual é: {current_pid}")

    # Executa os processos em paralelo
    run_processes()

if __name__ == "__main__":
    # Limpa o terminal antes de iniciar
    os.system("cls" if os.name == "nt" else "clear")
    print("Iniciando o programa... Aguarde.")
    main()
    print("Finalizando o programa...")
    sleep(2)  # Pausa de 2 segundos antes de encerrar
    print("Programa encerrado.")
    sleep(3)  # Pausa de 3 segundos para visualização final
    os.system("cls" if os.name == "nt" else "clear")  # Limpa o terminal