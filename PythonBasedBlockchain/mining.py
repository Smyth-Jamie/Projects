from hashlib import sha3_512 as HASH
import random as r
import time as t
import string

class Mine():
    def __init__(self, TRANSACTION_BLOCK):
        self.data = TRANSACTION_BLOCK
        self.Blockroot = []

    def __merkleroot(self):
        merklerootArray = []
        length = len(self.data)
        loopcount = 0
        while length > 1:
            if round(length / 2) != (length / 2):
                length += 1
            length = length / 2
            loopcount += 1
#            # print(length, loopcount) # This is removed to spare processing time for testing
        tempstore = []
        for x in self.data:
            tempstore.append(x)
#         # print('Tempstore', tempstore, '\n') # This is removed to spare processing time for testing
        for x in range(0, loopcount):
            temp = []
            if round(len(tempstore)/2) != len(tempstore)/2 and x < loopcount:
                tempstore.append(HASH(str(t.time()).encode()).hexdigest())
#             # print('Tempstore in range section', tempstore, '\n') # This is removed to spare processing time for testing
            for x in range(0, len(tempstore), 2):
                hashvalue = HASH(str(str(tempstore[x]) + '||' + str(tempstore[x+1])).encode()).hexdigest()
                temp.append(hashvalue)
#            # print('Temp', temp, '\n') # This is removed to spare processing time for testing
            tempstore.clear()
            for x in temp:
                tempstore.append(x)
            merklerootArray.insert(0, temp)
        print(merklerootArray)
        return merklerootArray

    def mine(self, previousBlock):
        start = t.time()
        sumDICT = {}
        merkle = Mine.__merkleroot(self)
        proof = 0
        hashsum = ' '
        while str(hashsum)[0] != '0':
            proof = ''.join(r.choice(string.ascii_letters) for i in range(0, round(r.random()*100)))
            hashsum = str(HASH(str(str(merkle[0]) + '|||' + str(proof) + '|||' + str(previousBlock['HashSum'])).encode()).hexdigest())
            # print('\nMerkle:', merkle[0], '\nCurrent Proof:', proof, '\nCurrent Hashsum: ', hashsum) # This is removed to spare processing time for testing
            t.sleep(0.5)
        end = t.time()
        sumDICT = {
            'HashSum': hashsum,
            'PreviousBlock': str(previousBlock['HashSum']),
            'MerkleRoot': str(merkle[0]),
            'Proof': proof,
            'Time': end-start,
            'Time Mined': t.time(),
            'MerkleTree': merkle, # Added as test
            'Transactions': self.data
        }
        '''
        for x in merkle[0:]:
            sumDICT['MerkleTree'].append(x)''' # Removed for testing
        return sumDICT