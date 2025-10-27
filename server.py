import zmq
import json
from const import *


value = []

context = zmq.Context()
socket = context.socket(zmq.REP)  
socket.bind("tcp://*:" + PORT) 

print(f"Servidor ZeroMQ iniciado e escutando na porta {PORT}...")

while True:
    message = socket.recv_json()
    print(f"Recebido do cliente: {message}")

    operation = message.get("operation")
    payload = message.get("payload")
    
    response = {"status": "OK", "result": None}

    try:
        if operation == "append":
            value.append(payload)
            response["result"] = value
        elif operation == "insert":
            index, data = payload
            value.insert(index, data)
            response["result"] = value
        elif operation == "remove":
            value.remove(payload)
            response["result"] = value
        elif operation == "sort":
            value.sort()
            response["result"] = value
        elif operation == "search":
            response["result"] = payload in value
        elif operation == "get_by_index":
            response["result"] = value[payload]
        elif operation == "value":
            response["result"] = value
        elif operation == "clear":
            value = []
            response["result"] = value
        elif operation == "STOP":
            response["status"] = "Servidor encerrando..."
            socket.send_json(response)
            break
        else:
            response["status"] = "ERRO: Operação desconhecida."

    except Exception as e:
        response["status"] = f"ERRO: {str(e)}"

    socket.send_json(response)

print("Servidor encerrado.")