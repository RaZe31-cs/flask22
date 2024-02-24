from flask import Flask, render_template, url_for
import os

app = Flask(__name__, static_folder='static')


@app.route('/training/<prof>')
def train(prof):
    path = os.path.join('..', 'static', 'img', 'build.jpg')
    if 'инженер' in prof:
        path = os.path.join('..', 'static', 'img', 'ingener.jpg')
    return render_template('index2.html', title=prof, path=path)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
