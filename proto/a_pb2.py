# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: a.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x07\x61.proto\"\x1b\n\x19new_genesis_block_request\";\n\x1anew_genesis_block_response\x12\x1d\n\rgenesis_block\x18\x01 \x01(\x0b\x32\x06.Block\"\xa1\x02\n\x05\x45vent\x12\x12\n\nevent_type\x18\x01 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\x12\x0f\n\x07\x65ventNo\x18\x03 \x01(\t\x12\x12\n\nneed_index\x18\x04 \x01(\t\x12\x1c\n\x14\x64onator_bank_account\x18\x05 \x01(\t\x12\x1c\n\x14\x64onatee_bank_account\x18\x06 \x01(\t\x12\x14\n\x0c\x64onatee_name\x18\x07 \x01(\t\x12\x14\n\x0c\x64onatee_idNo\x18\x08 \x01(\t\x12\x18\n\x10key_income_proof\x18\t \x01(\t\x12\x1a\n\x12key_medical_record\x18\n \x01(\t\x12\x1c\n\x14key_hospital_payment\x18\x0b \x01(\t\x12\x13\n\x0bisConfirmed\x18\x0c \x01(\x08\"9\n\x11new_block_request\x12\x15\n\rprevblockhash\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\x05\"+\n\x12new_block_response\x12\x15\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x06.Block\"\'\n\x18query_blockchain_request\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\x90\x01\n\x05\x42lock\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x11\n\ttimestamp\x18\x02 \x01(\t\x12\x16\n\x06\x65vents\x18\x03 \x03(\x0b\x32\x06.Event\x12\x15\n\rPrevBlockHash\x18\x04 \x01(\t\x12\r\n\x05Nonce\x18\x05 \x01(\x05\x12\x13\n\x0b\x43urrentHash\x18\x06 \x01(\t\x12\x12\n\ndifficulty\x18\x07 \x01(\x05\"3\n\x19query_blockchain_response\x12\x16\n\x06\x62locks\x18\x01 \x03(\x0b\x32\x06.Block\"\x9c\x02\n\x11StartEventRequest\x12\x12\n\nevent_type\x18\x01 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\x12\x12\n\nneed_index\x18\x03 \x01(\t\x12\x1c\n\x14\x64onator_bank_account\x18\x04 \x01(\t\x12\x1c\n\x14\x64onatee_bank_account\x18\x05 \x01(\t\x12\x14\n\x0c\x64onatee_name\x18\x06 \x01(\t\x12\x14\n\x0c\x64onatee_idNo\x18\x07 \x01(\t\x12\x18\n\x10key_income_proof\x18\x08 \x01(\t\x12\x1a\n\x12key_medical_record\x18\t \x01(\t\x12\x1c\n\x14key_hospital_payment\x18\n \x01(\t\x12\x13\n\x0bisConfirmed\x18\x0b \x01(\x08\"%\n\x12StartEventResponse\x12\x0f\n\x07\x65ventNo\x18\x01 \x01(\t2\x99\x02\n\nBlockChain\x12M\n\x11new_genesis_block\x12\x1a.new_genesis_block_request\x1a\x1a.new_genesis_block_request\"\x00\x12\x36\n\tnew_block\x12\x12.new_block_request\x1a\x13.new_block_response\"\x00\x12K\n\x10query_blockchain\x12\x19.query_blockchain_request\x1a\x1a.query_blockchain_response\"\x00\x12\x37\n\nStartEvent\x12\x12.StartEventRequest\x1a\x13.StartEventResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'a_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NEW_GENESIS_BLOCK_REQUEST._serialized_start=11
  _NEW_GENESIS_BLOCK_REQUEST._serialized_end=38
  _NEW_GENESIS_BLOCK_RESPONSE._serialized_start=40
  _NEW_GENESIS_BLOCK_RESPONSE._serialized_end=99
  _EVENT._serialized_start=102
  _EVENT._serialized_end=391
  _NEW_BLOCK_REQUEST._serialized_start=393
  _NEW_BLOCK_REQUEST._serialized_end=450
  _NEW_BLOCK_RESPONSE._serialized_start=452
  _NEW_BLOCK_RESPONSE._serialized_end=495
  _QUERY_BLOCKCHAIN_REQUEST._serialized_start=497
  _QUERY_BLOCKCHAIN_REQUEST._serialized_end=536
  _BLOCK._serialized_start=539
  _BLOCK._serialized_end=683
  _QUERY_BLOCKCHAIN_RESPONSE._serialized_start=685
  _QUERY_BLOCKCHAIN_RESPONSE._serialized_end=736
  _STARTEVENTREQUEST._serialized_start=739
  _STARTEVENTREQUEST._serialized_end=1023
  _STARTEVENTRESPONSE._serialized_start=1025
  _STARTEVENTRESPONSE._serialized_end=1062
  _BLOCKCHAIN._serialized_start=1065
  _BLOCKCHAIN._serialized_end=1346
# @@protoc_insertion_point(module_scope)
