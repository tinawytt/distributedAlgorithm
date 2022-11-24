# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 16:11:29 2022

@author: 86130
"""
import socket
import time
import queue
import threading
from _thread import *
import pickle
# from core.blockchain.blockchain import BlockChain
# from core.transactions.transaction import new_coinbase_tx
# from core.blockchain.block import new_genesis_block
from block import *
import json
# Constants
# HOST = '127.0.0.1' 
# HOST = '192.168.100.18'
HOST = 'localhost'
PORT = 12500
NUMBER_OF_THREADS = 1

# Global Variables
nodeSocket = None
clientConnections = []
clientAddresses = []
local_bc = Blockchain()
# coinbase = new_coinbase_tx("7AgP8z7XYyZ2sdnVJ6HCiE5X2reJDf")
genesis_block = new_genesis_block()
add_block(genesis_block)



def serveBlockChain():
    global nodeSocket
    global clientConnections
    global clientAddresses

    # Create a socket
    nodeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket
    nodeSocket.bind((HOST, PORT))

    nodeSocket.listen(5)
    print("Listening to port " + str(PORT))

    while(True):
        try:
            clientConnection, clientAddress = nodeSocket.accept()
            print(clientConnection)
            clientConnections.append(clientConnection)
            clientAddresses.append(clientAddress)
            print(str(clientAddress[0]) + " just connected")

            # broadcast genesis block to all
            #todo
            last_hash = local_bc.blocks.get("l").decode()
            last_block = local_bc.blocks.get(last_hash)
            clientConnection.sendall(last_block)
            start_new_thread(server_receive_block_and_send, (clientConnection, clientAddress))
        except Exception as e:
            print("Error in accepting connections" + e)
def is_type_block(block):
    res=True
    index=block.get("Index")
    if(index == None):
        res=False
    transaction=block.get("Transactions")
    if(transaction == None):
        res=False
    prev_hash=block.get("PrevBlockHash")
    if(prev_hash == None):
        res=False
    difficulty=block.get("Difficulty")
    if(difficulty == None):
        res=False
    return res
    
def server_receive_block_and_send(clientConnection, clientAddress):
    global local_bc
    while True:
        data = clientConnection.recv(1024)
        print("===server receive a block===")
        
        print(eval(data.decode('UTF-8')))
        print("===server receive a block===")
        blocks=local_bc.blocks
        last_hash=blocks.get("l").decode()
        block=eval(data.decode('UTF-8'))
        blocks.set(block["Hash"],json.dumps(block))
        blocks.set("l",block["Hash"])
        print("server successful add 1 block to its chain")
        # if is_type_block(eval(data.decode('UTF-8'))) and bc.validate_block(eval(data.decode('UTF-8'))):
        #    bc.add_block(eval(data.decode('UTF-8')))
        for conn in clientConnections:
            conn.sendall(bytes('{}'.format(block),'utf-8'))
serveBlockChain()