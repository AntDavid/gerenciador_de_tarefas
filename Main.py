from task import Task
from task_manager import TaskManager

class Main:
    def __init__(self):
        # Inicializa a aplicação criando uma instância do gerenciador de tarefas.
        self.app = App()

    def executar(self):
        # Inicia a execução da aplicação.
        self.app.executar()

class App:
    def __init__(self):
        # Cria uma instância do gerenciador de tarefas.
        self.task_manager = TaskManager()

    def exibir_menu(self):
        # Exibe o menu de opções.
        print("---- MENU ----")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa Como Concluída")
        print("4. Remover Tarefa")
        print("5. Salvar Tarefas em Arquivo")
        print("6. Carregar Tarefas de Arquivo")
        print("7. Sair")

    def executar(self):
        # Loop principal da aplicação.
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
            elif opcao == "4":
                # Remove uma tarefa com base no índice fornecido.
                id = int(input("Digite o número da tarefa: "))
                self.task_manager.remover_tarefa(id)
            elif opcao == "5":
                # Salva as tarefas em um arquivo.
                nome_arquivo = input("Digite o nome do arquivo para salvar: ")
                self.task_manager.salvar_arquivo(nome_arquivo)
            elif opcao == "6":
                # Carrega as tarefas de um arquivo.
                nome_arquivo = input("Digite o nome do arquivo para carregar: ")
                self.task_manager.carregar_arquivo(nome_arquivo)
            elif opcao == "7":
                print("Saindo...")
                break
            else:
                print("Opção inválida")

if __name__ == "__main__":
    # Cria uma instância da classe `Main` e inicia a execução da aplicação.
    main = Main()
    main.executar()
