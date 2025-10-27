# Client-Server com ZeroMQ para Manipulação de Listas

Este projeto demonstra a construção de uma aplicação cliente-servidor utilizando a biblioteca **ZeroMQ (ZMQ)** em Python. O objetivo é mostrar como os padrões de comunicação do ZeroMQ, especificamente o padrão **REQ-REP** (Requisição-Resposta), simplificam a criação de sistemas distribuídos robustos.

O servidor expõe um serviço de manipulação de uma lista em memória, e o cliente invoca remotamente as operações disponíveis para modificar e consultar o estado dessa lista.

## Arquitetura e Padrão de Comunicação

O sistema utiliza o padrão REQ-REP do ZeroMQ, que impõe um fluxo de comunicação síncrono e estrito:
1.  O cliente inicia a comunicação enviando uma requisição (`zmq.REQ`).
2.  O servidor aguarda por uma requisição, a processa e envia uma única resposta de volta (`zmq.REP`).
3.  O cliente deve aguardar a resposta antes de poder enviar a próxima requisição.

Este padrão é ideal para serviços do tipo RPC (Remote Procedure Call), onde cada chamada de cliente espera um resultado direto.

A troca de dados estruturados (operações e argumentos) é feita utilizando **JSON**, aproveitando os métodos `send_json()` e `recv_json()` da biblioteca `pyzmq`.

## Funcionalidades Implementadas

O servidor oferece as seguintes operações remotas para manipular uma lista:

| Operação   | Payload (Dados)           | Descrição                                         |
| :--------- | :------------------------ | :------------------------------------------------ |
| `value`    | `None`                    | Retorna o estado atual da lista.                  |
| `append`   | `elemento`                | Adiciona um elemento ao final da lista.           |
| `insert`   | `[índice, elemento]`      | Insere um elemento em uma posição específica.     |
| `remove`   | `elemento`                | Remove a primeira ocorrência do elemento.         |
| `search`   | `elemento`                | Verifica se um elemento existe, retornando `True`/`False`. |
| `get_by_index`| `índice`                 | Retorna o elemento em um determinado índice.      |
| `sort`     | `None`                    | Ordena os elementos da lista.                     |
| `clear`    | `None`                    | Remove todos os elementos da lista.               |
| `STOP`     | `None`                    | Encerra a execução do servidor de forma limpa.    |

## Pré-requisitos

Certifique-se de que você tem o Python 3 e a biblioteca ZeroMQ para Python instalada.

Para instalar em um sistema baseado em Debian/Ubuntu:
```bash
sudo apt update
sudo apt install python3-zmq
```

## Como Executar o Sistema

**1. Configurar a Conexão**

Edite o arquivo `const.py` para definir o endereço do servidor.
*   Para testes na sua máquina local:
    ```python
    HOST = "localhost"
    ```
*   Para testes em um ambiente distribuído (ex: AWS):
    ```python
    HOST = "IP_PRIVADO_DA_INSTANCIA_DO_SERVIDOR"
    ```

**2. Iniciar o Servidor**

Abra um terminal, navegue até a pasta do projeto e execute:
```bash
python3 server.py
```
O servidor será iniciado e aguardará por requisições.

**3. Executar o Cliente**

Abra um **segundo terminal** e, na mesma pasta, execute o script do cliente:
```bash
python3 client.py
```
O cliente se conectará ao servidor, executará uma sequência de testes que demonstra todas as funcionalidades implementadas e, ao final, enviará um comando para encerrar o servidor.````