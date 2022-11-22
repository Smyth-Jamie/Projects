from hashlib import sha3_256 as HASH
import string
import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature

class Keys():
    def __init__(self, DATA):
        self.curve = ec.SECP256R1()
        self.signature_algorithm = ec.ECDSA(hashes.SHA3_256())
        self.priv_key = 0
        self.pub_key = 0
        if DATA != '':
            hashval = int('0x' + str(HASH(DATA.encode()).hexdigest()), 16)
            self.priv_key = ec.derive_private_key(hashval, self.curve, default_backend())
            self.pub_key = self.priv_key.public_key()
        else:
            hashval = int('0x' + str(HASH(str(''.join(random.choice(string.ascii_letters) for i in range(0, 1023))).encode())), 16)
            self.priv_key = ec.derive_private_key(hashval, self.curve, default_backend())
            self.pub_key = self.priv_key.public_key()

    def sign(self, data):
        return self.priv_key.sign(data.encode(), self.signature_algorithm)

    def verify(self, sig, data):
        try:
            info = [sig, data, self.pub_key.verify(sig, data.encode(), self.signature_algorithm), 'OK']
        except InvalidSignature:
            info = [sig, data, 'null', 'ERROR']
        return info