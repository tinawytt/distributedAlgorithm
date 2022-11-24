import json
import time
from pow import Proof_of_work
from redis_db.redis_storage import Redis
class Block:
    def __init__(self,events,prevhash,index):
        self.block=dict()
#         self.TimeStamp=int(time.time())
#         self.Events=events
#         self.PrevBlockHash=prevhash
#         self.Index=index
#         self.Nonce=0
#         self.Difficulty=8
#         self.Hash
class Blockchain:
    def __init__(self,config=None):
        self.blocks=Redis(config)
        # genesis_block=new_genesis_block()
        # self.blocks.append(genesis_block)

def new_block(event,prevhash,index):
    block = {
        "TimeStamp":str(int(time.time())),#
        "Events": event,
        "PrevBlockHash": prevhash,
        "Index": index,
        "Nonce": 0,
        "Difficulty": 8
    }
    # block=Block(event,prevhash,index)
    # print(block["TimeStamp"])
    pow=Proof_of_work(block)
    nonce,hash=pow.mine(block)
    block["Hash"]=hash
    block["Nonce"]=nonce
    # block.Hash=hash
    # block.Nonce=nonce

    return block
def new_genesis_block():
    # new a genesis block and add it into blockchain directly
    genesis_block=new_block("","",0)
    blocks = Blockchain().blocks
    print("=====")
    print(genesis_block)
    print("=====")
    print(str(genesis_block))
    blocks.set(genesis_block["Hash"], str(genesis_block))
    blocks.set("l", genesis_block["Hash"])
    return genesis_block

def add_block(block):
    flag=0
    blocks=Blockchain().blocks
    # if len(get_blockchain("hi"))==0:
    #     # blocks.append(block)
    #     print(block)
    last_hash=blocks.get("l").decode()
    # print(blocks.get(last_hash))
    # print("enter add a block")
    # if block["PrevBlockHash"]==last_hash:
    #     flag+=1
    #     print("satisfy1")
    # print(type(blocks.get(last_hash)))
    # print(blocks.get(last_hash))
    
    # print(str(blocks.get(last_hash))[2:-1])
    # print(json.loads("\""+str(blocks.get(last_hash))[2:-1])+"\"")
    # if block["TimeStamp"]>json.loads("\""+str(blocks.get(last_hash))[2:-1]+"\"")["TimeStamp"]:
    #     flag+=1
    #     print("satisfy2")
    # if int(block['Hash'],16)<2**(256-block["Difficulty"]):
    #     flag+=1
    #     print("satisfy3")
    # if flag==3:

        # blocks.append(block)
        # print("===add block function==")
        # print(block.decode())
    blocks.set(block["Hash"],str(block))
    blocks.set("l",block["Hash"])
    # else:
    #     print("block is not valid!")
def add_block2(block):
    flag=0
    blocks=Blockchain().blocks
    if len(get_blockchain("hi"))==0:
        # blocks.append(block)
        print("======")
        
        
        blocks.set(eval(block)["Hash"], block)
        blocks.set("l", eval(block)["Hash"])
    else:
        last_hash=blocks.get("l")
        # print(blocks.get(last_hash))
        if eval(block)["PrevBlockHash"]==blocks.get(last_hash):
            flag+=1
        if eval(block)["TimeStamp"]<eval(blocks.get(last_hash))["TimeStamp"] and block["TimeStamp"]>time.time():
            flag+=1
        if int(eval(block)['Hash'],16)<2**(256-eval(block)["Difficulty"]):
            flag+=1
        if flag==3:

            blocks.append(eval(block))
            print(eval(block).decode())
            blocks.set(block.Hash,eval(block).decode())
            blocks.set("l",eval(block).Hash)
        else:
            print("block is not valid!")
def get_block_by_index(blocks,index):
    for i in blocks:
        if i.Index==index:
            return i
    return False
def get_blockchain(string):
    blocks = []
    storage=Blockchain().blocks
    for b in storage.keys():
        # 把’l‘的键值对 去掉
        if b.decode() != 'l':
            v = storage.get(b.decode())
            blocks.append(v)
    # print(blocks['Index'])
    # 对blocks 排序，按照index 从小到大
    # blocks.sort(key=lambda x: x['Index'], reverse=False)
    # blocks=sorted(blocks,key= blocks["Index"], reverse=False)
    return blocks

