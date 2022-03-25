import os
from sre_constants import SUCCESS
from urllib import request

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/teste', methods=['POST'])
def teste():
    if request.method == 'POST':
        print(request.JSON)
        return 'Success',200
    else:
        abort(400)


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
