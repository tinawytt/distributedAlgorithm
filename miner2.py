from __future__ import print_function

import logging
import random
import time
import grpc
import blockchain_pb2
import blockchain_pb2_grpc

# The client request the AddBlock to server
def run():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = blockchain_pb2_grpc.BlockChainStub(channel)
        tran_msg = "This block was added by client 2."
        expect_hash = random.randint(0,9)
        response = stub.AddBlock(blockchain_pb2.AddBlockRequest(transaction=tran_msg, expectHash=expect_hash))
        while 1 == 1:
            time.sleep(1)
            expect_hash = random.randint(0,9)
            print("Mining the next Block, Guessing the expected puzzle hash is " + str(expect_hash))
            response = stub.AddBlock(blockchain_pb2.AddBlockRequest(transaction=tran_msg, expectHash=expect_hash))
            if response.hash != 'False':
                print("Add the block successfully. The target puzzle Hash is " + str(expect_hash))
                print(" Received block address: " + response.hash)


if __name__ == '__main__':
    logging.basicConfig()
    run()
