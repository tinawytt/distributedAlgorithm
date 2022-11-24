import hashlib
import random
import string


# This file used to define the blockchain structure

# A block must include hash code (address), previous block's hash code, and the transaction context

class Event:
    def __init__(self,event_type,amount,eventNo,need_index,donator_bank_account,
                 donatee_bank_account,donatee_name,
              donatee_idNo,key_income_proof,key_medical_record,
              key_hospital_payment,isConfirmed):
        self.event_type=event_type
        self.amount=amount
        self.eventNo=eventNo
        self.need_index=need_index
        self.donator_bank_account=donator_bank_account
        self.donatee_bank_account=donatee_bank_account
        self.donatee_name=donatee_name
        self.donatee_idNo=donatee_idNo
        #这三个key还没tostring
        self.key_income_proof=key_income_proof
        self.key_medical_record=key_medical_record
        self.key_hospital_payment=key_hospital_payment
        self.isConfirmed=isConfirmed
    def toString(self):
        return "{"+"event_type:"+str(self.event_type)+","+"amount:"+str(self.amount)+",eventNo:"+self.eventNo+",need_index:"+str(self.need_index)+",donator_bank_account:"+str(self.donator_bank_account)+",donatee_bank_account:"+str(self.donatee_bank_account)+",donatee_name:"+str(self.donatee_name)+",donatee_idNo:"+str(self.donatee_idNo)+",isConfirmed:"+str(self.isConfirmed)+"}"
def add_event(events,event_type,amount,donatee_name,need_index="",
              donator_bank_account="",donatee_bank_account="",
              donatee_idNo="",key_income_proof="",key_medical_record="",
              key_hospital_payment="",isConfirmed=False):
    value = ''.join(random.sample(string.digits, 8))
    if(event_type==1):
        
        eventNo="D"+value
    elif event_type==2:
        eventNo="N"+value
        
    else:
        eventNo="C"+value
    event=Event(event_type,amount,eventNo,need_index,
              donator_bank_account,donatee_bank_account,donatee_name,
              donatee_idNo,key_income_proof,key_medical_record,
              key_hospital_payment,isConfirmed)
    events.append(event)
    return eventNo,event