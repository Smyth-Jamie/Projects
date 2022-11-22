from Blockchain import Blockchain, Transaction, Serialize
from KeyGeneration import Keys
import random
import string

B = Blockchain("newBlockchain.dat")
while(int(input('|| 1 || Create transactions in pool || \n|| 2 || Exit transaction creation ||\n')) != 2):
    for x in range(0, int(input('Input an Integer Value: '))):
        sender = Keys(''.join(random.choice(string.ascii_letters) for i in range(0, 1023)))
        receiver = Keys(''.join(random.choice(string.ascii_letters) for i in range(0, 1023)))
        contract = ''.join(random.choice(string.ascii_letters) for i in range(0, 52))
        T = Transaction(sender.pub_key.public_bytes(Serialize.Encoding.X962, Serialize.PublicFormat.UncompressedPoint).hex(), sender.sign(str(sender.pub_key)), receiver.pub_key.public_bytes(Serialize.Encoding.X962, Serialize.PublicFormat.UncompressedPoint).hex(), contract, random.random())
        T.createTransaction()
        B.addTransaction(T.placeTransaction())

    B.mine()

while True:
    selection = int(input('Choose search option:\n 1: Browse Ledger\n 2: print Ledger\n 3: Explore Blockchain\n 4: Export all blockchain data to txt file\n'))
    if selection == 1:
        print(B.ledgerSearch(str(input('Enter the required address: '))))
    elif selection == 2:
        print(B.ledgerData())
    elif selection == 3:
        print(B.BlockchainSearch(int(input('Enter the required block index: '))))
    elif selection == 4:
        txtfile = open('BlockchainData.txt', "w")
        writingString = ''
        for x in range(len(B.Blockchain)):
            writingString += '\n \n Block ' + str(x) + ': \n' +  B.BlockchainSearch(x)
        txtfile.write(writingString)
        txtfile.close()

