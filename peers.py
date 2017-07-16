import local as io
import net
peersFile = "peers.dat"
def getLocalPeers():
    print("added locally "+x)
    return io.load(peersFile)
def addPeer(peer):
    localPeers = getLocalPeers()
    for local in localPeers:
        if local != peer:
            io.append(str(peer), peersFile)
            break
