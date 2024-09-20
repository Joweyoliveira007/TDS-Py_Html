def critical_section(self, name):
        with self.lock:
            # Seção crítica onde apenas um processo pode acessar por vez
            print(f'Processo {name} está acessando a seção crítica.')
            time.sleep(1)  # Simula uma tarefa demorada
            print(f'Processo {name} saiu da seção crítica.')

def worker(monitor, name):
    for _ in range(5):
        monitor.critical_section(name)
        time.sleep(0.5)  # Tempo fora da seção crítica

if _name_ == '_main_':
    monitor = Monitor()

    # Criação de processos
    process1 = multiprocessing.Process(target=worker, args=(monitor, 'A'))
    process2 = multiprocessing.Process(target=worker, args=(monitor, 'B'))

    # Início dos processos
    process1.start()
    process2.start()

    # Espera até que os processos sejam concluídos
    process1.join()
    process2.join()

    print("Todos os processos foram concluídos")