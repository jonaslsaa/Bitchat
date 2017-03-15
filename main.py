import threading
import peers
import net
import local as io
isUser = False




def startup():
    if io.check(peers.peersFile) == False:
        print("error: missing peers file")

try:
   threading.Thread(target=net.checkForCommands).start()
except:
   print "Error: unable to start thread"


startup()

if isUser:
    print(peers.getLocalPeers())



