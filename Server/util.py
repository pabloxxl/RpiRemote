#IMPORTS
import socket
from os import listdir,getcwd,chdir
from pickle import dumps,loads
#IMPORTS

class RpiListener:
  PORT = 5003 #Port to listen to
  def __init__(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

  def bind(self):
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Enables rebinding of socket
    self.sock.bind(('',self.PORT))
    self.sock.listen(5)

  def listenForCmd(self):
    client,addr = self.sock.accept() 
    print 'Incomming connection from ', addr
    cmd = client.recv(128)
    client.close()
    return cmd

  def unbind(self):
    self.sock.close()

class DirectoryHandler:
  def __init__(self,path):
    if path!=getcwd():
      chdir(path)
  def dirName(self):
    return getcwd()
  def changeDir(self,name)
    try:
      chdir(name)
    except:
    print "Directory "+name+" not found"
  def getFiles(self)
    files = listdir(getcwd())
    return dumps(files)
