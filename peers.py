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
    for addr in peers:
        net.SendData("ping", addr)

def cleanup():
    clean = []
    global alives
    if len(alives[0]) > 0:
        clean.append(alives[0])
    for i in alives:
        for c in clean:
            if i != c:
                clean.append(i)
    alives = clean

def updatePeers():
    global alives
    for addr in alives:
        SendData("updatepeers", addr)
