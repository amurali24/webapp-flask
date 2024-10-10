from flask import Flask, request, jsonify, render_template, redirect, url_for
import random
import string

app = Flask(__name__)

# Home page with welcome message and options
@app.route('/')
def index():
    return render_template('index.html')

# Handle random number generation
@app.route('/generate_random_number', methods=['POST'])
def generate_random_number():
    min_val = int(request.form.get('min', 0))
    max_val = int(request.form.get('max', 100))
    number = random.randint(min_val, max_val)
    result = f"Random Number: {number}"
    return render_template('result.html', result=result)

# Handle random text generation
@app.route('/generate_random_text', methods=['POST'])
def generate_random_text():
    length = int(request.form.get('length', 10))
    letters = string.ascii_letters + string.digits + string.punctuation + ' '
    result_str = ''.join(random.choice(letters) for _ in range(length))
    result = f"Random Text: {result_str}"
    return render_template('result.html', result=result)

# Handle Fibonacci sequence generation
@app.route('/generate_fibonacci', methods=['POST'])
def generate_fibonacci():
    n = int(request.form.get('n', 10))
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    result = f"Fibonacci Sequence: {seq[:n]}"
    return render_template('result.html', result=result)

# Handle Tribonacci sequence generation
@app.route('/generate_tribonacci', methods=['POST'])
def generate_tribonacci():
    n = int(request.form.get('n', 10))
    seq = [0, 0, 1]
    for i in range(3, n):
        seq.append(seq[i-1] + seq[i-2] + seq[i-3])
    result = f"Tribonacci Sequence: {seq[:n]}"
    return render_template('result.html', result=result)

# Handle random haiku generation
@app.route('/generate_random_haiku', methods=['POST'])
def generate_random_haiku():
    five_syllables = [
        "Whispering winds blow",
        "An old silent pond",
        "Light of the moon shines",
        "Snowflakes softly fall",
        "Gentle morning breeze"
    ]
    seven_syllables = [
        "Leaves dance under moonlit skies",
        "A frog leaps into the pond",
        "Shadows stretch across the land",
        "Silence echoes in the night",
        "Flowers bloom with vibrant hues"
    ]
    haiku = f"{random.choice(five_syllables)}<br>{random.choice(seven_syllables)}<br>{random.choice(five_syllables)}"
    result = f"Random Haiku:<br>{haiku}"
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False, threaded=False)
