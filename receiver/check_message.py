import os

# Path to signed_message.txt in receiver folder
receiver_path = "receiver/signed_message.txt"

# Check if the signed message file exists
if os.path.exists(receiver_path):
    # Read the content of the file
    with open(receiver_path, "r") as f:
        content = f.readlines()

    # Validate file format (should contain 2 lines: message and signature)
    if len(content) == 2:
        # Extract message and signature
        message = content[0].strip()
        signature = content[1].strip()
        
        # Display message and signature
        print(f"📨 Received Message: {message}")
        print(f"✍️ Signature: {signature}")
    else:
        print("❌ Error: File format invalid or message not received properly.")
else:
    print("❌ Error: signed_message.txt not found in receiver folder.")
