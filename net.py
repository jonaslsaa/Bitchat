import time
import socket
import threading
import peers
import string
import random

history = []

def StartListen():
    host = "127.0.0.1"
    port = 1900
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    
    while 1:
        data, addr = sock.recvfrom(1024)
        gotData(data, addr) # < upgrade to threading
    sock.close()
    
def gotData(rawdata, addr):
    print(rawdata)
    rawdata = data.split("|")
    
    if data[0] == "msg":
        canPost = True
        if len(data) >= 3:
            for c in history:
                if c == data[2]: # checks if has been posted
                    canPost = False
            if canPost == True:
                print(data[1])
                history.append(data[2])
                for a in peers.alives:
                    if a != addr:
                        SendData(rawdata, a)
    
    if data[0] == "ping":
        SendData("alive", addr)
        peers.alives.append(addr)
    if data[0] == "alive":
        peers.alives.append(addr)
    if data[0] == "peer":
        if len(data[1]) >= 1:
            peer.addPeer(data[1])
    if data[0] == "updatepeers":
        if len(data[1]) >= 1:
            peers = peers.getLocalPeers()
            for p in peers:
                SendData("peer|"+str(p), addr)

                
def SendData(data, host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(bytes(data, "utf-8"), (host, 1900))


def id(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
