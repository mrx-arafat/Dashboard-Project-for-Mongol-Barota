from flask import Flask, render_template, send_from_directory, Response
from cameras import stream_cam_1

app = Flask(__name__, static_url_path='')


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

# @app.route('/arm-cam-1')
# def arm_cam_1():
#    return Response(stream_cam_1(),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/soil')
def soil_page():
    return render_template('soil.html')


@app.route('/rock')
def rock_page():
    return render_template('rock.html')


@app.route('/science-cam')
def science_cam():
    return render_template('science-cam.html')


@app.route('/camera3.html')
def camera3():
    return render_template('camera3.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
