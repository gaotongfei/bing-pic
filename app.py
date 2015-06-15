from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/bing-image')
def image():
    return send_from_directory("bing_image", "image.jpg")

if __name__ == '__main__':
    app.run(debug=True)
