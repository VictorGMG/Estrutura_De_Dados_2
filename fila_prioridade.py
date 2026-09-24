import heapq


class FilaPrioridade:
    """
    Fila de prioridade usando heapq.

    A tupla (prioridade, contador, cliente) garante:
    - menor número de prioridade = atendimento primeiro;
    - contador = ordem de chegada em caso de empate.
    """

    def __init__(self):
        self._heap = []
        self._contador = 0

    def enqueue(self, cliente):
        entrada = (cliente["prioridade"], self._contador, cliente)
        heapq.heappush(self._heap, entrada)
        self._contador += 1

    def dequeue(self):
        if self.empty():
            return None
        _, _, cliente = heapq.heappop(self._heap)
        return cliente

    def head(self):
        if self.empty():
            return None
        return self._heap[0][2]

    def size(self):
        return len(self._heap)

    def empty(self):
        return len(self._heap) == 0


def nome_prioridade(valor):
    nomes = {
        1: "Emergência",
        2: "Prioritário",
        3: "Normal",
    }
    return nomes.get(valor, "Desconhecida")


if __name__ == "__main__":
    clientes = [
        {"nome": "Ana", "senha": "P001", "prioridade": 3},
        {"nome": "Bruno", "senha": "P002", "prioridade": 2},
        {"nome": "Carla", "senha": "P003", "prioridade": 3},
        {"nome": "Diego", "senha": "P004", "prioridade": 1},
        {"nome": "Eduarda", "senha": "P005", "prioridade": 2},
        {"nome": "Felipe", "senha": "P006", "prioridade": 1},
    ]

    fila = FilaPrioridade()

    print("=== DEMONSTRAÇÃO DA FILA DE PRIORIDADE ===")
    print("Clientes na ordem de chegada:")

    for cliente in clientes:
        fila.enqueue(cliente)
        print(
            f"  {cliente['senha']} - {cliente['nome']} - "
            f"{nome_prioridade(cliente['prioridade'])}"
        )

    print("\nOrdem de atendimento:")
    while not fila.empty():
        cliente = fila.dequeue()
        print(
            f"  Atendendo {cliente['senha']} - {cliente['nome']} - "
            f"prioridade {cliente['prioridade']} "
            f"({nome_prioridade(cliente['prioridade'])})"
        )
