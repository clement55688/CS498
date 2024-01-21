from flask import Flask, request, jsonify

app = Flask(__name__)
seed_value = 0  # Default seed value

@app.route('/', methods=['GET'])
def get_seed():
    return str(seed_value)

@app.route('/', methods=['POST'])
def update_seed():
    global seed_value
    data = request.get_json()
    seed_value = data.get('num', seed_value)  # Update seed value if 'num' is provided
    return jsonify(success=True, new_value=seed_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)