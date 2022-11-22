import pickle
import os

class DL():
    def __init__(self, ledgerLocation):
        self.ledgerLocation = ledgerLocation
        tempfile = open(self.ledgerLocation, 'a')
        filesize = os.path.getsize(self.ledgerLocation)
        if filesize == 0:
            self.ledger = {}
            pickle.dump(self.ledger, open(self.ledgerLocation, 'wb'))
        else:
            self.ledger = pickle.load(open(self.ledgerLocation, 'rb'))
    
    def updateLedger(self, data):
        for record in data:
            senderData = {}
            receiverData = {}
            sender = str(record[0])
            receiver = str(record[1])
            quantity = float(record[2])
            senderData['Public Key'] = sender
            receiverData['Public Key'] = receiver
            if sender not in self.ledger.keys():
                senderData['Quantity'] = 0 - quantity
            else:
                senderData['Quantity'] = self.ledger[sender]['Quantity'] - quantity
            if receiver not in self.ledger.keys():
                receiverData['Quantity'] = 0 + quantity
            else:
                receiverData['Quantity'] = self.ledger[receiver]['Quantity'] + quantity

            self.ledger[sender] = senderData
            self.ledger[receiver] = receiverData
    
    def confirmUpdate(self):
        pickle.dump(self.ledger, open(self.ledgerLocation, 'wb'))

    def getLedger(self):
        return self.ledger