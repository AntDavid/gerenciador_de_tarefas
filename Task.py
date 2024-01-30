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
