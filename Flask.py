from flask import Flask, request, jsonify, json
app = Flask(__name__)
@app.route('/api/v1/status', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify(data)
    if request.method == 'GET':
        message = "OK"
        return jsonify(message), 200

if __name__ == '__main__':
    app.run(host='localhost', port=8000)