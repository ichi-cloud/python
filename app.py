from flask import Flask, request, jsonify, abort, send_from_directory
from nanoid import generate
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    files = os.listdir('static')
    images = [f'<img src="/static/{f}" style="max-width: 200px; margin: 10px;">' for f in files if f.endswith(('.png', '.jpg', '.jpeg'))]
    return '<h1>HELLO</h1>' + ''.join(images)

@app.route('/greet/<name>')
def greet(name):
    return f'hello, {name}!'

@app.route('/v1/photos', methods=['POST'])
def post_photos():
    file = request.files.get('file')
    if file:
        if file.content_type not in ['image/png', 'image/jpeg']:
            abort(400, description='Invalid file type. Only PNG and JPEG are allowed.')

        ext = 'png' if file.content_type == 'image/png' else 'jpg'
        filename = f'{generate(size=4)}.{ext}'
        file.save(f'static/{filename}')
        resp = {'url': f'/static/{filename}'}
        return jsonify(resp)
    else:
        abort(400, description='No file provided.')

if __name__ == '__main__':
    app.run()