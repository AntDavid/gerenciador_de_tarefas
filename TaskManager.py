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

    def remover_tarefa(self, id):
        # Remove uma tarefa com base no índice fornecido.
        if 1 <= id <= len(self.tarefas):
            del self.tarefas[id - 1]
            print("Tarefa removida.")
        else:
            print("ID inválido.")

    def salvar_arquivo(self, nome_arquivo):
        # Salva as informações das tarefas em um arquivo CSV.
        with open(nome_arquivo, "w") as arquivo:
            for tarefa in self.tarefas:
                arquivo.write(f"{tarefa.nome},{tarefa.vencimento},{tarefa.concluida}\n")
        print("Tarefas salvas no arquivo.")

    def carregar_arquivo(self, nome_arquivo):
        # Carrega as informações das tarefas de um arquivo CSV.
        self.tarefas = []
        try:
            with open(nome_arquivo, "r") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(",")
                    nome, vencimento, status = dados
                    tarefa = Task(nome, vencimento)
                    if status == "True":
                        tarefa.concluir()
                    self.tarefas.append(tarefa)
            print("Tarefas carregadas do arquivo.")
        except FileNotFoundError:
            print("Arquivo não encontrado.")

