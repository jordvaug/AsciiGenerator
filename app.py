from flask import Flask, request
from transform import Transform
from cache import Cache
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
CACHE_CAPACITY = 100

__author__ = 'Jordan Vaughn'
app = Flask(__name__)

def valid_extension(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return {'sucess': 'true', 'message': 'Welcome to the ASCII Generator!'}, 200

@app.route("/image", methods=['POST'])
def upload_file():
    if 'file' not in request.files or request.files['file'].filename == '':
        return {'sucess': 'false', 'message': 'File not found'}, 400

    file = request.files['file']

    if file and valid_extension(file.filename):
        cache = Cache(CACHE_CAPACITY)       
        hashed_key = cache.hash_name(file)
        if cache.get(hashed_key) != -1:
            print('Found in cache')
            return {'sucess': 'true', 'message': cache.get(hashed_key)}, 200
        else:
            im = Transform.load_image(Transform, file) 
            grayscale = Transform.grayscale_image(Transform, im)
            resized_image = Transform.resize_image(Transform, grayscale)
            art = Transform.convert_image_to_ascii(Transform, resized_image)
            cache.put(hashed_key, art)
            for line in art:
                print(line)
            return {'sucess': 'true', 'message': art}, 200

if __name__ == '__main__':
    app.run(debug=True)