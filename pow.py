import hashlib
import time

# the upper bound of all potential nonces
MAX_NONCE = 20

class Proof_of_work:
    def __init__(self,block):
        self.block=block
    # perform PoW in a iteration manner
    def mine(self,block):
        # calculate the difficulty target from difficulty bits
        target = 2 ** (256 - self.block["Difficulty"])
        print("start mining……")
        # perform the iteration, until finding a nonce which satisfies the target
        start_time=time.time()
        for nonce in range(MAX_NONCE):
            # print(nonce)
            data=str(block["TimeStamp"]) + str(block["PrevBlockHash"])+str(block["Events"])+str(nonce)+str(block["Difficulty"])+str(block['Index'])
            hash_res = hashlib.sha256(
                data.encode('utf-8')).hexdigest()
            # hash_res=hashlib.sha256(
            #     hash.encode('utf-8')).hexdigest()
            # print(int(hash_res, 16))
            # print(target)
            # print()
            if int(hash_res, 16) < target:
                end_time=time.time()
                elapse_time=end_time-start_time
                print(f'success with nonce {nonce}\n')
                print(f'block hash is:\t\t {hash_res}')
                # print("hash_rate: "+nonce/elapse_time)
                return nonce,hash_res
        # target cannot be satisfied even all nonces are traversed

        print(f'failed after {MAX_NONCE} tries\n')
        return MAX_NONCE,hash_res

    def validate(self,nonce):
        target = 2 ** (256 - self.block['Difficulty'])
        data = str(self.block['TimeStamp']) + str(
            self.block['PrevBlockHash']) + \
               str(self.block["Events"])
        str(nonce) + str(self.block['Difficulty']) + str(self.block['Index'])
        hash_res = hashlib.sha256(
            data.encode('utf-8')).hexdigest()
        if hash_res >= target:
            return False
        if self.block["TimeStamp"] > int(time.time()):
            return False
        return True
