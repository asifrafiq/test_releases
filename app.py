from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    """
    A simple route that returns a welcome message.
    """
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    # Use 0.0.0.0 to ensure the server is accessible from outside the container
    app.run(host='0.0.0.0', port=5000)


