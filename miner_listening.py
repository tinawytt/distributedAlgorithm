from __future__ import print_function

import logging

import grpc
import blockchain_pb2
import blockchain_pb2_grpc

# The client request the QueryBlockchain to server, transferring the message by Block data structure
def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = blockchain_pb2_grpc.BlockChainStub(channel)
        blockchain = stub.QueryBlockchain(blockchain_pb2.QueryBlockchainRequest(message=''))
        print("Received Blockchain: ")
        print(blockchain.blocks)


if __name__ == '__main__':
    logging.basicConfig()
    run()
