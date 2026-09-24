from fila_classica import Fila
from fila_circular import FilaCircular
from fila_prioridade import FilaPrioridade, nome_prioridade

import random


def criar_cliente(numero):
    prioridades = [1, 2, 3]
    nomes = [
        "Ana", "Bruno", "Carla", "Diego", "Eduarda",
        "Felipe", "Gabriela", "Henrique", "Isabela", "Joao",
        "Karen", "Lucas", "Marina", "Nicolas", "Olivia",
        "Paulo", "Quezia", "Rafael", "Sofia", "Tiago"
    ]

    return {
        "nome": nomes[numero - 1],
        "senha": f"S{numero:03d}",
        "prioridade": random.choice(prioridades)
    }


def imprimir_cliente(cliente):
    return (
        f"{cliente['senha']} - {cliente['nome']} - "
        f"prioridade {cliente['prioridade']} "
        f"({nome_prioridade(cliente['prioridade'])})"
    )


def gerar_clientes(qtd=20, seed=42):
    random.seed(seed)
    return [criar_cliente(i) for i in range(1, qtd + 1)]


def simular_fila_classica(clientes):
    fila = Fila()
    for cliente in clientes:
        fila.enqueue(cliente)

    atendidos = []
    while not fila.empty():
        atendidos.append(fila.dequeue())
    return atendidos


def simular_fila_prioridade(clientes):
    fila = FilaPrioridade()
    for cliente in clientes:
        fila.enqueue(cliente)

    atendidos = []
    while not fila.empty():
        atendidos.append(fila.dequeue())
    return atendidos


def simular_fila_circular(clientes, capacidade=5):
    fila = FilaCircular(capacidade)
    atendidos = []
    eventos = []

    proximo = 0

    while proximo < len(clientes) or not fila.empty():
        while proximo < len(clientes) and not fila.full():
            cliente = clientes[proximo]
            fila.enqueue(cliente)
            eventos.append(
                f"enqueue {cliente['senha']} | front={fila.front} "
                f"rear={fila.rear} | estado={fila}"
            )
            proximo += 1

        if not fila.empty():
            cliente = fila.dequeue()
            atendidos.append(cliente)
            eventos.append(
                f"dequeue {cliente['senha']} | front={fila.front} "
                f"rear={fila.rear} | estado={fila}"
            )

    return atendidos, eventos


def desafio_final():
    clientes = gerar_clientes(20)

    print("\n" + "=" * 78)
    print("DESAFIO FINAL - 20 CLIENTES")
    print("=" * 78)

    print("\n1. CLIENTES NA ORDEM DE CHEGADA")
    for i, cliente in enumerate(clientes, 1):
        print(f"{i:02d}. {imprimir_cliente(cliente)}")

    classica = simular_fila_classica(clientes)
    circular, eventos = simular_fila_circular(clientes)
    prioridade = simular_fila_prioridade(clientes)

    print("\n2. ORDEM DE ATENDIMENTO - FILA CLÁSSICA (FIFO)")
    for i, cliente in enumerate(classica, 1):
        print(f"{i:02d}. {imprimir_cliente(cliente)}")

    print("\n3. COMPORTAMENTO - FILA CIRCULAR (capacidade 5)")
    for evento in eventos:
        print("   " + evento)

    print("\nAtendimento resultante da simulação circular:")
    for i, cliente in enumerate(circular, 1):
        print(f"{i:02d}. {imprimir_cliente(cliente)}")

    print("\n4. ORDEM DE ATENDIMENTO - FILA DE PRIORIDADE")
    for i, cliente in enumerate(prioridade, 1):
        print(f"{i:02d}. {imprimir_cliente(cliente)}")

    print("\n5. COMPARAÇÃO")
    print("- Fila clássica: respeita integralmente a ordem de chegada.")
    print("- Fila circular: mantém FIFO, mas reutiliza posições do vetor.")
    print("- Fila de prioridade: atende primeiro menor valor de prioridade;")
    print("  em empate, mantém a ordem de chegada.")

    ordem_fifo = [c["senha"] for c in classica]
    ordem_prio = [c["senha"] for c in prioridade]

    print("\nA ordem FIFO e a ordem por prioridade são iguais?",
          ordem_fifo == ordem_prio)

    return clientes


def menu_interativo():
    fila = FilaPrioridade()
    contador = 1

    while True:
        print("\n" + "=" * 50)
        print("SISTEMA INTELIGENTE DE ATENDIMENTO")
        print("=" * 50)
        print("1 - Inserir cliente")
        print("2 - Atender próximo cliente")
        print("3 - Consultar próximo cliente")
        print("4 - Visualizar fila")
        print("5 - Executar desafio com 20 clientes")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome: ").strip()
            senha = f"M{contador:03d}"

            try:
                prioridade = int(
                    input("Prioridade (1-Emergência, 2-Prioritário, 3-Normal): ")
                )
                if prioridade not in (1, 2, 3):
                    raise ValueError
            except ValueError:
                print("Prioridade inválida. Use 1, 2 ou 3.")
                continue

            cliente = {
                "nome": nome,
                "senha": senha,
                "prioridade": prioridade
            }
            fila.enqueue(cliente)
            contador += 1
            print(f"Cliente inserido: {imprimir_cliente(cliente)}")

        elif opcao == "2":
            cliente = fila.dequeue()
            if cliente is None:
                print("Não há clientes aguardando.")
            else:
                print(f"Atendendo: {imprimir_cliente(cliente)}")

        elif opcao == "3":
            cliente = fila.head()
            if cliente is None:
                print("A fila está vazia.")
            else:
                print(f"Próximo: {imprimir_cliente(cliente)}")

        elif opcao == "4":
            if fila.empty():
                print("A fila está vazia.")
            else:
                print(f"Total de clientes: {fila.size()}")
                copia = sorted(fila._heap)
                for i, (_, _, cliente) in enumerate(copia, 1):
                    print(f"{i:02d}. {imprimir_cliente(cliente)}")

        elif opcao == "5":
            desafio_final()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    desafio_final()

    print("\n" + "=" * 78)
    print("MENU INTERATIVO")
    print("=" * 78)
    menu_interativo()
