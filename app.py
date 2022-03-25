import os
from sre_constants import SUCCESS


from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/teste', methods=['POST'])
def teste():
    if request.method == 'POST':
        print(request.JSON)
        return 'Success',200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
