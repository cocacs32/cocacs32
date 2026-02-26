from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Geo IP AI Assistant"

@app.route('/api/ip', methods=['GET'])
def get_ip_info():
    ip_address = request.args.get('ip')
    # Here you would integrate your IP handling logic
    return jsonify({'ip': ip_address, 'info': 'Sample IP info.'})

if __name__ == '__main__':
    app.run(debug=True)