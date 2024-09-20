import threading

class Monitor:
    def __init__(self):
        self.lock = threading.Lock()

    def critical_section(self):
        with self.lock:
            # Código da seção crítica
            print("Seção crítica acessada por", threading.current_thread().name)
# Exemplo de uso
monitor = Monitor()

def thread_function():
    for _ in range(5):
        monitor.critical_section()
# Criando threads
threads = []
for i in range(3):
    thread = threading.Thread(target=thread_function, name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()
# Esperando todas as threads terminarem
for thread in threads:
    thread.join()