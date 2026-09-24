# fila-atendimento-hands-on

## Sistema Inteligente de Atendimento

Projeto desenvolvido em Python para demonstrar três formas de organização de clientes em uma central de atendimento:

- Fila clássica (FIFO);
- Fila circular;
- Fila de prioridade.

O projeto também possui uma simulação automática com 20 clientes e um menu interativo.

---

## Integrantes

Preencha com os nomes dos integrantes do grupo:

- Integrante 1: ______________________________
- Integrante 2: ______________________________
- Integrante 3: ______________________________
- Integrante 4: ______________________________

---

## Contexto

Cada cliente possui:

- **Nome**
- **Senha**
- **Prioridade**

As prioridades são:

| Valor | Tipo |
|---|---|
| 1 | Emergência |
| 2 | Prioritário |
| 3 | Atendimento normal |

Na fila de prioridade, valores menores possuem preferência.

---

## Estrutura do projeto

```text
fila-atendimento-hands-on/
├── fila_classica.py
├── fila_circular.py
├── fila_prioridade.py
├── main.py
└── README.md
```

### `fila_classica.py`

Implementa a classe `Fila` utilizando o princípio FIFO (First In, First Out).

Operações:

- `enqueue(cliente)` — insere um cliente;
- `dequeue()` — remove e retorna o próximo cliente;
- `head()` — consulta o próximo cliente sem removê-lo;
- `size()` — retorna a quantidade de clientes;
- `empty()` — verifica se a fila está vazia.

A demonstração cadastra inicialmente 10 clientes e apresenta o atendimento na mesma ordem em que chegaram.

### `fila_circular.py`

Implementa uma fila circular com capacidade fixa de 5 elementos.

Além das operações básicas, são apresentados:

- `front` — índice da próxima posição a ser removida;
- `rear` — índice da próxima posição disponível para inserção;
- `full()` — verifica se a fila está cheia.

O índice é atualizado utilizando:

```python
indice = (indice + 1) % capacidade
```

Isso permite que, ao chegar ao final do vetor, a fila volte para a primeira posição disponível.

### `fila_prioridade.py`

Utiliza o módulo `heapq` da biblioteca padrão do Python.

Cada entrada do heap segue o formato:

```python
(prioridade, contador, cliente)
```

O primeiro campo determina a prioridade. O segundo preserva a ordem de chegada quando dois clientes possuem a mesma prioridade.

---

## Como executar

É necessário ter Python 3 instalado.

Não são necessárias bibliotecas externas.

### Executar o desafio completo

No terminal:

```bash
python main.py
```

O programa:

1. gera 20 clientes;
2. mostra a ordem de chegada;
3. executa a fila clássica;
4. demonstra a fila circular;
5. executa a fila de prioridade;
6. apresenta uma comparação;
7. abre o menu interativo.

### Executar cada demonstração separadamente

Fila clássica:

```bash
python fila_classica.py
```

Fila circular:

```bash
python fila_circular.py
```

Fila de prioridade:

```bash
python fila_prioridade.py
```

---

# Demonstração das estruturas

## 1. Fila clássica

A fila clássica segue o princípio FIFO:

> o primeiro cliente que entra é o primeiro cliente atendido.

Exemplo:

```text
Entrada:
Ana
Bruno
Carla
Diego

Atendimento:
Ana
Bruno
Carla
Diego
```

A estrutura é adequada quando não existe necessidade de alterar a ordem de atendimento.

---

## 2. Fila circular

A fila circular utiliza um vetor de capacidade fixa.

Exemplo conceitual com capacidade 5:

```text
[ C001 | C002 | C003 | C004 | C005 ]
    ↑                              ↑
  front                            rear
```

Depois que alguns clientes são removidos, as posições liberadas podem ser reutilizadas:

```text
[ C006 | C007 | C003 | C004 | C005 ]
```

O objetivo da demonstração é mostrar que o `rear` pode voltar para o início do vetor.

### O que acontece ao tentar inserir em uma fila circular cheia?

Quando a fila está cheia, não existe posição disponível para armazenar outro elemento. Neste projeto, `enqueue()` retorna `False` e o novo cliente não é inserido.

---

# 3. Fila de prioridade

Na fila de prioridade, a ordem de chegada não é necessariamente a ordem de atendimento.

A regra utilizada é:

```text
1 - Emergência
2 - Prioritário
3 - Normal
```

Portanto, um cliente que chegou depois pode ser atendido antes de outro que chegou anteriormente se possuir uma prioridade numericamente menor.

Quando dois clientes possuem a mesma prioridade, o contador de chegada é utilizado para preservar a ordem FIFO entre eles.

---

# Desafio final

O programa gera automaticamente 20 clientes com prioridades entre 1 e 3.

A simulação apresenta:

1. clientes na ordem de chegada;
2. atendimento utilizando FIFO;
3. comportamento da fila circular, incluindo `front` e `rear`;
4. atendimento utilizando prioridade;
5. comparação entre os resultados.

Para tornar os testes reproduzíveis, foi utilizado:

