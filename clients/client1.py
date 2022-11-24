from __future__ import print_function

import logging
import random
import time
import grpc
from proto import a_pb2 as blockchain_pb2
from proto import a_pb2_grpc as blockchain_pb2_grpc
from block import *
def new_block():
    print("generate new block")
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = blockchain_pb2_grpc.BlockChainStub(channel)
        response = stub.new_block(blockchain_pb2.new_block_request())
        print(response)
def new_genesis_block():
    print("generate new genesis block")
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = blockchain_pb2_grpc.BlockChainStub(channel)
        response=stub.new_genesis_block(blockchain_pb2.new_genesis_block_request())
        print(response)

def add_block():
    print("add the block to the blockchain!")

def query_blockchain():
    print("query blockchain")
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = blockchain_pb2_grpc.BlockChainStub(channel)
        print("before response")
        hello="hello"
        response = stub.query_blockchain(blockchain_pb2.query_blockchain_request(msg=hello))
        print("after response")
        print(response)
        print("====")
# blockchain_pb2.query_blockchain_request()
def new_a_block():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = blockchain_pb2_grpc.BlockChainStub(channel)
        response=stub.new_block(blockchain_pb2.new_block_request(prevblockhash="efb26dbb8165dab135f04a338e31b49cba2d590ef9f4fa90786fdfc8c709b645",index=1))
        print("==new_block response==")
        print(response)
        print("=========")
        
def broadcast():
    print("broadcast to other nodes")
def send_block():
    print("send block to other nodes")


        

if __name__ == '__main__':
    logging.basicConfig()
    
    # new_genesis_block()
    new_a_block()
