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

HOST = 'localhost'

# HOST = '127.0.0.1' 
NODEHOST = '127.0.0.1'
PORT = 12000
callCount =0
NODEPORT=12500
nodeServerSocket = None
config={
        "host": "localhost",
        "port": 6379,
        "db": 1
    }
local_bc = Blockchain(config)

minerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
minerSocket.bind((HOST, 12000))
minerSocket.listen(5)
clientConnections = []
clientAddresses = []

def connectToNodeServer():
    global nodeServerSocket
    global callCount
    nodeServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect via the socket
    try:
        nodeServerSocket.connect((HOST, NODEPORT))
    except:
        print("Unable to connect to the blockchain service")
        print("Trying again...")
        callCount = callCount + 1
        if callCount > 2:
            return
        else:
            connectToNodeServer()
    
    # Connect via the socket
    
    data = nodeServerSocket.recv(1024)
    print("===miner receive initial block===")
    print(data.decode('UTF-8'))
    print("===miner receive initial block===")
    blocks=local_bc.blocks
    # last_hash=blocks.get("l").decode()
    block=eval(data.decode('UTF-8'))
    blocks.set(block["Hash"],json.dumps(block))
    blocks.set("l",block["Hash"])
    
    
def mine():
    start_new_thread(listening, ())
    start_new_thread(acceptconnection, ())
    while True:
        # def new_a_block(prevhash, i):
        #     with grpc.insecure_channel('127.0.0.1:50051') as channel:
        #         stub = blockchain_pb2_grpc.BlockChainStub(channel)
        #         print(prevhash)
        #         response = stub.new_block(
        #             blockchain_pb2.new_block_request(prevblockhash=prevhash,
        #                                              index=i))
        #         print("==new_block response==")
        #         print(response)
        #         print("=========")
        
        str1=str(get_blockchain("last")[-1])[2:-1]
        # print(str1)
        str2=str1.replace('\'','\"')
        str3=str2.replace('<','\"<')
        str4=str3.replace('>','>\"')
        # print(str4)
        dict1=json.loads(str4)
        # last_hash=get_blockchain("last")[-1]["PrevBlockHash"]
        # index=get_blockchain("last")[-1]["Index"]
        # print(dict1)
        # print(type(dict1))
        # print(dict1["PrevBlockHash"])
        last_hash="0058dbe54e14e6da79dcf48ab6548fcb571050b879178566818fbd67e7598394"
        index=dict1["Index"]
        # mined_block= local_bc.new_block("",last_hash,)
        # mined_block=new_a_block("0058dbe54e14e6da79dcf48ab6548fcb571050b879178566818fbd67e7598394",index+1)
        mined_block=new_block("",last_hash,index)
        
        bytes_mined_block= bytes('{}'.format(mined_block),'utf-8')
        # bytes_mined_block = json.dumps(mined_block).encode()
        # for conn in clientConnections:
        #     conn.sendall(bytes_mined_block)
        nodeServerSocket.sendall(bytes_mined_block)
        time.sleep(10)
        print("====miner sent a block to nodeServer====")
        print(mined_block)
        print("====miner sent a block to nodeServer====")
        
def listening():
    while True:
        print("enter")
        data = nodeServerSocket.recv(1024)
        print("===miner receive a block===")
        print(data.decode('UTF-8'))
        print("===miner receive a block===")
        
        blocks=local_bc.blocks
        last_hash=blocks.get("l").decode()
        block=eval(data.decode('UTF-8'))
        blocks.set(block["Hash"],json.dumps(block))
        blocks.set("l",block["Hash"])
        for conn in clientConnections:
            conn.sendall(bytes('{}'.format(block),'utf-8'))
        print("===miner update and broadcast====")
        print(block)
        print("===miner update and broadcast====")
def acceptconnection():
    while True:
        clientConnection, clientAddress = minerSocket.accept()
        clientConnections.append(clientConnection)
        clientAddresses.append(clientAddress)
        print(str(clientAddress[0]) + " just connected")
        
connectToNodeServer()
mine()
