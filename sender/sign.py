import sys
import os

# Get the parent directory (Digital_Signature_RSA)
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)

# Import required utilities
from utils.rsa_utils import hash_message

# Ask the sender to input the message
message = input("✍️ Enter the message to be signed: ")

# Save the message to message.txt
with open("sender/message.txt", "w") as f:
    f.write(message)
print("📩 Message saved to sender/message.txt successfully!")

# Read sender's private key
try:
    with open("sender/private_key.txt", "r") as f:
        d, n = map(int, f.read().splitlines())
except FileNotFoundError:
    print("❌ Error: private_key.txt not found in sender folder. Run keygen.py first.")
    sys.exit(1)

# Hash and sign the message
hashed_message = hash_message(message)
signature = pow(hashed_message, d, n)

# Write the signed message to signed_message.txt
with open("sender/signed_message.txt", "w") as f:
    f.write(f"{message}\n{signature}")
print("✅ Message signed and saved to sender/signed_message.txt successfully!")
