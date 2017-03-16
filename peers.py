import local as io
import net
peersFile = "peers.dat"
alives = []
def getLocalPeers():
    return io.load(peersFile)
def addPeer(peer):
    localPeers = getLocalPeers()
    for local in localPeers:
        if local != peer:
            io.append(str(peer), peersFile)
            break
def gatherAlives():
    peers = getLocalPeers()
    global alives
    alives = []

def cleanup():
    pass

def updatePeers():
    for addr in alives:
        SendData("updatepeers", addr)
