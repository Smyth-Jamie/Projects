from hashlib import sha3_512 as HASH
from uuid import uuid4

class Transaction():
    __transactionSTRUCT = {}
    def __init__(self, FROM, SIG, TO, CONTRACT, QUANTITY):
        self.sender = FROM
        self.signature = SIG
        self.receiver = TO
        self.contract = CONTRACT
        self.quantity = QUANTITY

    def createTransaction(self):
        Transaction.__transactionSTRUCT = {
            'Transaction ID': HASH(str(uuid4()).encode()).hexdigest(),
            'Sender': self.sender,
            'Signature': self.signature,
            'Receiver': self.receiver,
            'Contract': self.contract,
            'Quantity': self.quantity
        }
        return True

    def readTransaction(self):
        print(Transaction.__transactionSTRUCT)

    def placeTransaction(self):
        return Transaction.__transactionSTRUCT