```python
random.seed(42)
```

Assim, a mesma execução gera a mesma sequência de prioridades.

---

# Respostas do relatório

## 1. Por que a ordem de atendimento da fila de prioridade pode ser diferente da ordem da fila clássica?

Porque as duas estruturas utilizam critérios diferentes.

Na fila clássica, o único critério é a ordem de chegada: quem chega primeiro é atendido primeiro.

Na fila de prioridade, o sistema considera a prioridade do cliente. Como a prioridade 1 possui preferência sobre as prioridades 2 e 3, um cliente que chegou posteriormente pode ser atendido antes de alguém que chegou anteriormente.

Exemplo:

```text
Chegada:
Cliente A -> prioridade 3
Cliente B -> prioridade 1
Cliente C -> prioridade 3

Fila clássica:
A -> B -> C

Fila de prioridade:
B -> A -> C
```

Em caso de empate de prioridade, este projeto mantém a ordem de chegada por meio do contador associado ao cliente.

---

## 2. Em quais situações reais uma fila de prioridade seria mais adequada?

Uma fila de prioridade é adequada quando os clientes não devem necessariamente ser atendidos apenas pela ordem de chegada.

Alguns exemplos:

- pronto-socorro hospitalar;
- central de atendimento de emergências;
- suporte técnico com chamados críticos;
- sistemas operacionais que precisam executar tarefas mais urgentes;
- atendimento bancário para situações excepcionais;
- centrais de infraestrutura com incidentes críticos.

Nesses casos, a prioridade pode representar o grau de urgência ou impacto de cada atendimento.

---

## 3. Quais são as vantagens e limitações de uma fila circular?

### Vantagens

- Reutiliza as posições liberadas do vetor.
- Evita movimentar todos os elementos após uma remoção.
- Possui capacidade fixa e previsível.
- É útil em buffers e sistemas que trabalham continuamente com entrada e saída de dados.
- Permite controlar a ocupação utilizando `front`, `rear` e tamanho.

### Limitações

- A capacidade é limitada ao tamanho definido.
- Uma fila cheia não pode receber outro elemento até que uma posição seja liberada.
- A implementação exige controle cuidadoso dos índices.
- É necessário diferenciar situações de fila vazia e fila cheia.

---

## 4. O que acontece ao tentar inserir um elemento em uma fila circular cheia?

A inserção não deve ocorrer, pois não há espaço disponível.

Neste projeto, o método:

```python
enqueue()
```

retorna:

```python
False
```

quando a fila está cheia.

Dessa forma, o programa informa que a operação não foi realizada sem sobrescrever um cliente que ainda está aguardando atendimento.

---

# Comparação das estruturas

| Estrutura | Critério de atendimento | Capacidade | Principal característica |
|---|---|---:|---|
| Fila clássica | Ordem de chegada | Dinâmica | FIFO |
| Fila circular | Ordem de chegada | Fixa | Reutilização de posições |
| Fila de prioridade | Prioridade + ordem de chegada | Dinâmica | Urgências primeiro |

## Conclusão

As três estruturas resolvem problemas relacionados a filas, mas possuem objetivos diferentes.

A fila clássica é indicada quando todos os clientes devem seguir rigorosamente a ordem de chegada.

A fila circular é útil quando existe uma capacidade fixa e é necessário reutilizar eficientemente as posições de armazenamento.

A fila de prioridade é indicada quando alguns clientes precisam ser atendidos antes de outros devido à sua prioridade. Neste projeto, a ordem de chegada continua sendo importante para desempatar clientes com a mesma prioridade.

---

# Evidências de testes

Ao executar:

```bash
python main.py
```

o terminal apresenta:

- os 20 clientes gerados;
- suas senhas e prioridades;
- a ordem FIFO;
- os eventos de `enqueue` e `dequeue` da fila circular;
- os valores de `front` e `rear`;
- a ordem da fila de prioridade;
- a comparação final.

Para a entrega, recomenda-se capturar screenshots do terminal e adicioná-los ao repositório, por exemplo:

```text
evidencias/
├── fila_classica.png
├── fila_circular.png
├── fila_prioridade.png
└── desafio_final.png
```

---

# GitHub

O repositório deve possuir o nome:

```text
fila-atendimento-hands-on
```

Depois de criar o repositório no GitHub, os comandos básicos são:

```bash
git init
git add .
git commit -m "Implementa sistema de filas de atendimento"
git branch -M main
git remote add origin URL_DO_REPOSITORIO
git push -u origin main
```

Substitua `URL_DO_REPOSITORIO` pela URL do repositório criado.

Depois, copie o link do GitHub e envie no Blackboard.

---

# Bônus: menu interativo

O arquivo `main.py` possui um menu que permite:

1. Inserir cliente;
2. Atender próximo cliente;
3. Consultar próximo cliente;
4. Visualizar a fila;
5. Executar o desafio com 20 clientes;
0. Sair.

A fila utilizada no menu é a fila de prioridade, permitindo simular um cenário mais próximo de uma central em que atendimentos urgentes precisam ser tratados primeiro.
