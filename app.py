import os
from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/teste', methods=['POST'])
def teste():
    if request.method == 'POST':
        print(request.json)
        return "success",200
    else:
        abort(400)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')
