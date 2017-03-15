import local as io
peersFile = "peers.dat"
peers = []
def updatePeers():
    global peersFile
    global peers
    p = io.load(peersFile)
    #net.getPeers(p[0])
def getLocalPeers():
    return io.load(peersFile)
