import os
import pickle
from mining import Mine
from DistributedLedger import DL
from transaction import Transaction
from cryptography.hazmat.primitives import serialization as Serialize

class Blockchain():
    def __init__(self, ChainName):
        self.ledgerOBJ = DL('Ledger.dat')
        self.ledger = self.ledgerOBJ.getLedger()
        self.transactionPool = []
        self.Blockchain = []
        self.chain = ChainName
        tempfile = open(self.chain, 'a')
        filesize = os.path.getsize(self.chain)
        tempfile.close()
        if filesize == 0:
            genesis = {
                'HashSum': '0xce2dyz',
                'Transactions': ['A simple Python Blockchain']
            }
            self.Blockchain.append(genesis)
            pickle.dump(self.Blockchain, open(self.chain, 'wb'))
        else:
            self.Blockchain = pickle.load(open(self.chain, 'rb'))


    def addTransaction(self, transactionData):
        T = Transaction(transactionData['Sender'], transactionData['Signature'], transactionData['Receiver'], transactionData['Contract'], transactionData['Quantity'])
        T.createTransaction()
        self.transactionPool.append(T.placeTransaction())

    def mine(self):
        M = Mine(self.transactionPool[:5000])
        if len(self.Blockchain) == 1:
            data = M.mine(self.Blockchain[0])
        elif len(self.Blockchain) < 1:
            data = 'NULL'
        else:
            data = M.mine(self.Blockchain[len(self.Blockchain)-1]) ##### ERROR Resolved 30/10/2022 -1 was -2, resulted in wrong hashsum for whole chain
        if data != 'NULL':
            ledgerArray = []
            for section in data:
                if section == 'Transactions':
                    for transaction in data[section]:
                        transactionData = [transaction['Sender'], transaction['Receiver'], transaction['Quantity']]
                        ledgerArray.append(transactionData)
            self.Blockchain.append(data)
            self.transactionPool[5000:].clear()
            self.ledgerOBJ.updateLedger(ledgerArray)
            self.ledgerOBJ.confirmUpdate()
            self.ledger = self.ledgerOBJ.getLedger()
            pickle.dump(self.Blockchain, open(self.chain, 'wb'))

    def ledgerData(self):
        dataString = ''
        for record in self.ledger:
            dataString += '{\n' 
            dataString += ' ' 
            dataString += self.ledger[record]['Public Key']
            dataString += ' ' 
            dataString += str(self.ledger[record]['Quantity'])
            dataString += '\n}\n'
        return dataString

    def ledgerSearch(self, address):
        data = self.ledger[address]
        string = '{\n'
        for key in data:
            string += ' ' + str(key) +' ' + str(data[key]) + '\n'
        string += '}\n'
        return string

    def getBlockData(self, block, genesis):
        string = ''
        for section in block:
            if section == 'Transactions' and genesis == False:
                string += ' ' + str(section)
                for transaction in block[section]:
                    string += '\n' + ' ' + ' ' + '{\n'
                    for division in transaction:
                        string += ' ' + ' ' + ' ' + str(division) + ' ' + str(transaction[division]) + '\n'
                string += ' ' + ' ' + '}\n'
            elif genesis is None or genesis == True:
                string += ' ' + str(section) + ' ' + str(block[section]) + '\n'
            elif section == 'MerkleTree':
                string += ' ' + str(section)
                string += '\n  {'
                for branch in block[section]:
                        string += '\n   ' + str(branch)
                string += '\n  }\n'
            else:
                string += ' ' + str(section) + ' ' + str(block[section]) + '\n'

        return string

    def BlockchainSearch(self, block_INDEX):
        blockchain = pickle.load(open(self.chain, 'rb'))
        boolean = False
        if block_INDEX == 0:
            boolean = True
        return Blockchain.getBlockData(self, block=blockchain[block_INDEX], genesis=boolean)