# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:05:17 2022

@author: 86130
"""
import grpc
# import blockchain_pb2
# import blockchain_pb2_grpc
import proto.a_pb2 as blockchain_pb2
import proto.a_pb2_grpc as blockchain_pb2_grpc
from bitstring import BitArray
# The client request the AddBlock to server
def start_event():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = blockchain_pb2_grpc.BlockChainStub(channel)
        key_income_proof=""
        key_medical_record=""
        key_hospital_payment=""
        
        # response = stub.StartEvent(blockchain_pb2.StartEventRequest(
        #     # dict1
        # event_type=2,amount=100,need_index="",donator_bank_account="",
        # donatee_bank_account="123456",donatee_name="xiaoming",
        # donatee_idNo="1111",key_income_proof=key_income_proof,
        # key_medical_record=key_medical_record,
        # key_hospital_payment=key_hospital_payment,isConfirmed=False
        # ))
        # print(response.eventNo)
        response = stub.StartEvent(blockchain_pb2.StartEventRequest(
            # dict1
        event_type=1,amount=1000,need_index="N99999999",donator_bank_account="5678",
        donatee_bank_account="123456",donatee_name="xiaoming",
        donatee_idNo="",key_income_proof=key_income_proof,
        key_medical_record=key_medical_record,
        key_hospital_payment=key_hospital_payment,isConfirmed=False
        ))
        print(response.eventNo)
        response = stub.StartEvent(blockchain_pb2.StartEventRequest(
        event_type=3,amount=1000,need_index="N99999998",donator_bank_account="",
        donatee_bank_account="",donatee_name="xiaoming",
        donatee_idNo="",key_income_proof=key_income_proof,
        key_medical_record=key_medical_record,
        key_hospital_payment=key_hospital_payment,isConfirmed=True
        ))
        print(response.eventNo)
        

if __name__ == '__main__':
    start_event()
    # temp = format(123, "b")
    # print(type(temp))
    # b = BitArray(bin=temp)
    # print(b.uint)
