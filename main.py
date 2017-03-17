import threading
import time
import peers
import net
import local as io

username = "annonymous"

def startup():
    if io.check(peers.peersFile) == False: # checks for peers file
        print("error: missing peers file")

    print(peers.getLocalPeers()) # prints peers
    
    threading.Thread(target=net.StartListen).start() # starts server
    threading.Thread(target=routine).start() # starts routine code

    usernm = input("\nusername (press enter for 'annonymous'): ")
    if usernm != "":
        global username
        username = usernm
    print("Connecting...")
    time.sleep(5)
    print(str(username)+" connected. \n\n\n")
    print("")
    
    while 1:
        messaging() # starts messaging code

def routine():
    while 1:
        peers.updatePeers() # tries to get more peers, expands network
        peers.gatherAlives() # organizes who is online
        peers.cleanup() # clean up code
        time.sleep(30) # does ^^ this every 5 minutes

def messaging():
    msg = input(": ")
    data = str(username) + ": " + str(msg)
    for addr in peers.alives:
        net.SendData("msg|"+data+"|"+net.id(), addr)
        
startup()
