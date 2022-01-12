import socket
from uuid import getnode as get_mac
from flask import Flask,jsonify

# Get device details
def get_device_details():
	hostname = socket.gethostname()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	s.close()
	MAC_address = get_mac()
	MAC_address = (':'.join(("%012X" % MAC_address)[i:i+2] for i in range(0, 12, 2)) ).replace(":", "-")
	return hostname,ip,MAC_address
	
app = Flask(__name__)

# Returns device hostname,IP and MAC address
@app.route("/details")
def details():
    hostname,ip,mac = get_device_details()
    out = "Hello!!!....I'm " + hostname + "....My MAC ID is " + mac + "....and My IP address is "+ip
    return out

@app.route("/health")
def health():
    return jsonify(
        status="up"
    )

@app.route("/")
def home():
<<<<<<< HEAD
    return "Hello World! FROM MAIN BRANCH"
=======
    return "Hello Universe"
>>>>>>> e73c36bcba1c7f98a2a63c318f8de4cf08ea0099
   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
	
