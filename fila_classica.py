class Fila:
    """Fila clássica baseada no princípio FIFO (First In, First Out)."""

    def __init__(self):
        self._dados = []

    def enqueue(self, cliente):
        self._dados.append(cliente)

    def dequeue(self):
        if self.empty():
            return None
        return self._dados.pop(0)

    def head(self):
        if self.empty():
            return None
        return self._dados[0]

    def size(self):
        return len(self._dados)

    def empty(self):
        return len(self._dados) == 0

    def __str__(self):
        return " -> ".join(str(c) for c in self._dados)


if __name__ == "__main__":
    clientes = [
        {"nome": "Ana", "senha": "A001", "prioridade": 3},
        {"nome": "Bruno", "senha": "A002", "prioridade": 2},
        {"nome": "Carla", "senha": "A003", "prioridade": 3},
        {"nome": "Diego", "senha": "A004", "prioridade": 1},
        {"nome": "Eduarda", "senha": "A005", "prioridade": 2},
        {"nome": "Felipe", "senha": "A006", "prioridade": 3},
        {"nome": "Gabriela", "senha": "A007", "prioridade": 1},
        {"nome": "Henrique", "senha": "A008", "prioridade": 3},
        {"nome": "Isabela", "senha": "A009", "prioridade": 2},
        {"nome": "Joao", "senha": "A010", "prioridade": 3},
    ]

    fila = Fila()
    print("=== DEMONSTRAÇÃO DA FILA CLÁSSICA ===")
    print("Clientes na ordem de chegada:")

    for cliente in clientes:
        fila.enqueue(cliente)
        print(f"  {cliente['senha']} - {cliente['nome']}")

    print(f"\nTamanho da fila: {fila.size()}")
    print(f"Próximo cliente: {fila.head()['nome']}")

    print("\nOrdem de atendimento (FIFO):")
    while not fila.empty():
        cliente = fila.dequeue()
        print(f"  Atendendo {cliente['senha']} - {cliente['nome']}")
