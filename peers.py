import local as io
import net
peersFile = "peers.dat"
def getLocalPeers():
    return io.load(peersFile)
def addPeer(peer):
    print("added locally: "+peer)
    localPeers = getLocalPeers()
    for local in localPeers:
        if local != peer:
            io.append(str(peer), peersFile)
            break
