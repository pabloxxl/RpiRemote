#IMPORTS
from socket import *
from ConfigParser import ConfigParser
#IMPORTS

class Config(object):
  def __init__(self,path):
    self.parser = ConfigParser()
    if self.parser.read(path):
      self.parsed = True
      print "Config file loaded"
    else:
      self.parsed = False
      print "Could not read config file"
  def parseConfig(self):
    if self.parsed:
      self.__parseIp()
      self.__parsePort()
    else:
      self.ip = "127.0.0.1"
      self.port = 5000

  def __parseIp(self):
    try:
      self.ip = self.parser.get("config","ip")
    except:
      self.ip = "127.0.0.1" 
      print "Could not parse ip adress"

  def __parsePort(self):
    try:
      sPort = self.parser.get("config","port")
      self.port = int(sPort)
    except:
      self.port = 5000
      print "Could not parse port"

		
class RpiConnect(object):
  def __init__(self,ip,port):
    self.ip = ip
    self.port = port
    self.sock = socket(AF_INET, SOCK_STREAM)

  def connect(self):
    self.sock.connect((self.ip,self.port))
    print "Connected"

  def disconnect(self):
    self.sock.close()
    print "Disconnected"
  
  def send(self,msg):
    if self.sock.send(msg):
      print msg+" sent"
  
  def recv(self):
    print "Waiting for answer from Rpi"
    answer = self.sock.recv(128)
    print "Answer from Rpi: "+answer
    return answer

