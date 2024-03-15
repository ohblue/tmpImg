from flask import Flask, request, jsonify
import os
import tempfile
import time

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi vercel!'
    
# 存储临时上传的图片的字典，格式为 {图片ID: (图片路径, 上传时间)}
temp_images = {}

# 上传图片的API端点
@app.route('/api/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No selected image file'}), 400

    _, temp_filename = tempfile.mkstemp(suffix='.jpg')  # 生成一个临时文件路径
    image_file.save(temp_filename)
    
    image_id = str(int(time.time()))  # 使用当前时间作为图片ID
    temp_images[image_id] = (temp_filename, time.time())

    return jsonify({'image_id': image_id}), 200

# 获取图片的API端点
@app.route('/api/image/<image_id>', methods=['GET'])
def get_image(image_id):
    if image_id not in temp_images:
        return jsonify({'error': 'Image not found or expired'}), 404

    image_path, _ = temp_images[image_id]
    with open(image_path, 'rb') as f:
        image_data = f.read()

    return image_data, 200, {'Content-Type': 'image/jpeg'}

# 删除图片的API端点
@app.route('/api/delete/<image_id>', methods=['DELETE'])
def delete_image(image_id):
    if image_id not in temp_images:
        return jsonify({'error': 'Image not found'}), 404

    image_path, _ = temp_images.pop(image_id)
    os.remove(image_path)

    return jsonify({'message': 'Image deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=False)
