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
    time.sleep(2)
    print(str(username)+" connected. \n\n\n")
    print("")

    while 1:
        messaging() # starts messaging code

def routine():
    while 1:
        print("updating peers")
        net.updatePeers() # tries to get more peers, expands network
        time.sleep(15)
        print("gathering peers")
        net.gatherAlives() # organizes who is online
        time.sleep(15) # does ^^ this every 5 minutes
        #net.cleanup() # clean up code, broken

def messaging():
    msg = input(": ")
    if msg != "":
        ID = net.id()
        data = str(username) + ": " + str(msg)
        alives = net.getAlives()
        for addr in alives:
            threading.Thread(target=net.SendData, args=("msg|"+data+"|"+ID,addr)).start()
        print(alives)

def message(mData, mAddr):
    net.SendData(mData, mAddr)


startup()
