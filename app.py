from flask import Flask, request, jsonify
from ocrService.pytesseractUrlOcrService import process_image

app = Flask(__name__)


@app.route('/ocr', methods=["POST"])
def post_url_for_ocr():

    try:
        url = request.json['image_url']
        output = process_image(url)
        return jsonify({
            "captcha": output
        })

    except:
        return jsonify({
            "error": "try {'image_url': 'https://asdfg'}"
        })

if __name__ == '__main__':
    app.run()
