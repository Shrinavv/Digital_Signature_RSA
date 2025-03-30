from flask import Flask, request, jsonify, send_file, render_template
import os

app = Flask(__name__, static_folder="static", static_url_path="/")

# Correct base directory and receiver folder paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Digital_Signature_RSA/
RECEIVER_FOLDER = os.path.join(BASE_DIR, "receiver")
CHECKED_MESSAGE_PATH = os.path.join(RECEIVER_FOLDER, "checked_message.txt")

# Paths for SSL certificates
CERT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cert.pem")
KEY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "key.pem")

# Create receiver folder if it doesn't exist
if not os.path.exists(RECEIVER_FOLDER):
    os.makedirs(RECEIVER_FOLDER)


# 📩 Route to receive the signed message
@app.route("/api/receive", methods=["POST"])
def receive_message():
    try:
        signed_message = request.form.get("signed_message")

        # Check if message is received
        if not signed_message:
            return jsonify({"error": "❌ No signed message received."}), 400

        # Save the received message to checked_message.txt
        with open(CHECKED_MESSAGE_PATH, "w") as f:
            f.write(signed_message)

        print("✅ Message received and saved successfully!")
        return jsonify({"success": "✅ Message received and saved successfully!"})

    except Exception as e:
        print(f"❌ Error receiving message: {str(e)}")
        return jsonify({"error": f"❌ Internal Server Error: {str(e)}"}), 500


# 📥 Route to download the checked message
@app.route("/api/download", methods=["GET"])
def download_message():
    try:
        if os.path.exists(CHECKED_MESSAGE_PATH):
            return send_file(CHECKED_MESSAGE_PATH, as_attachment=True)
        else:
            return jsonify({"error": "❌ No checked message found to download."}), 404

    except Exception as e:
        print(f"❌ Error downloading message: {str(e)}")
        return jsonify({"error": f"❌ Internal Server Error: {str(e)}"}), 500


# 🟢 Home route for serving index.html
@app.route("/")
def home():
    return app.send_static_file("index.html")


if __name__ == "__main__":
    # ✅ Ensure cert and key files exist
    if os.path.exists(CERT_FILE) and os.path.exists(KEY_FILE):
        app.run(host="0.0.0.0", port=5000, ssl_context=(CERT_FILE, KEY_FILE))
    else:
        print("❌ Error: SSL certificate or key not found. Check paths or regenerate them.")
