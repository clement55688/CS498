from flask import Flask, jsonify
import subprocess
import socket

app = Flask(__name__)

# HTTP POST to trigger CPU stress
@app.route('/', methods=['POST'])
def stress_cpu():
    # Start stress_cpu.py as a subprocess
    subprocess.Popen(["python3", "stress_cpu.py"])
    return jsonify(success=True, message="CPU stress started")

# HTTP GET to return the private IP address
@app.route('/', methods=['GET'])
def get_ip():
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return jsonify(ip_address=private_ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
