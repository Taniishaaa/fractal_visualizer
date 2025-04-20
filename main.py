from flask import Flask, render_template, request, send_file
from fractals import mandelbrot, julia
import matplotlib.cm as cm
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fractal')
def generate_fractal():
    width = int(request.args.get('width', 800))
    height = int(request.args.get('height', 600))
    zoom = float(request.args.get('zoom', 1.0))
    x_center = float(request.args.get('x_center', 0.0))
    y_center = float(request.args.get('y_center', 0.0))
    max_iter = int(request.args.get('max_iter', 200))
    mode = request.args.get('mode', 'mandelbrot')
    color_map = request.args.get('colormap', 'inferno')  # Fixed the parameter name to match frontend

    if mode == 'mandelbrot':
        data = mandelbrot(width, height, zoom, x_center, y_center, max_iter)
    else:
        data = julia(width, height, zoom, x_center, y_center, max_iter)

    norm_data = data / max_iter
    rgba = cm.get_cmap(color_map)(norm_data)
    img = (rgba[:, :, :3] * 255).astype(np.uint8)

    pil_img = Image.fromarray(img)
    buf = io.BytesIO()
    pil_img.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
