import sys
import os

# Get the parent directory (Digital_Signature_RSA)
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)

# /receiver/verify.py
from utils.rsa_utils import hash_message

# Read receiver's public key
with open("sender/public_key.txt", "r") as f:
    e, n = map(int, f.read().splitlines())

# Read the signed message and signature
with open("receiver/signed_message.txt", "r") as f:
    message, signature = f.read().splitlines()
    signature = int(signature)

# Recompute hash and verify the signature
hashed_message = hash_message(message)
verified_hash = pow(signature, e, n)

if verified_hash == hashed_message:
    print("✅ Signature is valid! Message integrity verified.")
else:
    print("❗ Signature is invalid! Message may have been tampered.")
