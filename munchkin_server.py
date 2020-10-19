#############################################
# Author: Pranay Gundam
#############################################

# most of the basic beginning code to set up the socket and threading connections
# came from the TA mini-lecture starter code made by Rohan Varma and adapted by 
# Kyle Chin/Ping-Ya Chao
import socket
import threading
from queue import Queue

# Be sure to specify a both a IP address in HOST and a port in PORT. If you want
# to play local multiplayer then just put your internal IP address in HOST and
# specify any port above 50000. If you want to play non-local multiplayer then
# put you external IP address in HOST and assign PORT to a forwarded port.
HOST = ""
PORT = 64425
BACKLOG = 4

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', PORT))
server.listen(BACKLOG)

print(server.getsockname())

print("looking for connection")


def handleClient(client, serverChannel, cID, clientele):
    client.setblocking(1)
    msg = ""
    while True:
        try:
            msg += client.recv(10).decode("UTF-8")
            command = msg.split("\n")
            while len(command) > 1:
                readyMsg = command[0]
                msg = "\n".join(command[1:])
                serverChannel.put(str(cID) + " " + readyMsg)
                command = msg.split("\n")
        except:
            print('we failed in server')
            return

def serverThread(clientele, serverChannel):
    while True:
        msg = serverChannel.get(True, None)
        print("msg recv: " + msg)
        msgList = msg.split(" ")
        senderID = msgList[0]
        instruction = msgList[1]
        details = " ".join(msgList[2:])
        if details != "":
            for cID in clientele:  # Note: cID is just an abbreviation for client ID
                if cID != senderID:
                    sendMsg = instruction + " " + senderID + " " + details + "\n"
                    clientele[cID].send(sendMsg.encode())
                    print("> sent to %s:" % cID, sendMsg[:-1])
        print()
        serverChannel.task_done()


clientele = dict()
playerNum = 0

serverChannel = Queue(100)
threading.Thread(target=serverThread, args=(clientele, serverChannel)).start()

names = ["0", "1", "2", "3"]

while True:
    client, address = server.accept()
    # myID is the key to the client in the clientele dictionary
    myID = names[playerNum]
    print(myID, playerNum)
    for cID in clientele:
        print(repr(cID), repr(playerNum))
        clientele[cID].send((f"newPlayer {myID}\n").encode())
        client.send((f"newPlayer {cID}\n").encode())
    clientele[myID] = client
    client.send((f"myIDis {myID} \n").encode())
    print(f"connection recieved from {myID}")
    threading.Thread(target=handleClient, args=
    (client, serverChannel, myID, clientele)).start()
    playerNum += 1
