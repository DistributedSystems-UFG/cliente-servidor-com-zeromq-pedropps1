import multiprocessing #-
import zmq
from time import sleep #-
from const import *

def client():
  context = zmq.Context()
  socket  = context.socket(zmq.REQ)       # create request socket

  socket.connect("tcp://"+ HOST + PORT) # block until connected
  socket.send(b"Hello world")             # send message
  message = socket.recv()                 # block until response
  socket.send(b"STOP")                    # tell server to stop
  print(message.decode())                 # print result
#-
if __name__ == "__main__": #-
  s = multiprocessing.Process(target=server) #-
  c = multiprocessing.Process(target=client) #-
#-
  s.start() #-
  sleep(2) #-
  c.start() #-
  c.join() #-
  s.join() #-
