class Task:
    def __init__(self, nome, vencimento):
        # Inicializa uma tarefa com nome, data de vencimento e status de conclusão padrão como False.
        self.nome = nome
        self.vencimento = vencimento
        self.concluida = False

    def concluir(self):
        # Define o status de conclusão da tarefa como True (tarefa concluída).
        self.concluida = True

    def pendente(self):
        # Define o status de conclusão da tarefa como False (tarefa pendente).
        self.concluida = False

    def __str__(self):
        # Retorna uma representação da tarefa no formato "nome - vencimento (status)".
        status = "concluída" if self.concluida else "pendente"
        return f"{self.nome} - {self.vencimento} ({status})"


class TaskManager:
    def __init__(self):
        # Inicializa o gerenciador de tarefas com uma lista vazia para armazenar tarefas.
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        # Adiciona uma tarefa à lista de tarefas.
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        # Lista todas as tarefas na lista de tarefas numerando-as.
        for idx, tarefa in enumerate(self.tarefas):
            print(f"{idx + 1}. {tarefa}")

    def concluir_tarefa(self, id):
        # Marca uma tarefa como concluída com base no índice fornecido.
        if 1 <= id <= len(self.tarefas):
            self.tarefas[id - 1].concluir()
            print("Tarefa concluída.")
        else:
            print("ID inválido.")

    # ... outros métodos ...


class App:
    def __init__(self):
        # Inicializa a aplicação criando uma instância do gerenciador de tarefas.
        self.task_manager = TaskManager()

    def exibir_menu(self):
        # Exibe o menu de opções.
        print("---- MENU ----")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa Como Concluída")
        print("4. Remover Tarefa")
        print("5. Salvar Tarefas em Arquivo")
        print("7. Sair")

    def executar(self):
        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                # Solicita informações para criar uma nova tarefa e a adiciona ao gerenciador.
                nome = input("Entre com o nome da tarefa: ")
                data_vencimento = input("Data de vencimento da tarefa no formato DD/MM/AAAA: ")
                tarefa = Task(nome, data_vencimento)
                self.task_manager.adicionar_tarefa(tarefa)
            elif opcao == "2":
                # Lista todas as tarefas no gerenciador.
                self.task_manager.listar_tarefas()
            elif opcao == "3":
                # Marca uma tarefa como concluída com base no índice fornecido.
                id = int(input("Digite o número da tarefa: "))
                self.task_manager.concluir_tarefa(id)
            # ... outros casos ...

            elif opcao == "7":
                print("Saindo...")
                break
            else:
                print("Opção inválida")

if __name__ == "__main__":
    # Cria uma instância da aplicação e a executa.
    app = App()
    app.executar()
