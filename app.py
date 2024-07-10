from flask import Flask, jsonify, request
from font import process_fonts

app = Flask(__name__)

# Route for the root URL
@app.route('/')
def home():
    return "Stylish Name"

# Route for Converted Fonts Data
@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    if 'text' in data:
        text = data['text']
        fonts_directory = "E:\\fonts_directory"
        font_data = process_fonts(fonts_directory, text)
        response = {'text': text, 'data': font_data}
    else:
        response = {'error': 'No text provided'}
    print(response)
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)
