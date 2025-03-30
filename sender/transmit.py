#++++++++++++++++++++++++++++++ Using shutil to tranfer files ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import shutil
# import os

# # Define file paths
# sender_path = "sender/signed_message.txt"
# receiver_path = "receiver/signed_message.txt"

# # Check if the signed message file exists
# if os.path.exists(sender_path):
#     # Check if the file already exists in the receiver folder
#     if os.path.exists(receiver_path):
#         print("⚠️ Warning: signed_message.txt already exists in receiver folder. Overwriting...")

#     # Simulate sending the file by moving it to the receiver folder
#     shutil.move(sender_path, receiver_path)
#     print(f"📡 Message successfully transmitted to {receiver_path}")
# else:
#     print("❌ Error: signed_message.txt not found in sender folder. Run sign.py first.")

#+++++++++++++++++++++++++++++++++++Using HTTPS to transfer files+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import requests
import os
import urllib3

# Disable SSL warnings for self-signed certificates (for local testing)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define API endpoint of receiver using HTTPS
url = "https://127.0.0.1:5000/api/receive"  # HTTPS enabled now!

# Define the path of the signed message
sender_path = "../sender/signed_message.txt"

# Check if the signed message file exists
if os.path.exists(sender_path):
    # Read the signed message
    with open(sender_path, "r") as f:
        signed_message = f.read()

    # Send the signed message to the receiver using HTTPS POST
    try:
        # ✅ Send with verification disabled for self-signed certificate
        response = requests.post(url, data={"signed_message": signed_message}, verify=False)

        # Check for successful transmission
        if response.status_code == 200:
            print("📡 Message successfully transmitted to the receiver via HTTPS!")
        else:
            print(f"❌ Error: Failed to transmit the message. Status code: {response.status_code}")

    except Exception as e:
        print(f"❌ Error: {str(e)}")
else:
    print("❌ Error: signed_message.txt not found in sender folder. Run sign.py first.")
