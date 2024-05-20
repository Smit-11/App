from flask import Flask, render_template
import os

# Create Flask app
app = Flask(__name__)

# Initialize the LED state
led_state = "OFF"

# Custom Jinja environment to load templates from the same directory as app.py
template_path = os.path.abspath(os.path.dirname(__file__))
app.jinja_loader.searchpath.append(template_path)

@app.route('/')
def index():
    global led_state
    return render_template('index.html', led_state=led_state)

@app.route('/LED=ON')
def led_on():
    global led_state
    led_state = 'ON'
    return 'LED=ON'

@app.route('/LED=OFF')
def led_off():
    global led_state
    led_state = 'OFF'
    return 'LED=OFF'

@app.route('/state')
def state():
    global led_state
    return f'LED={led_state}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)


