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
    #print(peers[0])
    for addr in peers:
        #print("addr: "+addr)
        net.SendData("ping", addr)

def cleanup():
    clean = []
    wasCleaned = False
    global alives
    for i in alives:
        if i not in clean:
            clean.append(i)
            wasCleaned == True
    if wasCleaned == True:
        alives = clean
            

def updatePeers():
    global alives
    for addr in alives:
        net.SendData("updatepeers", addr)

def aliveAppend(x):
    alives.append(x)
def getAlives():
    return alives
