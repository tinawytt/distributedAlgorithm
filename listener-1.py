# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 15:46:09 2022

@author: 86130
"""
import json
import socket
import time
import queue
import threading
import pickle
from _thread import *

import grpc

from block import *
from proto import a_pb2_grpc as blockchain_pb2_grpc
from proto import a_pb2 as blockchain_pb2

callCount=0
NODEHOST = 'localhost'
# HOST = '127.0.0.1' 
# NODEHOST = '127.0.0.1'

config={
        "host": "localhost",
        "port": 6379,
        "db": 2
    }
local_bc = Blockchain(config)
# nodeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     # Bind the socket
# nodeSocket.bind((HOST, PORT))
# nodeSocket.listen(5)
    
def connectToNodeServer(port):
    global callCount
    nodeServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect via the socket
    try:
        nodeServerSocket.connect((NODEHOST, port))
    except:
        print("Unable to connect to the blockchain service")
        print("Trying again...")
        callCount = callCount + 1
        if callCount > 2:
            return
        else:
            connectToNodeServer(port)
    
    # Connect via the socket
    
    data = nodeServerSocket.recv(1024)
    print("===listener1 receive block from port"+str(port)+"===")
    print(data.decode('UTF-8'))
    blocks=local_bc.blocks
    # last_hash=blocks.get("l").decode()
    block=eval(data.decode('UTF-8'))
    blocks.set(block["Hash"],json.dumps(block))
    blocks.set("l",block["Hash"])
    start_new_thread(listening, (nodeServerSocket,port))
    
 
def listening(nodeServerSocket,port):
    while True:
        data = nodeServerSocket.recv(1024)
        print("===listener1 receive block from port"+str(port)+"===")
        print(data.decode('UTF-8'))
        print("===listener1 receive block from port"+str(port)+"===")
        
        blocks=local_bc.blocks
        last_hash=blocks.get("l").decode()
        block=eval(data.decode('UTF-8'))
        blocks.set(block["Hash"],json.dumps(block))
        blocks.set("l",block["Hash"])
start_new_thread(connectToNodeServer,(12500,))
start_new_thread(connectToNodeServer,(12000,))


