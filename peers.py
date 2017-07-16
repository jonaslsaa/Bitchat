import local as io
import net
peersFile = "peers.dat"
def getLocalPeers():
    return io.load(peersFile)
def addPeer(peer):
    print("added locally: "+peer)
    localPeers = getLocalPeers()
    if peer not in localPeers:
        io.append(str(peer), peersFile)
