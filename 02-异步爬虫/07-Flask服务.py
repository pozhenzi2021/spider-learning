from flask import Flask
import time

app = Flask("__main__")


@app.route('/aaa')
def index_pzz():
    time.sleep(2)
    return 'hello aaa'


@app.route('/bbb')
def index_jay():
    time.sleep(2)
    return 'hello bbb'


@app.route('/ccc')
def index_tom():
    time.sleep(2)
    return 'hello ccc'


if __name__ == '__main__':
    app.run(threaded=True)
