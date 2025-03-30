import sys
import os

# Get the parent directory (Digital_Signature_RSA)
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)
# /sender/keygen.py
from utils.rsa_utils import generate_keys

# Generate sender's keys and store them
generate_keys("sender")
print("✅ Sender's keys generated successfully!")
