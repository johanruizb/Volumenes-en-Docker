from flask import Flask
app = Flask(__name__)
app.run(host='0.0.0.0')
@app.route('/', methods=['GET'])
def hello_world():
    return {
        'hello': 'world'
    }