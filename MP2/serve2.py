from flask import Flask, jsonify
import subprocess
import socket
import time

app = Flask(__name__)

# Record the start time
start_time = time.time()

# HTTP POST to trigger CPU stress
@app.route('/', methods=['POST'])
def stress_cpu():
    # Start stress_cpu.py as a subprocess
    # subprocess.Popen(["python3", "stress_cpu.py"])
    # return jsonify(success=True, message="CPU stress started")
    return '123'

# HTTP GET to return different private IP addresses based on elapsed time
@app.route('/', methods=['GET'])
def get_ip():
    elapsed_time = time.time() - start_time
    if elapsed_time <= 300:  # 0~5 minutes
        private_ip = "192.168.1.100"  # Mocked private IP
    elif elapsed_time <= 900:  # 5~15 minutes
        # Two kinds of IPs, alternating each call
        private_ips = ["192.168.1.101", "192.168.1.102"]
        index = int(elapsed_time // 300) % 2
        private_ip = private_ips[index]
    else:  # After 15 minutes
        # Three kinds of IPs, alternating each call
        private_ips = ["192.168.1.103", "192.168.1.104", "192.168.1.105"]
        index = int(elapsed_time // 300) % 3
        private_ip = private_ips[index]
    
    return jsonify(ip_address=private_ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
