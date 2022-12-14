from concurrent import futures
import logging
import grpc
import proto.a_pb2 as blockchain_pb2
import proto.a_pb2_grpc as blockchain_pb2_grpc
from bc_definition import *
from block import *
import json
# We implement the function at server class
class BlockchainServer(blockchain_pb2_grpc.BlockChainServicer):
    # When the server created, a new blockchain will be created too
    def __init__(self):
        self.blockchain = Blockchain()
        self.waiting_events=[]
        self.confirmed_events=[]
    def new_genesis_block(self, request, response):
        genesis_block = new_genesis_block()
        pb_genesis_block = blockchain_pb2.Block(index=genesis_block["Index"],
                                                timestamp=genesis_block["TimeStamp"],
                                                events=genesis_block["Events"],
                                                PrevBlockHash=genesis_block["PrevBlockHash"],
                                                Nonce=genesis_block["Nonce"],
                                                CurrentHash=genesis_block["Hash"],
                                                difficulty=genesis_block["Difficulty"])
        print(pb_genesis_block)
        response = blockchain_pb2.new_genesis_block_response(genesis_block=pb_genesis_block)
        return response
    def new_genesis_block2(self,request,response):
        genesis_block=new_genesis_block()
        pb_genesis_block=blockchain_pb2.Block(index=genesis_block["Index"],timestamp=genesis_block["TimeStamp"],events=genesis_block["Events"],PrevBlockHash=genesis_block["PrevBlockHash"],Nonce=genesis_block["Nonce"],CurrentHash=genesis_block["Hash"],difficulty=genesis_block["Difficulty"])
        response=blockchain_pb2.new_genesis_block_response(genesis_block=pb_genesis_block)
        return response
    def query_blockchain(self, request, context):
        
        blocks=[]
        for i in range(len(get_blockchain(request.msg))):
            print(get_blockchain(request.msg)[i])
            
            str1=str(get_blockchain(request.msg)[i])[2:-1]
            print(str1)
            str2=str1.replace('\'','\"')
            str3=str2.replace('<','\"<')
            str4=str3.replace('>','>\"')
            print(str4)
            blocks.append(str4)
            
            
            
        response = blockchain_pb2.q_blockchain_response(blocks=blocks)
        return response
    def new_block(self,request,response):
        if(len(self.confirmed_events)>0):
            nblock=new_block(self.confirmed_events,request.prevblockhash,request.index)
            
            pb_events=[]
            for e in self.confirmed_events:
                pb_event=blockchain_pb2.Event(event_type=e.event_type,amount=e.amount,
                                     eventNo=e.eventNo,need_index=e.need_index,
                                     donator_bank_account=e.donator_bank_account,
                                     donatee_bank_account=e.donatee_bank_account,
                                     donatee_name=e.donatee_name,donatee_idNo=e.donatee_idNo,
                                     key_income_proof=e.key_income_proof,key_medical_record=e.key_medical_record,
                                     key_hospital_payment=e.key_hospital_payment,isConfirmed=e.isConfirmed)
                pb_events.append(pb_event)
            
            pb_new_block=blockchain_pb2.Block(index=nblock["Index"],timestamp=nblock["TimeStamp"],#nblock["TimeStamp"].to_bytes(4, 'big')
                             events=pb_events,PrevBlockHash=nblock["PrevBlockHash"],
                             Nonce=nblock["Nonce"],CurrentHash=nblock["Hash"],
                             difficulty=nblock["Difficulty"])
            response = blockchain_pb2.new_block_response(block=pb_new_block)
            add_block(nblock)
            self.confirmed_events=[]
        return response
    def StartEvent(self, request, context):
        
        if(request.event_type==1):
            eventNo,event2=add_event(self.confirmed_events,request.event_type, request.amount,
                          request.donatee_name,need_index=request.need_index,
                          donator_bank_account=request.donator_bank_account,
                          donatee_bank_account=request.donatee_bank_account)
            
        elif request.event_type==2:
            #????????????????????????????????????????????????????????????????????????miner????????????Block
            eventNo,event2=add_event(self.waiting_events,request.event_type, request.amount,
                          request.donatee_name,
                          donatee_bank_account=request.donatee_bank_account,
                          donatee_idNo=request.donatee_idNo,
                          key_income_proof=request.key_income_proof,
                          key_medical_record=request.key_medical_record,
                          key_hospital_payment=request.key_hospital_payment)
            
        else:
            eventNo,event2=add_event(self.confirmed_events,request.event_type, request.amount,
                          request.donatee_name,need_index=request.need_index,
                          isConfirmed=True)
        #?????????event??????????????????localTxList
        #???miner????????????Block
        print("===waiting list===")
        for event in self.waiting_events:
            print(event.toString())
        print("=========")
        print("===confirmed events===")
        for event in self.confirmed_events:
            print(event.toString())
        print("=========")
        response=blockchain_pb2.StartEventResponse(eventNo=eventNo)
        return response

# server setting
def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    blockchain_pb2_grpc.add_BlockChainServicer_to_server(BlockchainServer(), server)
    server.add_insecure_port('127.0.0.1:' + port)
    server.start()
    print("blockchain-demo started, listening on " + port)
    server.wait_for_termination()


# run the server
if __name__ == '__main__':
    logging.basicConfig()
    serve()
