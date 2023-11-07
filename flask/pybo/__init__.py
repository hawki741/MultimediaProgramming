from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_pybo():
    return 'hello~~~pybo 패키지~~~'