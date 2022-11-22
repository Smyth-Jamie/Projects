from hashlib import sha3_256
import KeyGeneration as KG
from Blockchain import Serialize
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from secrets import token_bytes
import codecs

Bob_keys = KG.Keys(str(sha3_256(b'HelloWorld!')))

Alice_keys = KG.Keys(str(sha3_256(b'GoodbyeWorld!')))


Bob_pub_key = Bob_keys.pub_key.public_bytes(Serialize.Encoding.OpenSSH, Serialize.PublicFormat.OpenSSH)
Bob_priv_key = Bob_keys.priv_key.private_bytes(Serialize.Encoding.PEM, Serialize.PrivateFormat.TraditionalOpenSSL, Serialize.NoEncryption())

Alice_pub_key = Alice_keys.pub_key.public_bytes(Serialize.Encoding.OpenSSH, Serialize.PublicFormat.OpenSSH)
Alice_priv_key = Alice_keys.priv_key.private_bytes(Serialize.Encoding.PEM, Serialize.PrivateFormat.TraditionalOpenSSL, Serialize.NoEncryption())

Bob_shared_key = Bob_keys.priv_key.exchange(ec.ECDH(), Alice_keys.pub_key)
Alice_shared_key = Alice_keys.priv_key.exchange(ec.ECDH(), Bob_keys.pub_key)

Bob_derived_key = HKDF(algorithm=hashes.SHA3_256(), length=32, salt=None, info=b'').derive(Alice_shared_key)
Alice_derived_key = HKDF(algorithm=hashes.SHA3_256(), length=32, salt=None, info=b'').derive(Bob_shared_key)

print('Bob private key: ', codecs.encode(codecs.decode(Bob_priv_key.hex(), 'hex'), 'base64').decode(), '\nBob public key: ', codecs.encode(codecs.decode(Bob_pub_key.hex(), 'hex'), 'base64').decode())
print('Alice private key: ', codecs.encode(codecs.decode(Alice_priv_key.hex(), 'hex'), 'base64').decode(), '\nAlice public key: ', codecs.encode(codecs.decode(Alice_pub_key.hex(), 'hex'), 'base64').decode())

print('\n')

print('Bobs derived key: ', Bob_derived_key.hex(), '\nAlices derived key: ', Alice_derived_key.hex())

def encrypt(derived_key, msg, bytes):
    aes = Cipher(algorithms.AES(derived_key), modes.CBC(bytes), backend=default_backend())
    encryptor = aes.encryptor()

    padder = padding.PKCS7(128).padder()
    padder_data = padder.update(msg.encode()) + padder.finalize()
    return encryptor.update(padder_data) + encryptor.finalize()

def decrypt(derived_key, encrypted_msg, bytes):
    aes = Cipher(algorithms.AES(derived_key), modes.CBC(bytes), backend=default_backend())
    decryptor = aes.decryptor()
    decrypted_data = decryptor.update(encrypted_msg) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(decrypted_data) + unpadder.finalize()

msg = 'Hello Alice'
bytes = token_bytes(16)
print('msg: ', msg)
print('bytes: ', bytes)

encrypted_msg = encrypt(Bob_derived_key, msg, bytes)
print('encrypted_msg: ', encrypted_msg)

decrypted_msg = decrypt(Alice_derived_key, encrypted_msg, bytes)
print('decrypted_msg: ', decrypted_msg.decode())

