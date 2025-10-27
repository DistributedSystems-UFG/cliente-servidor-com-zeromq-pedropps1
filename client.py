import zmq
from const import *

context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect("tcp://" + HOST + ":" + PORT)
print(f"Cliente conectado ao servidor em {HOST}:{PORT}")

def call_remote_procedure(operation, payload=None):
  request = {"operation": operation, "payload": payload}
  print(f"\n-> Enviando: {request}")
  
  socket.send_json(request)
  
  response = socket.recv_json()
  print(f"<- Recebido: {response}")
  return response

print("\n" + "="*30)
print("INICIANDO TESTES DE OPERAÇÕES REMOTAS COM ZEROMQ")
print("="*30)

call_remote_procedure("clear")

call_remote_procedure("append", 10)
call_remote_procedure("append", 30)
call_remote_procedure("append", 5)

call_remote_procedure("value")

call_remote_procedure("insert", [1, 20])

call_remote_procedure("sort")

call_remote_procedure("search", 30)
call_remote_procedure("search", 99)

call_remote_procedure("remove", 20)

call_remote_procedure("value")

print("\nEnviando comando para encerrar o servidor...")
call_remote_procedure("STOP")

print("\n" + "="*30)
print("TESTES CONCLUÍDOS")
print("="*30)
