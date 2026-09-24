class FilaCircular:
    """Fila circular com capacidade fixa."""

    def __init__(self, capacidade):
        if capacidade <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")

        self.capacidade = capacidade
        self._dados = [None] * capacidade
        self.front = 0
        self.rear = 0
        self._tamanho = 0

    def enqueue(self, cliente):
        if self._tamanho == self.capacidade:
            return False

        self._dados[self.rear] = cliente
        self.rear = (self.rear + 1) % self.capacidade
        self._tamanho += 1
        return True

    def dequeue(self):
        if self.empty():
            return None

        cliente = self._dados[self.front]
        self._dados[self.front] = None
        self.front = (self.front + 1) % self.capacidade
        self._tamanho -= 1
        return cliente

    def head(self):
        if self.empty():
            return None
        return self._dados[self.front]

    def size(self):
        return self._tamanho

    def empty(self):
        return self._tamanho == 0

    def full(self):
        return self._tamanho == self.capacidade

    def estado(self):
        return self._dados.copy()

    def __str__(self):
        itens = []
        for item in self._dados:
            if item is None:
                itens.append("-")
            else:
                itens.append(item["senha"])
        return "[" + " | ".join(itens) + "]"


if __name__ == "__main__":
    print("=== DEMONSTRAÇÃO DA FILA CIRCULAR ===")

    fila = FilaCircular(5)
    clientes = [
        {"nome": "Ana", "senha": "C001", "prioridade": 3},
        {"nome": "Bruno", "senha": "C002", "prioridade": 2},
        {"nome": "Carla", "senha": "C003", "prioridade": 3},
        {"nome": "Diego", "senha": "C004", "prioridade": 1},
        {"nome": "Eduarda", "senha": "C005", "prioridade": 2},
        {"nome": "Felipe", "senha": "C006", "prioridade": 3},
    ]

    def mostrar(acao):
        print(
            f"{acao:<42} | front={fila.front} rear={fila.rear} "
            f"tamanho={fila.size()} estado={fila}"
        )

    for cliente in clientes[:5]:
        fila.enqueue(cliente)
        mostrar(f"Inserido {cliente['senha']}")

    removido1 = fila.dequeue()
    mostrar(f"Removido {removido1['senha']}")

    removido2 = fila.dequeue()
    mostrar(f"Removido {removido2['senha']}")

    for cliente in clientes[5:]:
        if fila.enqueue(cliente):
            mostrar(f"Inserido novamente {cliente['senha']}")
        else:
            mostrar(f"Fila cheia; não inserido {cliente['senha']}")

    print("\nA posição ocupada anteriormente é reutilizada quando rear volta ao início.")
