from flask import Flask, request, jsonify, abort, send_from_directory
from nanoid import generate
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    files = os.listdir('static')
    images = [f'<img src="/static/{f}" style="max-width: 200px; margin: 10px;">' for f in files if f.endswith(('.png', '.jpg', '.jpeg'))]

    form = '''
    <h2>画像アップロード</h2>
    <form action="/v1/photos" method="POST" enctype="multipart/form-data">
      <input type="file" name="file" accept="image/*" capture="environment" required>
      <button type="submit">アップロード</button>
    </form>
    '''

    return '<h1>Hello</h1>' + form + ''.join(images)


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

@app.route('/v1/photos/<filename>', methods=['DELETE'])
def delete_photo(filename):
    filepath = os.path.join('static', filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        return jsonify({'message': f'{filename} deleted.'}), 200
    else:
        abort(404, description='File not found.')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

    # https://github.com/ichi-cloud/pythonのリポジトリ

#git add app.py
#git commit -m "Add image upload form to root page"
#git push origin main
