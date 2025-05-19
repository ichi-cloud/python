from flask import Flask, request, jsonify, abort
from nanoid import generate
import os

app = Flask(__name__)

initial_image = 'SkxF.jpg'  # ← ここを残した画像に合わせて変更

@app.route('/', methods=['GET'])
def root():
    files = os.listdir('static')
    images_html = ''
    for f in files:
        if f.endswith(('.png', '.jpg', '.jpeg')):
            delete_button = ''
            if f != initial_image:
                delete_button = f'''
                    <form action="/v1/photos/{f}" method="POST" style="display:inline;">
                        <input type="hidden" name="_method" value="DELETE">
                        <button type="submit">削除</button>
                    </form>
                '''
            images_html += f'<div style="display:inline-block;">' \
                           f'<img src="/static/{f}" style="max-width:200px;"><br>{delete_button}</div>'

    form = '''
    <h2>画像アップロード</h2>
    <form action="/v1/photos" method="POST" enctype="multipart/form-data">
      <input type="file" name="file" accept="image/*" capture="environment" required>
      <button type="submit">アップロード</button>
    </form>
    '''
    return '<h1>hello</h1>' + form + images_html


@app.route('/v1/photos', methods=['POST'])
def post_photos():
    file = request.files.get('file')
    if file:
        if file.content_type not in ['image/png', 'image/jpeg']:
            abort(400, description='Invalid file type. Only PNG and JPEG are allowed.')

        ext = 'png' if file.content_type == 'image/png' else 'jpg'
        filename = f'{generate(size=4)}.{ext}'
        file.save(f'static/{filename}')
        return jsonify({'url': f'/static/{filename}'})
    else:
        abort(400, description='No file provided.')


@app.route('/v1/photos/<filename>', methods=['POST'])
def delete_photo(filename):
    if request.form.get('_method') == 'DELETE':
        if filename == initial_image:
            abort(403, description='Cannot delete the initial image.')
        filepath = os.path.join('static', filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            return jsonify({'status': 'deleted'})
        else:
            abort(404, description='File not found.')
    else:
        abort(405)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

    # https://github.com/ichi-cloud/pythonのリポジトリ

#git add app.py
#git commit -m "Add image upload form to root page"
#git push origin main
