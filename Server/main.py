###IMPORTS
from util import RpiListener
from util import DirectoryHandler
from omx import OmxHandler
###IMPORTS

listener = RpiListener()
cp = OmxHandler()
cp.createFifo()
dir = DirectoryHandler("/home/pi") 
listener.bind()
print "Established listener. Waiting for incoming commands."

continueParsing = True
while continueParsing:
  cmd = listener.listenForCmd()
  continueParsing = cp.parseCmd(cmd)
listener.unbind()
cp.removeFifo()
